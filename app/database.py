from fastapi.applications import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_DATABASE_URL = "postgresql://postgres:9787565407Ss#@localhost/pro1"

ENGINE = create_engine(SQL_DATABASE_URL)

SESSION_LOCAL = sessionmaker(autocommit=False,autoflush=False,bind=ENGINE)

Base = declarative_base()


def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close