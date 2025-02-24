from ports.weather_port import WeatherPort
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError
from infrastructure.logging_adapter import get_logger
from application.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork
logger = get_logger()

class WeatherService:
    def __init__(self, weather_port: WeatherPort, uow: AbstractUnitOfWork = SqlAlchemyUnitOfWork()):
        self.weather_port = weather_port
        self.uow = uow

    def get_weather_information(self, location_id: str) -> Weather:
        weather = self.weather_port.get_weather_information(location_id)
        if not weather:
            raise LocationNotFoundError(f"Weather information for location with ID {location_id} not found")
        with self.uow:
            print("Inserting item on database")
            self.uow.weather.add(weather)
            self.uow.commit() 
        return weather