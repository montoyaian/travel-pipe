from datetime import date

class Flight:
    def __init__(self, id:int, origin:str, destination:str, date:date, positions:int, hour:float, id_agency:int):
        self.__id = id
        self.__origin = origin
        self.__destination = destination
        self.__date = date
        self.__positions = positions
        self.__hour = hour
        self.__id_agency = id_agency
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def origin(self):
        return self.__origin
    @origin.setter
    def origin(self, new_origin):
        self.__origin = new_origin
        
    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, new_destination):
        self.__destination = new_destination
        
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, new_date):
        self.__date = new_date
        
    @property
    def positions(self):
        return self.__positions
    @positions.setter
    def positions(self, new_positions):
        self.__positions = new_positions
        
    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, new_hour):
        self.__hour = new_hour
        
    @property
    def id_agency(self):
        return self.__id_agency
    @id_agency.setter
    def id_agency(self, new_id_agency):
        self.__id_agency = new_id_agency
        
    def __str__(self):
        return {"id": self.__id,
                "origin": self.__origin,
                "destination": self.__destination,
                "date": self.__date,
                "positions": self.__positions,
                "hour": self.__hour,
                "id_agency": self.__id_agency}