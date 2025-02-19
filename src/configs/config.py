from pydantic import BaseModel
import os

class Configurations(BaseModel):
    # accu_weather_url: str = os.getenv("ACCU_WEATHER_URL")
    # accu_weather_api_key: str = os.getenv("ACCU_WEATHER_API_KEY")
    accu_weather_url: str = "http://dataservice.accuweather.com/currentconditions/v1"
    accu_weather_api_key: str = "sRfnrvmAbE30ySXdruJAey5zKfNGq5Ge"
app_config = Configurations()

# ACCU_WEATHER_URL=http://dataservice.accuweather.com/currentconditions/v1
# ACCU_WEATHER_API_KEY=sRfnrvmAbE30ySXdruJAey5zKfNGq5Ge