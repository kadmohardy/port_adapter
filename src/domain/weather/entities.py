from dataclasses import dataclass
from pydantic import BaseModel, EmailStr

class Weather(BaseModel):
    id: str
    temperature: float
    weather_text: str
