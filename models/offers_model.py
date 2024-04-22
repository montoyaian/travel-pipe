from typing import Optional

from pydantic import BaseModel


class offermodel (BaseModel):
    id_flight:Optional[int]
    discount:Optional[int]
    customer_type:Optional[str]
    flight_type:Optional[str]    
    class Config:
        from_attributes = True


class offerUpdateModel (offermodel):

    class Config:
        from_attributes = True