import logging

from sqlalchemy import String, Integer, MetaData, Table, Float
from sqlalchemy.sql.schema import Column

from domain.weather.entities import Weather
from sqlalchemy.orm import  registry, mapper

mapper_registry = registry()
metadata = MetaData()

logger = logging.getLogger(__name__)

weather_table = Table(
    "weather",
    metadata,
    Column("location_id", Integer, primary_key=True, autoincrement=True),
    Column("weather_text", String(255)),
    Column("temperature", Float, nullable=False),
)

def start_mappers(): 
    print("mapping weather")
    mapper_registry.map_imperatively(Weather, weather_table)

