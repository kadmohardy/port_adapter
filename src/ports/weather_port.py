from typing import Optional
from abc import ABC, abstractmethod
from domain.weather.entities import Weather

class WeatherPort(ABC):
    @abstractmethod
    def get_weather_information(self, location_id: int) -> Optional[Weather]:
        pass

