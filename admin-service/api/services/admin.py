from sqlalchemy import update, select, func

from api.database import SessionLocal
from api.models.visitors import Location,Employee,Visitors




class AdminService:
    @staticmethod
    def select_visit(cpg):
        stnum = (cpg - 1) * 15
        with SessionLocal() as sess:
            cnt = sess.query(func.count(Visitors.id)).scalar()
            stmt = select(Visitors.id, Visitors.regdate, Visitors.company_name, Visitors.department_name, Visitors.job_position,
                          Visitors.name, Visitors.phone_number, Employee.department_name, Employee.job_position, Employee.name,
                          Employee.security_grade, Visitors.purpose, Location.location, Location.security_grade, Visitors.visit_date, Visitors.status)\
            .join_from(Visitors, Employee)\
            .join_from(Visitors, Location)\
            .order_by(Visitors.id.desc()).offset(stnum).limit(15)
            result = sess.execute(stmt)

        return result, cnt

    @staticmethod
    def accept_visit(number):
        with SessionLocal() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='Y')
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def reject_visit(number):
        with SessionLocal() as sess:
            stmt = update(Visitors).where(Visitors.id == number).values(status='R')
            result = sess.execute(stmt)
            sess.commit()

        return result
