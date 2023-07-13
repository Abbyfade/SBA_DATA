# connection to database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sbatest.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Abiola@localhost:5432/sba_data"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL#, connect_args = {"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()
