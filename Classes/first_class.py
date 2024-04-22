from Classes.flight import Flight
from datetime import date

class Firstclass(Flight):
    def __init__(self, id:int, origin:str, destination:str, date:date, positions:int, hour:int, id_agency:int, premium_cost:float):
        super().__init__(id, origin, destination, date, positions, hour, id_agency)
        self.premium_cost = premium_cost
        
    @property
    def premium_flight(self):
        return self.__premium_cost
    @premium_flight.setter
    def premium_flight(self, new_premium_cost):
        self.__premium_cost = new_premium_cost
        
    def __str__(self):
        return {"id": self.id,
                "origin": self.origin,
                "destination": self.destination,
                "date": self.date,
                "positions": self.positions,
                "hour": self.hour,
                "id_agency": self.id_agency,
                "premium_cost": self.premium_cost}
