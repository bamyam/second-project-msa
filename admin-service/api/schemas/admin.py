from pydantic import BaseModel
from datetime import datetime
from typing import Union

class Admin(BaseModel):
    id: int
    regdate: Union[str, datetime]
    company_name: str
    department_name: str
    job_position: str
    name: str
    phone_number: str
    department_name_1: str
    job_position_1: str
    name_1: str
    security_grade: int
    purpose: str
    location: str
    security_grade_1: int
    visit_date: str
    status: str
    cpg: int
    stpg: int
    allpage: int

    class Config:
        from_attributes = True
