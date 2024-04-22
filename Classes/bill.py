class Bill:
    def __init__(self, id:int, total_price:int, id_booking:int, payment_method:str):
        self.__id = id
        self.__total_price = total_price
        self.__id_booking = id_booking
        self.__payment_method = payment_method
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def total_price(self):
        return self.__total_price
    @total_price.setter
    def total_price(self, new_total_price):
        self.__total_price = new_total_price
        
    @property
    def id_booking(self):
        return self.__id_booking
    @id_booking.setter
    def id_booking(self, new_id_booking):
        self.__id_booking = new_id_booking
        
    @property
    def payment_method(self):
        return self.__payment_method
    @payment_method.setter
    def payment_method(self, new_payment_method):
        self.__payment_method = new_payment_method
        
    def __str__(self):
        return {"id": self.__id,
                "total_price": self.__total_price,
                "id_booking": self.__id_booking,
                "payment_method": self.__payment_method}