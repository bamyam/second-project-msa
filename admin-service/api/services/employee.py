from sqlalchemy.orm import Session
from sqlalchemy import select
from api.models.visitors import Employee
from api.database import SessionLocal


class EmployeeService:

    @staticmethod
    def get_all_employees():
        """
        데이터베이스에서 모든 직원 정보를 조회하여 반환합니다.

        Returns:
            List[Employee]: 조회된 직원 정보 목록
        """
        with SessionLocal() as session:
            statement = select(Employee.id, Employee.name, Employee.job_position, Employee.department_name, Employee.phone_number, Employee.email, Employee.security_grade)
            result = session.execute(statement).fetchall()
            return result