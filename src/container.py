
import json
from dependency_injector import containers, providers
from pydantic_settings import BaseSettings
from application.weather_service import WeatherService
from infrastructure.weather.weather_adapter import AccuWeatherAdapter
from application.unit_of_work import SqlAlchemyUnitOfWork

class ApplicationContainer(containers.DeclarativeContainer):
    """Dependency Injection container for the application (application-level dependencies)
    see https://github.com/ets-labs/python-dependency-injector for more details
    """
    print("Starting dependencies injection container")
    weather_service = providers.Factory(
        WeatherService,
        weather_port=AccuWeatherAdapter()
    )

 


