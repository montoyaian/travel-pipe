from Classes.bill import Bill
from Classes.booking import Booking
import mysql.connector

DELETE_SUCCESS = {"message": "eliminacion completa"}

connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
cursor = connection.cursor()
class DatabaseControllerBokings():

    """
    This class is used to connect to the database and execute queries
    """
    def insert_booking(self, booking: Booking):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        if booking.type_flight =="standart class":
            cursor.execute("""SELECT * FROM appdb.standart_class WHERE ID= %s""", (booking.id_flight,))
            flight = cursor.fetchone()
            if flight and flight[4]>=booking.cant_positions:
                if booking.type_client == "standart client":
                    cursor.execute("""SELECT * FROM appdb.Offers WHERE Id_flight= %s AND 
                    Customer_type = 'standart client'""", (booking.id_flight,))
                    offer = cursor.fetchone()
                    if not offer:
                        discount = 0.0 
                    else:
                        discount = float(offer[2])
                    cursor.execute("""SELECT * FROM appdb.standart_client WHERE ID= %s""", (booking.id_client,))
                    client = cursor.fetchone()
                    if client:                      
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        cursor.execute(
                        """UPDATE appdb.standart_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        connection.commit()
                        client_new_bookings = client[3] + 1 
                        cursor.execute(
                        """UPDATE appdb.standart_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        connection.commit()
                        new_cost_position = price_position - (price_position * discount/100)
                        cursor.execute('''INSERT INTO appdb.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))
                        connection.commit()
                        if discount == 0:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            }     
                        else:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            "offer" : offer[0],
                            "discount" : discount
                            }  
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                    
                elif booking.type_client == "premium client":
                    cursor.execute("""SELECT * FROM appdb.Offers WHERE Id_flight= %s AND 
                                Customer_type = 'premium client'""", (booking.id_flight,))
                    offer = cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    cursor.execute("""SELECT * FROM appdb.premium_client WHERE ID= %s""", (booking.id_client,))
                    client = cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        cursor.execute(
                        """UPDATE appdb.standart_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        connection.commit()
                        client_new_bookings =client[3]+ 1
                        cursor.execute(
                        """UPDATE appdb.premium_client SET
                        bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        cursor.execute('''INSERT INTO appdb.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        )) 
                        connection.commit()  
                        if discount == 0:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            }     
                        else:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            "offer" : offer[0],
                            "discount" : discount
                            } 
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                else:
                    return{"error":"tipo de cliente no encontrado"}               
            else:
                return{"error":"vuelo no disponible"} 
              
        elif(booking.type_flight =="first class"):
            cursor.execute("""SELECT * FROM appdb.first_class WHERE ID= %s""", (booking.id_flight,))
            flight = cursor.fetchone()
            if flight and flight[4]>=booking.cant_positions:
                if booking.type_client == "standart client":
                    cursor.execute("""SELECT * FROM appdb.Offers WHERE Id_flight= %s AND 
                    Customer_type = 'standart client'""", (booking.id_flight,))
                    offer = cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    cursor.execute("""SELECT * FROM appdb.standart_client WHERE ID= %s""", (booking.id_client,))
                    client = cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions= flight[4] - booking.cant_positions
                        cursor.execute(
                        """UPDATE appdb.first_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        connection.commit()
                        client_new_bookings = client[3] + 1
                        cursor.execute(
                        """UPDATE appdb.standart_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        cursor.execute('''INSERT INTO appdb.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))   
                        connection.commit()
                        if discount == 0:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            }     
                        else:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            "offer" : offer[0],
                            "discount" : discount
                            }       
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                    
                elif booking.type_client == "premium client":
                    cursor.execute("""SELECT * FROM appdb.Offers WHERE Id_flight= %s AND 
                                Customer_type = 'premium client'""", (booking.id_flight,))
                    offer = cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    cursor.execute("""SELECT * FROM appdb.premium_client WHERE ID= %s""", (booking.id_client,))
                    client = cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        cursor.execute(
                        """UPDATE appdb.first_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        connection.commit()
                        client_new_bookings= client[3] + 1
                        cursor.execute(
                        """UPDATE appdb.premium_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        cursor.execute('''INSERT INTO appdb.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))
                        connection.commit()                        
                        if discount == 0:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            }     
                        else:
                            bookingj = {
                            "cant_position":booking.cant_positions,
                            "Id_flight": booking.id_flight,
                            "Id_client": booking.id_client,
                            "Type_flight": booking.type_flight,
                            "Type_client": booking.type_client,
                            "Cost_position": new_cost_position,
                            "offer" : offer[0],
                            "discount" : discount
                            }  
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                else:
                    return{"error":"tipo de cliente no encontrado"}               
            else:
                return{"error":"vuelo no disponible"} 
        else:
            return{"error":"tipo de vuelo no encontrado"}
          
    def edit_booking(self, cant_position:int, id_booking:int):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM appdb.bookings WHERE ID= %s""", (id_booking,))
        booking = cursor.fetchone()
        if booking:
            if booking[4] == "standart class":
                cursor.execute("""SELECT * FROM appdb.standart_class  WHERE ID= %s""", (booking[2],))
                flight = cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                if flight_old_position > cant_position:
                    flight_new_position = flight_old_position - cant_position
                    cursor.execute(
                    """UPDATE appdb.standart_class SET
                    Positions=%s
                    WHERE id = %s""",
                    (
                    flight_new_position,
                    flight[0],
                    ),
                    )
                    print(cant_position)
                    connection.commit()
                    cursor.execute(
                    """UPDATE appdb.bookings SET
                    Cant_positions=%s
                    WHERE id = %s""",
                    (
                    cant_position,
                    booking[0],
                    ),
                    )
                    connection.commit()
                    bookingj = {
                    "Cant_position": cant_position,
                    "Id_flight": booking[2],
                    "Id_client": booking[3],
                    "Type_flight": booking[4],
                    "Type_client": booking[5],
                    "Cost_position": booking[6]
                    }  
                    return bookingj
                else:
                    return {"error": "cantidad de puestos no disponibles" }
            else:
                cursor.execute("""SELECT * FROM appdb.first_class  WHERE ID= %s""", (booking[2],))
                flight = cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                if flight_old_position > cant_position:
                    flight_new_position = flight_old_position - cant_position
                    cursor.execute(
                    """UPDATE appdb.first_class SET
                    Positions=%s
                    WHERE id = %s""",
                    (
                    flight_new_position,
                    flight[0],
                    ),
                    )
                    connection.commit()
                    cursor.execute(
                    """UPDATE appdb.bookings SET
                    Cant_positions=%s
                    WHERE id = %s""",
                    (
                    cant_position,
                    booking[0],
                    ),
                    )
                    connection.commit()
                    bookingj = {
                    "Cant_position": cant_position,
                    "Id_flight": booking[2],
                    "Id_client": booking[3],
                    "Type_flight": booking[4],
                    "Type_client": booking[5],
                    "Cost_position": booking[6]
                    }  
                    return bookingj
                else:
                    return {"error": "cantidad de puestos no disponibles" }
        else:
            return{"error":"reserva no encontrada"}
    
    def delete_booking(self, id:int):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM appdb.bookings WHERE ID= %s""", (id,))
        booking = cursor.fetchone()
        if booking:
            if booking[4] == "standart class":
                cursor.execute("""SELECT * FROM appdb.standart_class WHERE ID= %s""", (booking[2],))
                flight = cursor.fetchone()
                flight_new_position = flight[4] + booking[1]
                cursor.execute(
                """UPDATE appdb.standart_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                connection.commit()
                if booking[5] == "standart client":
                    cursor.execute("""SELECT * FROM appdb.standart_client WHERE ID= %s""", (booking[3],))
                    client = cursor.fetchone()
                    client_new_booking = client[3] - 1
                    cursor.execute(
                    """UPDATE appdb.standart_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    connection.commit()
                else:
                    cursor.execute("""SELECT * FROM appdb.premium_client WHERE ID= %s""", (booking[3],))
                    client = cursor.fetchone()
                    client_new_booking = client[3] - 1
                    cursor.execute(
                    """UPDATE appdb.premium_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    connection.commit()
            else:
                cursor.execute("""SELECT * FROM appdb.first_class WHERE ID= %s""", (booking[2],))
                flight = cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                flight_new_position = flight_old_position - booking[1]
                cursor.execute(
                """UPDATE appdb.first_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                connection.commit()
                cursor.execute(
                """UPDATE appdb.first_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                connection.commit()
                if booking[5] == "standart client":
                    cursor.execute("""SELECT * FROM appdb.standart_client WHERE ID= %s""", (booking[3],))
                    client = cursor.fetchone()
                    client_new_booking = client[3] - 1
                    cursor.execute(
                    """UPDATE appdb.standart_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    connection.commit()
                else:
                    cursor.execute("""SELECT * FROM appdb.premium_client WHERE ID= %s""", (booking[3],))
                    client = cursor.fetchone()
                    client_new_booking = client[3] - 1
                    cursor.execute(
                    """UPDATE appdb.premium_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    connection.commit()
                
            cursor.execute("""DELETE FROM appdb.bookings WHERE ID= %s""", (id,))
            connection.commit()
            return DELETE_SUCCESS
        else:
            return{"error":"reserva no encontrada"}
                    
    def show_booking(self,id:str):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        if id == "all":
            cursor.execute(
            '''SELECT * FROM appdb.bookings''')
            rows = cursor.fetchall()
            rowsj=[]
            for i in rows:
                rowj ={
                "id": i[0],
                "Cant_position": i[1],
                "Id_flight":i[2] ,
                "Id_client": i[3],
                "Type_flight": i[4],
                "Type_client": i[5],
                "Cost_position":i[6]
                }  
                rowsj.append(rowj)
    
            return rowsj
        else:
            try:
                cursor.execute(
                '''SELECT * FROM appdb.bookings WHERE id = {}'''.format(id))
                rows = cursor.fetchall()
                rowj ={
                "id" : rows[0][0],
                "Cant_position": rows[0][1],
                "Id_flight":rows[0][2] ,
                "Id_client": rows[0][3],
                "Type_flight": rows[0][4],
                "Type_client": rows[0][5],
                "Cost_position":rows[0][6]
                }  
                return rowj
            except:
                return{"message" : "datos no validos"}
    
    def show_bill(self, id_booking:int, payment_method:str):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM appdb.bookings WHERE ID= %s""", (id_booking,))
        booking = cursor.fetchone() 

        if booking:
            total_cost = booking[6] * booking[1]
            bill = Bill(id_booking, total_cost, id_booking, payment_method)
            billj = {
            "id": bill.id,
            "total_price": bill.total_price,
            "id_booking": bill.id_booking,
            "payment_method": bill.payment_method,
            "cant_positions" : booking[1],
            "id_flight" : booking[2],
            "type_flight" : booking[4]
            }
            return  billj
        else:
            return {"error": "Reserva no encontrada"}
