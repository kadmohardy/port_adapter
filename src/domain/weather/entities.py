from pydantic import BaseModel

class Weather(BaseModel):
    id: str
    temperature: float
    wether_text: str
