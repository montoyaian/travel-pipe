from models.flight_model import *
from typing import Optional

class Standart_flight_model (FlightModel):
    standart_cost :  Optional[float]
    class Config:
        from_attributes = True


class fly_standart_UpdateModel (Standart_flight_model):
    class Config:
        from_attributes = True