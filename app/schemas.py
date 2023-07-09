from typing import List
from pydantic import BaseModel

class TopGainers(BaseModel):
    date: str
    code: str
    opening_price: float
    closing_price: float
    volume: float
    percent_change: float

class TopGainerCreate(BaseModel):
    date: str
    country: str
    code: str
    opening_price: float
    closing_price: float
    volume: float
    percent_change: float

class TopLosers(BaseModel):
    date: str
    code: str
    opening_price: float
    closing_price: float
    volume: float
    percent_change: float

class TopTraders(BaseModel):
    date: str
    exchange_code: str
    previous_value: float
    index_value: float
    percent_change: float