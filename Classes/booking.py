class Booking:
    def __init__(self, id:int, cant_positions:int, id_flight:int, id_client:int,
                 type_client:str,type_flight:str,cost_position:float):
        self.__id = id
        self.__cant_positions = cant_positions
        self.__id_flight = id_flight
        self.__id_client = id_client
        self.__type_client = type_client
        self.__type_flight = type_flight
        self.__cost_position = cost_position
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def cant_positions(self):
        return self.__cant_positions
    @cant_positions.setter
    def cant_positions(self, new_cant_positions):
        self.__cant_positions = new_cant_positions
        
    @property
    def id_flight(self):
        return self.__id_flight
    @id_flight.setter
    def id_flight(self, new_id_flight):
        self.__id_flight = new_id_flight
        
    @property
    def id_client(self):
        return self.__id_client
    @id_client.setter
    def id_client(self, new_id_client):
        self.__id_client = new_id_client
        
    @property
    def type_flight(self):
        return self.__type_flight
    @type_flight.setter
    def type_flight(self, new_type_flight):
        self.__type_flight = new_type_flight
        
    @property
    def type_client(self):
        return self.__type_client
    @type_client.setter
    def type_client(self, new_type_client):
        self.__type_client = new_type_client   

    @property
    def cost_position(self):
        return self.__cost_position
    
    @cost_position.setter
    def cost_position(self, new_cost_position):
        self.new_cost_position = new_cost_position   
          
    def __str__(self):
        return {"id": self.__id,
                "cant_positions": self.__cant_positions,
                "id_flight": self.__id_flight,
                "id_client": self.__id_client,
                "type_flight": self.__type_flight,
                "type_client": self.__type_client,
                "cost_position":self.__cost_position}
