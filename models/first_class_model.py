from models.flight_model import *
from typing import Optional

class First_flight_model (FlightModel):
    premium_cost : Optional[float]
    class Config:
        from_attributes = True


class fly_First_UpdateModel (First_flight_model ):
    class Config:
        from_attributes = True