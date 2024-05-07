from pydantic import BaseModel

class Location(BaseModel):
    id: int
    location: str
    security_grade: int

    class Config:
        from_attributes = True