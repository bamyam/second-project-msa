from api.models.visitors import Visitors
from api.models.visitors import Location

from sqlalchemy import insert, select, and_
from api.database import SessionLocal


class VisitorsService:

    @staticmethod
    def insert_visitor(vmdto):
        data = VisitorsService.visitor_convert(vmdto)
        with SessionLocal() as sess:
            stmt = insert(Visitors).values(data)
            result = sess.execute(stmt)
            sess.commit()

             # sess.query(Visitors.id).filter_by(name=data['name']).scalar()

            return result


    @staticmethod
    def visitor_convert(vmdto):
        data = vmdto.model_dump()
        mb = Visitors(**data)
        data = {
            'name': mb.name,
            'company_name': mb.company_name,
            'email': mb.email,
            'department_name': mb.department_name,
            'job_position': mb.job_position,
            'phone_number': mb.phone_number,
            'employee_id': mb.employee_id,
            'purpose': mb.purpose,
            'location_id': mb.location_id,
            'visit_date': mb.visit_date
        }

        return data

    @staticmethod
    def search_visitor(name, phone_number):
        with SessionLocal() as sess:
            # name과 phone_number를 모두 만족하는 방문객 정보 조회
            stmt = select(Visitors.name,Visitors.phone_number,Visitors.email,Visitors.company_name
                          ,Visitors.job_position,Visitors.department_name,Location.location
                          ,Visitors.purpose,Visitors.visit_date,Visitors.status)\
                .join(Location)\
                .where(and_(Visitors.name == name, Visitors.phone_number == phone_number))

            result = sess.execute(stmt).fetchall()

        return result


