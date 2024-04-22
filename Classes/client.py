class Client:
    def __init__(self, id:int, name:str, contact:int, bookings:int,email:str,password:str):   
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__bookings = bookings
        self.__email = email 
        self.__password = password     
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        self.__id = new_id
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, new_contact):
        self.__contact = new_contact
        
    @property
    def bookings(self):
        return self.__bookings
    @bookings.setter
    def bookings(self, new_bookings):
        self.__bookings = new_bookings
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        self.__email = new_email
        
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        self.__password = new_password   
        
                     
    def __str__(self):
        return {"id": self.__id,
                "name": self.__name,
                "contact": self.__contact,
                "bookings": self.__bookings,
                "email": self.__email
                }