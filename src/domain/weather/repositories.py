import abc
from typing import Set
from domain.weather.entities import Weather

class WeatherAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, weather: Weather):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, id) -> Weather:
        raise NotImplementedError()

