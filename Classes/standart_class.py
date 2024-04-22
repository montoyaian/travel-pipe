from Classes.flight import Flight
from datetime import date

class Standartclass(Flight):
    def __init__(self, id:int, origin:str, destination:str, date:date, positions:int, hour:int, id_agency:int, standart_cost:float):
        super().__init__(id, origin, destination, date, positions, hour, id_agency)
        self.__standart_cost = standart_cost
        
    @property
    def standart_cost(self):
        return self.__standart_cost
    @standart_cost.setter
    def standart_cost(self, new_standart_cost):
        self.__standart_cost = new_standart_cost
        
    def __str__(self):
        return {"id": self.id,
                "origin": self.origin,
                "destination": self.destination,
                "date": self.date,
                "positions": self.positions,
                "hour": self.hour,
                "id_agency": self.id_agency,
                "standart_cost": self.__standart_cost}