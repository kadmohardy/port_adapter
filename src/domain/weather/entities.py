from dataclasses import dataclass
from pydantic import BaseModel, EmailStr

@dataclass
class Weather:
    location_id: int
    temperature: float
    weather_text: str
