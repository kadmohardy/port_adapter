import abc
from typing import Set
from domain.weather.entities import Weather


class WeatherAbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  

    @abc.abstractmethod
    def add(self, weather: Weather):
        self._add(weather)
        self.seen.add(weather)

    @abc.abstractmethod
    def get(self, id) -> Weather:
        product = self._get(id)
        return product
