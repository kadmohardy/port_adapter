
import requests
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError

from ports.weather_port import WeatherPort
from requests.auth import HTTPBasicAuth
from configs import config

class AccuWeatherAdapter(WeatherPort):
    def _get_url(self, location_id: str) -> str: 
        api_key = config.app_config.accu_weather_api_key
        return config.app_config.accu_weather_url + '/' + location_id + '?apikey=' + api_key

    def get_weather_information(self, location_id: str) -> Weather:
        print("Searching weather information on")
        url = self._get_url(location_id)
        r = requests.get(url).json()
        match r: 
            case {'Code': '400'}:
                raise LocationNotFoundError("No weather information for locationID")
            case _:
                response = r[0]
                return Weather(id=location_id, temperature=response['Temperature']['Metric']['Value'], wether_text=response['WeatherText'])


