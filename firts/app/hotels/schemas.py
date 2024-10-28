from datetime import date
from fastapi import Query
from pydantic import BaseModel, Field
from typing import Optional

class SHotel(BaseModel):
    id: int
    name: str
    location: str
    stars: Optional[int]



class HotelSearchArgs(BaseModel):
    location: str
    date_from: date
    date_to: date
    stars: Optional[int] = Field(None, ge=1, le=7)
    spa: Optional[bool] = None