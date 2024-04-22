class Offer:
    def __init__(self, id:int, id_flight:int, discount:int, customer_type:str,flight_type:str):
        self.__id = id
        self.__id_flight = id_flight
        self.__discount = discount
        self.__customer_type = customer_type
        self.__flight_type = flight_type
                
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def id_flight(self):
        return self.__id_flight
    @id_flight.setter
    def id_flight(self, new_id_flight):
        self.__id_flight = new_id_flight
        
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount
        
    @property
    def customer_type(self):
        return self.__customer_type
    @customer_type.setter
    def customer_type(self, new_customer_type):
        self.__customer_type = new_customer_type
        
    @property
    def flight_type(self):
        return self.__flight_type
    @flight_type.setter
    def flight_type(self, new_flight_type):
        self.__flight_type = new_flight_type
        
    def __str__(self):
        return {"id": self.__id,
                "id_flight": self.__id_flight,
                "discount": self.__discount,
                "customer_type": self.__customer_type,
                "flight_type": self.__flight_type}
        