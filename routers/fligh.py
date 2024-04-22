from Classes.first_class import Firstclass
from Classes.standart_class import Standartclass
from controller.bd_controller_flight import DatabaseControllerFlight
from fastapi import APIRouter, Depends, HTTPException
from models.standart_class_model import *
from models.first_class_model import *

bd_object_flights = DatabaseControllerFlight() 

flight_router = APIRouter(
    prefix="/flight",
    tags=["Flight"],
)

@flight_router.post("/add/Firstclass")
async def add_Firstclass(First_class :  First_flight_model):
    """
    Add a Firstclass to database
    """
    return bd_object_flights.insert_flight(Firstclass(id=0,origin =First_class.origin, destination=First_class.destination, date= First_class.date, 
                                            positions=First_class.positions, hour=First_class.hour, id_agency=First_class.id_agency, premium_cost=First_class.premium_cost))

@flight_router.post("/add/standartclass")
async def add_standartclass(standart_class : Standart_flight_model):
    """
    Add a standart class to database
    """
    return bd_object_flights.insert_flight(Standartclass(id=0,origin =standart_class.origin, destination=standart_class.destination, date= standart_class.date, 
                                            positions=standart_class.positions, hour=standart_class.hour, id_agency=standart_class.id_agency, standart_cost=standart_class.standart_cost))

@flight_router.put("/edit/Firstclass/{flight_id}")
def edit_flight(flight_id,First_class : fly_First_UpdateModel):
    """
    edit a Firstclass to database
    """ 
    return bd_object_flights.edit_flight(Firstclass(id= flight_id,origin=First_class.origin, destination= First_class.destination, date = First_class.date, positions=First_class.positions, hour=First_class.hour, 
                                                       id_agency=First_class.id_agency, premium_cost=First_class.premium_cost))


@flight_router.put("/edit/standartclass/{flight_id}")
def edit_flight(flight_id, standart_class : fly_standart_UpdateModel):
    """
    edit a standartclass to database
    """ 
    return bd_object_flights.edit_flight(Standartclass(id= flight_id,origin=standart_class.origin, destination= standart_class.destination, date = standart_class.date, positions=standart_class.positions, hour=standart_class.hour, 
                                                       id_agency=standart_class.id_agency, standart_cost=standart_class.standart_cost))

@flight_router.delete("/delete/flight/{id}/{class_type}")
def delete_flight(id:int = 1 , class_type:str = "flght type"):
    """
    delete a standartclass to database
    """ 
    return bd_object_flights.delete_flight(id= id, class_type=class_type)

@flight_router.get("/get/flights/{id}/{table_name}")
def show_flight(id:str = "all or id",table_name:str = "standart_class or First_class"):
    """
    show flights
    """ 
    return bd_object_flights.show_flight(id=id, table_name=table_name)