from typing import List, Optional
from pydantic import BaseModel, Field

class GainerCreate(BaseModel):
    date: str
    country: str
    number: int
    code: str
    opening_price: str
    closing_price: str
    percent_change: str

class LoserCreate(BaseModel):
    date: str
    country: str
    number: int
    code: str
    opening_price: str
    closing_price: str
    percent_change: str

class TraderCreate(BaseModel):
    date: str
    country: str
    number: int
    exchange_code: str
    opening_price: str
    closing_price: str
    volume: str

class IndexCreate(BaseModel):
    date: str
    country: str
    exchange_code: str
    previous_value: str
    index_value: str
    percent_change: str

class Gainer(GainerCreate):
    id: int

    class Config:
        orm_mode = True

class Loser(LoserCreate):
    id: int

    class Config:
        orm_mode = True

class Trader(TraderCreate):
    id: int

    class Config:
        orm_mode = True

class Index(IndexCreate):
    id: int

    class Config:
        orm_mode = True