from fastapi import APIRouter, HTTPException, Depends
from application.weather_service import WeatherService
from container import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from domain.weather.entities import Weather
from domain.weather.exceptions import LocationNotFoundError
from infrastructure.logging_adapter import get_logger
from typing import Annotated

logger = get_logger()

router = APIRouter(prefix="/weather")

@router.get("/{location_id}")
@inject
async def get_user(location_id: str, weather_service: WeatherService = Depends(Provide[ApplicationContainer.weather_service])):
    logger.info(f"Trying to get weather information for LocationID")

    try:
        print(f"Trying to get weather information for LocationID {location_id}")
        return weather_service.get_weather_information(location_id)
    except LocationNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

