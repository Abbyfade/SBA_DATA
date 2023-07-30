#models for database [SQLAlchemy]
from sqlalchemy import Column, Integer, String, DateTime, Float, BigInteger
from app.db import Base

class TopGainers(Base):
    __tablename__ = "top_gainers"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(255))
    country = Column(String(255))
    number = Column(Integer)
    code = Column(String(255))
    opening_price = Column(Float)
    closing_price = Column(Float)
    percent_change = Column(Float)

class TopLosers(Base):
    __tablename__ = "top_losers"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(255))
    country = Column(String(255))
    number = Column(Integer)
    code = Column(String(255))
    opening_price = Column(Float)
    closing_price = Column(Float)
    percent_change = Column(Float)

class TopTraders(Base):
    __tablename__ = "top_traders"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(255))
    country = Column(String(255))
    number = Column(Integer)
    exchange_code = Column(String(255))
    opening_price = Column(Float)
    closing_price = Column(Float)
    volume = Column(BigInteger)

class Indices(Base):
    __tablename__ = "indices"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(255))
    country = Column(String(255))
    exchange_code = Column(String(255))
    previous_value = Column(Float)
    index_value = Column(Float)
    percent_change = Column(Float)