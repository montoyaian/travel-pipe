from Classes.standart_client import Standardclient
from Classes.premium_client import PremiumClient
from fastapi import APIRouter, Depends, HTTPException
from controller.bd_controller_clients import DatabaseControllerClient
from models.standart_client_model import *
from models.premium_client_model import *
from models.client_model import *

bd_object_client = DatabaseControllerClient() 

client_router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)

@client_router.post("/add/standartclient")
async def add_standartclient(standart_client : Standart_clientmodel):
    """
    Add a standart client to database
    """
    return bd_object_client.insert_client(Standardclient(id =0, name=standart_client.name, contact= standart_client.contact,bookings = standart_client.bookings ,email= standart_client.email, password = standart_client.password))



@client_router.post("/add/premiumclient")
async def add_premiumclient(premium_client : Premium_clientmodel):
    """
    Add a premium client to database
    """
    return bd_object_client.insert_client(PremiumClient(id =0, name= premium_client.name, contact= premium_client.contact,bookings = premium_client.bookings ,email= premium_client.email,password = premium_client.password))

@client_router.put("/edit/standartclient/{client_id}")
def edit_client(client_id, standart_client : Standart_clientUpdateModel):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_client(Standardclient(id = client_id, name=standart_client.name, contact= standart_client.contact,bookings = standart_client.bookings ,email= standart_client.email,password = standart_client.password))

@client_router.put("/edit/premiumclient/{client_id}")
def edit_client(client_id, premium_client : Premium_clientmodel):
    """
    edit a premium client to database
    """ 
    return bd_object_client.edit_client(PremiumClient(id = client_id, name=premium_client.name, contact= premium_client.contact,bookings = premium_client.bookings ,email= premium_client.email,password = premium_client.password))

@client_router.delete("/delete/client/{id}/{client_type}")
def delete_client(id:int = 1 , client_type:str = "client type"):
    """
    delete a client to database
    """ 
    return bd_object_client.delete_client(id= id, client_type=client_type)

@client_router.get("/get/clients/{id}/{table_name}")
def show_client(id:str = "all or id", table_name:str = "standart_client or premium_client"):
    """
     show clients
    """ 
    return bd_object_client.show_client(id=id,table_name=table_name)

@client_router.get("/get/premiumclient")
def show_premiumclient():
    """
    show premiums clients
    """ 
    return bd_object_client.premium_clients()