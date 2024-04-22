from Classes.offers import Offer
from controller.bd_controller_clients import DatabaseControllerClient
from models.offers_model import *
from fastapi import APIRouter, Depends, HTTPException

bd_object_client = DatabaseControllerClient() 

offers_router = APIRouter(
    prefix="/offers",
    tags=["Offers"],
)

@offers_router.post("/add/offers")
async def add_offers(offer:offermodel):
    """
    Add a offer to database
    """
    return bd_object_client.insert_offer(Offer(id=id, id_flight=offer.id_flight, discount=offer.discount, customer_type=offer.customer_type, flight_type=offer.flight_type))


@offers_router.put("/edit/offer/{offer_id}")
def edit_offer(offer_id, offer: offerUpdateModel):
    """
    edit offer to database
    """ 
    return bd_object_client.edit_offer(Offer(id= offer_id,id_flight=offer.id_flight, discount=offer.discount, customer_type=offer.customer_type,flight_type=offer.flight_type))

@offers_router.delete("/delete/offer/{id}")
def delete_offer(id:int = 1 ):
    """
    delete a offer to database
    """ 
    return bd_object_client.delete_offer(id= id)

@offers_router.get("/get/offers/{id}")
def show_offers(id:str = "all or id"):
    """
    show offers
    """ 
    return bd_object_client.show_offer(id=id)