import requests
import json
import urllib.parse as urlp

class ApiResource:
    def __init__(self) -> None:
        self.session = requests.Session()
        
    def get_request(self, url: str, **kwargs):
        with self.session as s:
            response = s.get(url, **kwargs)
            response.raise_for_status()
        return response

    def post_request(self, url, **kwargs):
        with self.session as s:
            response = s.post(url, **kwargs)
            response.raise_for_status()
        return response


class Strava(ApiResource):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = 'https://www.strava.com/api/v3/'
    
    def get_single_activity(self, id: int) -> dict:
        url = urlp.urljoin(self.base_url, f'activities/{id}')
        return url

if __name__ == "__main__": 
    x = Strava()
    print(x.get_single_activity(123))
    y = {
        "a": 123,
        "b": 12556
    }
    print(y['a'])
    a = ''
    if a:
        print ('A')
    else:
        print('nie')