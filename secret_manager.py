from dotenv import load_dotenv
import os


class SecretManager:
    load_dotenv()

    @staticmethod
    def get_secret(secret: str) -> str:
        return os.environ.get(secret)


class StravaSecretManager(SecretManager):
    __id = 'strava_id'
    __secret = 'strava_secret'
    __refresh_token = 'strava_refresh_token'

    @property
    def client_id(self):
        return self.get_secret(self.__id)

    @property
    def strava_secret(self):
        return self.get_secret(self.__secret)

    @property
    def strava_refresh_token(self):
        return self.get_secret(self.__refresh_token)


class MyFitnessPalSecretManager(SecretManager):
    __username = 'myfitnesspal_username'
    __secret = 'myfitnesspal_secret'

    @property
    def my_fitness_pal_secret(self):
        return self.get_secret(self.__secret)

    @property
    def my_fitness_pal_username(self):
        return self.get_secret(self.__username)
