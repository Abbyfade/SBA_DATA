from typing import List
from pydantic import BaseModel, condecimal
from datetime import date

class TopGainers(BaseModel):
    id: int
    date: date
    country: str
    number: int
    code: str
    opening_price: float
    closing_price: float
    percent_change: condecimal(decimal_places=2, ge=0)

class TopLosers(BaseModel):
    id: int
    date: str
    country: str
    number: int
    code: str
    opening_price: float
    closing_price: float
    percent_change: condecimal(decimal_places=2, ge=0)

class TopTraders(BaseModel):
    date: str
    country: str
    number: int
    exchange_code: str
    opening_price: float
    closing_price: float
    volume: int

class Indices(BaseModel):
    date: str
    country: str
    exchange_code: str
    previous_value: float
    index_value: float
    percent_change: condecimal(decimal_places=2, ge=0)