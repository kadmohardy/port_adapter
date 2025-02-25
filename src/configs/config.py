from pydantic import BaseModel
import os

class Configurations(BaseModel):
    # accu_weather_url: str = os.getenv("ACCU_WEATHER_URL")
    # accu_weather_api_key: str = os.getenv("ACCU_WEATHER_API_KEY")
    accu_weather_url: str = "https://dataservice.accuweather.com/forecasts/v1"
    accu_weather_api_key: str = "727ZVcS3pDX63coQz8KHE76vi1OSNmPR"
app_config = Configurations()

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "postgres")
    user, db_name = "postgres", "port_adapter_db"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"

def get_email_host_and_port():
    host = os.environ.get("EMAIL_HOST", "localhost")
    port = 11025 if host == "localhost" else 1025
    http_port = 18025 if host == "localhost" else 8025
    return dict(host=host, port=port, http_port=http_port)




