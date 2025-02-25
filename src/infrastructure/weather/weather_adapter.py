
import requests
import logging
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError
from ports.weather_port import WeatherPort
from requests.auth import HTTPBasicAuth
from configs import config
logger = logging.getLogger(__name__)

class AccuWeatherAdapter(WeatherPort):
    def _get_url(self, location_id: int) -> str: 
        url = config.app_config.accu_weather_url + '/daily/5day/' + location_id + '?' + 'apikey=' + config.app_config.accu_weather_api_key + "&details=true"
        return url
    
    def _translate_weather_information_from_accu(self, forecast_list): 
        translated_response_list = list()
        for forecast_item in forecast_list:
            date = forecast_item['Date']
            temperature = forecast_item['Temperature']['Maximum']['Value']
            day_rain_probability = forecast_item['Day']['RainProbability']
            night_rain_probability = forecast_item['Night']['RainProbability']
            day_snow_probability = forecast_item['Day']['SnowProbability']
            night_snow_probability = forecast_item['Night']['SnowProbability']
            day_ice_probability = forecast_item['Day']['IceProbability']
            night_ice_probability = forecast_item['Night']['IceProbability']
            translated_response = Weather(temperature=temperature, 
                                          day_rain_probability=day_rain_probability,
                                          night_rain_probability=night_rain_probability, 
                                          day_snow_probability=day_snow_probability, 
                                          night_snow_probability=night_snow_probability, 
                                          day_ice_probability=day_ice_probability, 
                                          night_ice_probability=night_ice_probability, 
                                          date=date)
            translated_response_list.append(translated_response)
        return translated_response_list

    def get_weather_information(self, location_id: int) -> Weather:
        url = self._get_url(location_id)
        response = requests.get(url).json()
        match response: 
            case {'Code': '400'}:
                raise LocationNotFoundError("No weather information for locationID")
            case _:
                print(response)
                translated_response = self._translate_weather_information_from_accu(response['DailyForecasts'])
                return translated_response

        
