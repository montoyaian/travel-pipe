from models.client_model import *


class Standart_clientmodel (ClientModel):

    class Config:
        from_attributes = True


class Standart_clientUpdateModel (ClientModel):
    
    class Config:
        from_attributes = True