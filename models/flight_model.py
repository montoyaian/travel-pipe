from typing import Optional
from datetime import date
from pydantic import BaseModel


class FlightModel (BaseModel):
    origin: Optional[str]
    destination: Optional[str]
    date: Optional[date]
    positions: Optional[int]
    hour: Optional[float]
    id_agency: Optional[int]

    