from ports.weather_port import WeatherPort
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError
from infrastructure.logging_adapter import get_logger
from application.unit_of_work import AbstractUnitOfWork
logger = get_logger()

class WeatherService:
    def __init__(self, weather_port: WeatherPort):
        self.weather_port = weather_port

    def get_weather_information(self, location_id: str) -> Weather:
        print("testando tudo agora")
        print(location_id)

        weather = self.weather_port.get_weather_information(location_id)
        if not weather:
            raise LocationNotFoundError(f"Weather information for location with ID {location_id} not found")
        # with self.uow:
        #     weather = self.uow.weather.add(weather)

        return weather