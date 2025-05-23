from .config import environment as env

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://{env.database_username}:{env.database_password}@{env.database_hostname}:{env.database_port}/{env.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def getDB():
    db = session()
    try: yield db
    finally: db.close()