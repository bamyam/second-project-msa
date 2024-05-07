from sqlalchemy.orm import Session
from sqlalchemy import select
from api.models.location import Location
from api.database import Session


class LocationService:

    @staticmethod
    def get_all_location():
        """
        데이터베이스에서 모든 장소 정보를 조회하여 반환합니다.

        Returns:
            List[Location]: 조회된 장소 정보 목록
        """
        with Session() as session:
            statement = select(Location.id, Location.location, Location.security_grade)
            result = session.execute(statement).fetchall()
            return result