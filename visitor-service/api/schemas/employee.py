from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    job_position: str
    department_name: str
    phone_number: str
    email: str
    security_grade: int

    class Config:
        from_attributes = True