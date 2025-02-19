from fastapi import APIRouter, HTTPException, Depends
from application.weather_service import WeatherService
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError
from infrastructure.logging_adapter import get_logger
from infrastructure.weather_adapter import AccuWeatherAdapter
from typing import Annotated

logger = get_logger()

router = APIRouter(prefix="/weather")

def get_weather_service() -> WeatherService:
    return WeatherService(AccuWeatherAdapter())

@router.get("/{location_id}")
def get_user(location_id: str, weather_service: Annotated[WeatherService, Depends(get_weather_service)]):
    logger.info(f"Trying to get weather information for LocationID")

    try:
        print(f"Trying to get weather information for LocationID {location_id}")
        return weather_service.get_weather_information(location_id)
    except LocationNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

