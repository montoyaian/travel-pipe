class Supplier:
    def __init__(self, id:int, name:str, contact:int, description:str):
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__description = description
        
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
    def description(self):
        return self.__description
    @description.setter
    def description(self, new_description):
        self.__description = new_description
        
    def __str__(self):
        return {"id": self.__id,
                "name": self.__name,
                "contact": self.__contact,
                "description": self.__description}
