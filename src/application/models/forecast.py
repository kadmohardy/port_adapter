from dataclasses import dataclass
from domain.weather.entities import Weather
from pydantic import BaseModel

class ForecastItem(BaseModel):
    date: str
    clothes: list

class ForecastResponse(BaseModel):
    clothes: list[ForecastItem] # type: ignore

    def __init__(self, weather_list: list[Weather]): 
        print(self._parse_weather(weather_list))
        super().__init__(clothes=self._parse_weather(weather_list))

    def _parse_weather(self, weather_list):
        forecast = [] 
        for weather in weather_list:
            clothes = weather.get_best_clothes()
            data = weather.date
            forecast_item = ForecastItem(date=data, clothes=clothes)
            forecast.append(forecast_item)
        return forecast
    



