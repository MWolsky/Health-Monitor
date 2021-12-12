import datetime
import logging
import pytz
import requests
import time
import urllib3
import atexit
from secret_manager import StravaSecretManager
from typing import Callable, List, Dict
from core.utils.helpers import date_to_unix_timestamp, logging_config, sleep_till_tomorrow, \
    sleep_till_next_quarter_of_hour, open_strava_logs, save_strava_logs, quarter_an_hour_timestamp_counter, \
    daily_timestamp_counter, timestamp_log

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging_config()


class Strava:
    rate_limits = {
        'daily_requests': 1000,
        'quarter_requests': 100
    }

    def __init__(self) -> None:
        self.session = requests.Session()
        self.base_url = 'https://www.strava.com/api/v3/'
        self.auth_url = 'https://www.strava.com/oauth/token'
        self.athlete_url = 'https://www.strava.com/api/v3/athlete/'
        self.athlete_activities_url = f'{self.base_url}athlete/activities/'
        self.activities_url = f'{self.base_url}activities/'
        self.athlete_zones_url = f'{self.athlete_url}zones'
        self.__secret_manager = StravaSecretManager()
        self.access_token = None
        self.token_expires_at = 0
        self.requests_counter = [datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in open_strava_logs()]
        self.__logger = logging.getLogger(__name__)
        self.delete_outdated_logs()
        atexit.register(self.cleanup)

    def cleanup(self):
        save_strava_logs(self.requests_counter)

    def delete_outdated_logs(self) -> None:
        today = datetime.datetime.now(pytz.utc).replace(tzinfo=None).date()
        relevant = [x for x in self.requests_counter if x.date() == today]
        self.requests_counter = relevant

    def check_for_limits_decorator(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs):
            daily_limit, daily_requests_made = daily_timestamp_counter(self.requests_counter, self.rate_limits['daily_requests']-1)
            quarter_limit, quarter_requests_made = quarter_an_hour_timestamp_counter(self.requests_counter,
                                                                                     self.rate_limits[
                                                                                         'quarter_requests']-1)
            if daily_limit and quarter_limit:
                self.__logger.info(f'Making request...\nYou made {daily_requests_made} requests today '
                                   f'and {quarter_requests_made} this quarter of an hour.')
                res = func(self, *args, **kwargs)
                self.requests_counter.append(timestamp_log())
                return res
            elif daily_limit and not quarter_limit:
                self.__logger.warning(f'15 min rate limit reached! You made {quarter_requests_made} requests'
                                      f' this quarter of an hour\n'
                                      f'Program will be waiting till next quarter of an hour...')
                sleep_till_next_quarter_of_hour()
                self.delete_outdated_logs()
                res = func(self, *args, **kwargs)
                self.requests_counter.append(timestamp_log())
                return res
            elif (not daily_limit and quarter_limit) or (not daily_limit and not quarter_limit):
                self.__logger.warning(f'Daily rate limit reached! You made {daily_requests_made} requests today.\n'
                                      f'Program will be waiting till tomorrow utc. Consider killing the program!')
                sleep_till_tomorrow()
                self.delete_outdated_logs()
                res = func(self, *args, **kwargs)
                self.requests_counter.append(timestamp_log())
                return res
        return wrapper

    @check_for_limits_decorator
    def get_request(self, url: str, **kwargs):
        with self.session as s:
            response = s.get(url, **kwargs)
            response.raise_for_status()
        return response.json()

    def get_request_paginated(self, url: str, after: str = None, before: str = None, **kwargs):
        """use after and before in yyyy-mm-dd format only in relevant endpoints. e.g. activities"""
        params = {'per_page': 200, 'page': 1}
        if after and not before:
            after_timestamp = date_to_unix_timestamp(after)
            params['after'] = after_timestamp
        elif before and not after:
            before_timestamp = date_to_unix_timestamp(before)
            params['before'] = before_timestamp
        elif after and before:
            after_timestamp = date_to_unix_timestamp(after)
            before_timestamp = date_to_unix_timestamp(before)
            params['after'] = after_timestamp
            params['before'] = before_timestamp

        page = True
        response = []
        while page:
            chunk = self.get_request(url, params=params, **kwargs)
            if chunk:
                response.append(chunk)
            params['page'] += 1
            if not chunk:
                page = False
        return response

    def post_request(self, url: str, **kwargs):
        with self.session as s:
            response = s.post(url, **kwargs)
            response.raise_for_status()
        return response.json()

    def refresh_access_token_decorator(func: Callable):
        def wrapper(self, *args, **kwargs):
            unix_time = time.time()
            to_expiration = self.token_expires_at - unix_time
            if self.access_token is None or to_expiration < 60:
                refresh_response = self.get_access_token()
                access_token = refresh_response['access_token']
                expires_at = refresh_response['expires_at']
                self.access_token = access_token
                self.token_expires_at = expires_at
            return func(self, *args, **kwargs)
        return wrapper

    @property
    def header(self):
        return dict(
            Authorization=f'Bearer {self.access_token}'
        )

    @refresh_access_token_decorator
    def detailed_activity(self,
                          activity_id: int,
                          params: dict = None) -> Dict:
        """
        Returns the given activity that is owned by the authenticated athlete.
        Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
        :param activity_id: activity identifier
        :param params: like {per_page: 200, page: 1}
        :return: dict with activity info
        """
        url = f'{self.activities_url}{activity_id}'
        activity = self.get_request(url, headers=self.header, params=params)
        return activity

    @refresh_access_token_decorator
    def activities(self, after: str = None, before: str = None):
        """
        Returns the activities of an athlete for a specific identifier. Requires activity:read.
        Only Me activities will be filtered out unless requested by a token with activity:read_all.
        :param after: date in yyyy-mm-dd. Activities after this date will be queried
        :param before: date in yyyy-mm-dd. Avticities before this date will be queried
        :return: list of dicts. Each dict represents activity
        """
        activities = self.get_request_paginated(self.athlete_activities_url,
                                                after=after,
                                                before=before,
                                                headers=self.header)
        flatten = [act for batch in activities for act in batch]
        return flatten

    @refresh_access_token_decorator
    def laps(self,
             activity_id: int,
             params: dict = None) -> List[Dict]:
        """
        Returns the laps of an activity identified by an identifier.
        Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
        :param activity_id: activitiy identifier
        :param params: like {per_page: 200, page: 1}
        :return: list of dicts. Each dict represents a lap
        """
        laps = self.get_request(f'{self.activities_url}{activity_id}/laps', headers=self.header, params=params)
        return laps

    @refresh_access_token_decorator
    def athlete_me(self, params: dict = None) -> Dict:
        """
        Returns the currently authenticated athlete. Tokens with profile:read_all scope will receive a detailed athlete
         representation; all others will receive a summary representation.
        :param params: like {per_page: 200, page: 1}
        :return: dict with athlete info
        """
        athlete = self.get_request(self.athlete_url, headers=self.header, params=params)
        return athlete

    @refresh_access_token_decorator
    def athlete_zones(self, params: dict = None) -> List[Dict]:
        """
        Returns the the authenticated athlete's heart rate and power zones. Requires profile:read_all.
        :param params: like {per_page: 200, page: 1}
        :return: list of dicts. Each dict is a zone
        """
        zones = self.get_request(self.athlete_zones_url, headers=self.header, params=params)
        return zones

    @refresh_access_token_decorator
    def athlete_stats(self,
                      athlete_id: int,
                      params: dict = None) -> Dict:
        """
        Returns the activity stats of an athlete. Only includes data from activities set to Everyone visibilty.
        :param athlete_id: athlete identifier
        :param params: like {per_page: 200, page: 1}
        :return: dict which contains athlete statistics
        """
        url = f'{self.base_url}athletes/{athlete_id}/stats'
        athlete_stats = self.get_request(url, headers=self.header, params=params)
        return athlete_stats

    def get_access_token(self) -> Dict:
        """
        Uses refresh token to get new authentication access token.
        :return: dict with access token and info when it will be expired
        """
        payload = dict(
            client_id=self.__secret_manager.client_id,
            client_secret=self.__secret_manager.strava_secret,
            refresh_token=self.__secret_manager.strava_refresh_token,
            grant_type='refresh_token',
            f='json'
        )
        token = self.post_request(self.auth_url, data=payload, verify=False)
        return token
