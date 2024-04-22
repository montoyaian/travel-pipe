from Classes.booking import Booking
from models.booking_model import * 
from controller.db_controller_bookings import DatabaseControllerBokings
from fastapi import APIRouter, Depends, HTTPException

bd_object_booking = DatabaseControllerBokings() 

bookings_router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@bookings_router.post("/add/booking")
def add_booking(booking : Bookingmodel):
    """
    add  booking to database
    """ 
    return bd_object_booking.insert_booking(Booking(id=1, cant_positions=booking.cant_positions, id_flight=booking.id_flight, id_client=booking.id_client,
                                            type_client=booking.type_client, type_flight=booking.type_flight, cost_position=0))


@bookings_router.put("/edit/booking/{booking_id}")
def edit_booking(booking_id, booking: BookingUpdateModel):
    """
    edit a booking to database
    """ 
    return bd_object_booking.edit_booking(booking.cant_positions, booking_id)


@bookings_router.delete("/delete/booking/{id}")
def delete_booking(id:int = 1):
    """
    delete  bookings to database
    """ 
    return bd_object_booking.delete_booking(id= id)

@bookings_router.get("/get/bookings/{id}")
def show_bookings(id:str = "all or id"):
    """
    show bookings
    """ 
    return bd_object_booking.show_booking(id=id)

@bookings_router.get("/get/bill")
def show_bill(id_booking:int = 1,payment_method:str = "payment_method"):
    """
    show bill
    """ 
    return bd_object_booking.show_bill(id_booking=id_booking,payment_method=payment_method)

