import sqlalchemy
from sqlalchemy.orm import sessionmaker


from api.models import visitors


db_url = 'sqlite:///admin.db'

engine = sqlalchemy.create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)

def create_tables():
    visitors.Base.metadata.create_all(engine)

def get_db():
    with SessionLocal() as db:
        yield db