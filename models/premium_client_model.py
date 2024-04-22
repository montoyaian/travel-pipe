from models.client_model import *


class Premium_clientmodel (ClientModel):

    class Config:
        from_attributes = True


class Premium_clientUpdateModel (ClientModel):   
    
    class Config:
        from_attributes = True