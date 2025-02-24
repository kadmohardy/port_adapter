import logging

from sqlalchemy import String, Integer, MetaData, Table, Float, DateTime
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import  registry
from datetime import datetime
from pytz import timezone

from domain.weather.entities import Weather

mapper_registry = registry()
metadata = MetaData()

logger = logging.getLogger(__name__)
UTC = timezone('UTC')

weather_table = Table(
    "weather",
    metadata,
    Column("location_id", Integer, primary_key=True, autoincrement=True),
    Column("weather_text", String(255)),
    Column("temperature", Float, nullable=False),
    Column("created_at", DateTime, default=datetime.now()),
    Column("update_at", DateTime, default=datetime.now()),
)

def start_mappers(): 
    print("mapping weather")
    mapper_registry.map_imperatively(Weather, weather_table)

