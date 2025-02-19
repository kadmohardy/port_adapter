
import json
from dependency_injector import containers, providers
from pydantic_settings import BaseSettings
from src.ports.weather_port import WeatherPort

class ApplicationContainer(containers.DeclarativeContainer):
    """Dependency Injection container for the application (application-level dependencies)
    see https://github.com/ets-labs/python-dependency-injector for more details
    """

    __self__ = providers.Self()
    
    # user_repository = providers.Factory(
    #     SQLAlchemyUserRepository,
    #     db_session=db_session,
    # )

 


