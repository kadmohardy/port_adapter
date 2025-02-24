import logging

from sqlalchemy import String, Integer, MetaData, Table, Float
from sqlalchemy.sql.schema import Column

from domain.weather.entities import Weather
from sqlalchemy.orm import declarative_base, registry

mapper_registry = registry()

logger = logging.getLogger(__name__)

Base = declarative_base()
metadata = MetaData()

weather_table = Table(
    "weather",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("weather_text", String(255)),
    Column("temperature", Float, nullable=False),
)

def start_mappers():
    logger.info("Starting mappers")
    mapper_registry.map_imperatively(Weather, weather_table)    

