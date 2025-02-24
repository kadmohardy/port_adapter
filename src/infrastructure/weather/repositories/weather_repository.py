from sqlalchemy.orm import Session
from domain.weather.entities import Weather
from domain.weather.repositories import WeatherAbstractRepository

class SQLAlchemyWeatherRepository(WeatherAbstractRepository):
    """SqlAlchemy implementation of WeatherAbstractRepository"""

    def __init__(self, db_session: Session):
        print("Initializing SQLAlchemyWeatherRepository")
        self.session = db_session


    def add(self, weather: Weather) -> Weather | None:
        try:
            self.session.add(weather)
            self._session.flush()
            self._session.refresh(weather)
            return weather
        except Exception as error:
            print(error)
            return None


    def get(self, id: int) -> Weather | None:
        try:
            response = (
                self.session.query(Weather)
                .filter_by(id=id)
                .one()
            )
            return response
        except Exception:
            return None
