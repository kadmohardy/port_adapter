# somewhere in the domain layer
import abc
from sqlalchemy.orm import Session
from domain.weather.entities import Weather
from domain.weather.repositories import WeatherAbstractRepository

class SQLAlchemyWeatherRepository(WeatherAbstractRepository):
    """SqlAlchemy implementation of WeatherAbstractRepository"""

    def __init__(self, db_session: Session):
        self._session = db_session


    def add(self, weather: Weather) -> Weather | None:
        try:
            self._session.add(weather)
            self._session.commit()
            return weather
        except Exception:
            return None


    def get_by_id(self, id: int) -> Weather | None:
        try:
            response = (
                self._session.query(Weather)
                .filter_by(id=id)
                .one()
            )
            return response
        except Exception:
            return None
