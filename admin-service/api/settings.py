from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    userid: str = os.getenv('userid')
    passwd: str = os.getenv('passwd')
    dbname: str = os.getenv('dbname')
    dbhost: str = os.getenv('dbhost')

    db_conn: str = f'mysql+pymysql://{userid}:{passwd}@{dbhost}:3306/{dbname}'
    #db_conn = f'mysql+pymysql://{userid}:{passwd}'
    #db_conn = f'oracle+cx_oracle://'

    # class Config:
    #     env_file = '.env'

config = Settings()