from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 아이디
    name = Column(String(20), nullable=False)                   # 이름
    job_position = Column(String(50), nullable=False)           # 직급
    department_name = Column(String(50), nullable=False)        # 부서명
    phone_number = Column(String(13), nullable=False)           # 전화번호
    email = Column(String(150), nullable=False)                 # 이메일
    security_grade = Column(Integer, nullable=False)            # 보안등급(1,2,3) 3등급이 가장 낮은 등급

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)      # PK
    location = Column(String(100), nullable=False)                  # 이름
    security_grade = Column(Integer, nullable=False)                # 보안등급(1,2,3) 3등급이 가장 낮은 등급

class Visitors(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 번호
    name = Column(String(20), nullable=True)                    # 방문객 이름
    company_name = Column(String(100), nullable=False)          # 회사 이름
    email = Column(String(150), nullable=False)                 # 이메일
    department_name = Column(String(50), nullable=False)        # 부서명
    job_position = Column(String(50), nullable=False)           # 직급
    phone_number = Column(String(13), nullable=False)           # 전화번호
    employee_id = mapped_column(Integer, ForeignKey('employee.id'))    # 담당자 이름
    purpose = Column(String(500), nullable=False)               # 방문 목적
    location_id = mapped_column(Integer, ForeignKey('location.id'))  # 방문 장소
    status = Column(String(1), default='N')     # 승인 상태(Y: 승인, N: 접수, R: 거절)
    regdate = Column(DateTime, default=datetime.now(), nullable=True)     # 신청일
    visit_date = Column(String(10), nullable=True)   # 방문날짜

