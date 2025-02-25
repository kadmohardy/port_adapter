from ports.weather_port import WeatherPort
from domain.weather.exceptions import LocationNotFoundError
from infrastructure.logging_adapter import get_logger

logger = get_logger()

class WeatherService:
    def __init__(self, weather_port: WeatherPort):
        self.weather_port = weather_port         

    def get_weather_information(self, location_id: str):
        weather_list = self.weather_port.get_weather_information(location_id)
        if not weather_list:
            raise LocationNotFoundError(f"Weather information for location with ID {location_id} not found")

        return weather_list