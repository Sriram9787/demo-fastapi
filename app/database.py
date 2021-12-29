from fastapi.applications import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQL_DATABASE_URL = "postgres://lenormoxtlobjq:3131d0dc2a85a9295585e5c4db4fc35cdc3d1cb3819b798d795ce9043fd8e3bc@ec2-44-198-211-34.compute-1.amazonaws.com:5432/d7hviodhvs8eg9"

ENGINE = create_engine(SQL_DATABASE_URL)

SESSION_LOCAL = sessionmaker(autocommit=False,autoflush=False,bind=ENGINE)

Base = declarative_base()


def get_db():
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close