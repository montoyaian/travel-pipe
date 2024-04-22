from Classes.first_class import Firstclass
from Classes.standart_class import Standartclass
from Classes.supplier import Supplier
from datetime import date
import mysql.connector

DELETE_SUCCESS = {"message": "eliminacion completa"}



connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
cursor = connection.cursor()
class DatabaseControllerFlight():
    """
    This class is used to connect to the database and execute queries
    """

    def insert_flight(self, flight: Firstclass or Standartclass):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute(
        """SELECT * FROM appdb.supplier WHERE id = %s""",
        (flight.id_agency,),
        )
        result = cursor.fetchone()
        if result:
            if flight.positions > 0:
                if flight.date >= date.today():
                    if isinstance(flight, Firstclass):
                        cursor.execute(      """INSERT INTO  appdb.first_class(
                        Origin,
                        Destination,
                        Date,
                        Positions,
                        Hour,
                        Id_agency,
                        Premium_cost
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (
                        flight.origin,
                        flight.destination,
                        flight.date,
                        flight.positions,
                        flight.hour,
                        flight.id_agency,
                        flight.premium_cost,
                        ))
                        connection.commit()
                        
                        flightj = {
                        "origin": flight.origin,
                        "destination": flight.destination,
                        "date": flight.date,
                        "positions": flight.positions,
                        "hour": flight.hour,
                        "id_agency": flight.id_agency,
                        "premium_cost": flight.premium_cost
                        }
                        return flightj

            
                    elif isinstance(flight, Standartclass):
                        cursor.execute(      """INSERT INTO  appdb.standart_class(
                        Origin,
                        Destination,
                        Date,
                        Positions,
                        Hour,
                        Id_agency,
                        Standart_cost
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (
                        flight.origin,
                        flight.destination,
                        flight.date,
                        flight.positions,
                        flight.hour,
                        flight.id_agency,
                        flight.standart_cost,
                        ))
                        connection.commit()
                        
                        flightj = {
                        "origin": flight.origin,
                        "destination": flight.destination,
                        "date": flight.date,
                        "positions": flight.positions,
                        "hour": flight.hour,
                        "id_agency": flight.id_agency,
                        "standart_cost": flight.standart_cost
                        }
                        return flightj    
                else:
                    return{"error": "fecha no valida"}
            else:
                return{"error": "cantidad de puestos no aceptada"}
        else:
            return{"error":"proveedor no encontrado"}
   
    def insert_supplier(self, supplier:Supplier ):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO  appdb.supplier(
        Name,
        Contact,
        Description
        ) VALUES (%s,%s, %s)""",
        (
        supplier.name,
        supplier.contact,
        supplier.description,
        ))
        connection.commit()
        supplierj = {
        "name": supplier.name,
        "contact": supplier.contact,
        "Description": supplier.description,
        }

        return supplierj      


     
    def edit_supplier(self,supplier:Supplier ):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM appdb.supplier WHERE ID = %s""", (supplier.id,))
        result = cursor.fetchone()

        if not result :
            return {"error":"proveedor no encontrado"}

        cursor.execute("""UPDATE appdb.supplier SET 
        Name = %s,
        Contact = %s,
        Description = %s
        WHERE ID = %s""",
        (
        supplier.name,
        supplier.contact,
        supplier.description,
        supplier.id,
        ))
        connection.commit()
        supplierj = {
        "id": supplier.id,
        "name": supplier.name,
        "contact": supplier.contact,
        "Description": supplier.description,
        }
        return supplierj

    def edit_flight(self, flight:Standartclass or Firstclass):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        cursor.execute(
        """SELECT * FROM appdb.supplier WHERE id = %s""",
        (flight.id_agency,),
        )
        result = cursor.fetchone()
        if result:
            if isinstance(flight, Standartclass):
                cursor.execute(
                """SELECT * FROM appdb.standart_class WHERE id = %s""",
                (flight.id,),
                 )
                result = cursor.fetchone()
                if result:
                    if flight.positions > 0:
                        if flight.date >= date.today():
                            cursor.execute(
                                """UPDATE appdb.standart_class SET
                                Origin=%s,
                                Destination=%s,
                                Date= %s,
                                Positions=%s,
                                Hour=%s,
                                Id_agency=%s,
                                Standart_cost=%s
                                WHERE id = %s""",
                                (
                                    flight.origin,
                                    flight.destination,
                                    flight.date,
                                    flight.positions,
                                    flight.hour,
                                    flight.id_agency,
                                    flight.standart_cost,
                                    flight.id,
                                ),
                            )
                            connection.commit()
                            cursor.execute(
                            """SELECT * FROM appdb.standart_class WHERE id = %s""",
                            (flight.id,),
                            )
                            updated_flight = cursor.fetchone()

                            updated_flight_dict = {
                                "id": updated_flight[0], 
                                "origin": updated_flight[1],
                                "destination": updated_flight[2],
                                "date": updated_flight[3],
                                "positions": updated_flight[4],
                                "hour": updated_flight[5],
                                "id_agency": updated_flight[6],
                                "standart_cost": updated_flight[7]
                            }
                            
                            return updated_flight_dict
                        
                        else:
                            return{"error": "fecha no valida"}
                    else:
                        return{"error": "cantidad de puestos no aceptada"}
                else:
                    return{"error": "vuelo no encontrado"}
           
            elif isinstance(flight, Firstclass):
                cursor.execute(
                """SELECT * FROM appdb.first_class WHERE id = %s""",
                (flight.id,),
                )
                result = cursor.fetchone()
                if result:
                    if flight.positions > 0:
                        if flight.date >= date.today():
                            cursor.execute(
                                """UPDATE appdb.first_class SET
                                Origin=%s,
                                Destination=%s,
                                Date=%s,
                                Positions=%s,
                                Hour=%s,
                                Id_agency=%s,
                                premium_cost=%s
                                WHERE id = %s""",
                                (
                                flight.origin,
                                flight.destination,
                                flight.date,
                                flight.positions,
                                flight.hour,
                                flight.id_agency,
                                flight.premium_cost,
                                flight.id,
                                ),
                            )
                            connection.commit()
                            cursor.execute(
                            """SELECT * FROM appdb.first_class WHERE id = %s""",
                            (flight.id,),
                            )
                            updated_flight = cursor.fetchone()

                            updated_flight_dict = {
                                "id": updated_flight[0],  
                                "origin": updated_flight[1],
                                "destination": updated_flight[2],
                                "date": updated_flight[3],
                                "positions": updated_flight[4],
                                "hour": updated_flight[5],
                                "id_agency": updated_flight[6],
                                "premium_cost": updated_flight[7]
                            }
                            
                            return updated_flight_dict
                        else:
                            return{"error": "fecha no valida"}
                    else:
                        return{"error": "cantidad de puestos no aceptada"}
                else:
                    return{"error": "vuelo no encontrado"}
        else:
            return{"error": "proveedor no encontrado"}
                        
    def delete_flight(self, id: int, class_type: str):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        """
        Delete a flight from database
        """
        cursor = connection.cursor()
        class_type.lower()
        if (class_type == "first class"):
            cursor.execute(
            """SELECT * FROM appdb.first_class WHERE id = %s""",
            (id,),
            )
            result = cursor.fetchone()
            if result:
                cursor.execute("""DELETE FROM appdb.first_class WHERE id = %s""", (id,))
                cursor.execute("""DELETE FROM appdb.bookings WHERE Id_flight= %s AND Type_flight = 'first class'""", (id,))
                cursor.execute("""DELETE FROM appdb.Offers WHERE Id_flight = %s""", (id,))
                connection.commit()
                return DELETE_SUCCESS
            else:
                return{"error": "vuelo no encontrado"}            
        elif (class_type == "standart class"):
            cursor.execute(
            """SELECT * FROM appdb.standart_class WHERE id = %s""",
            (id,),
            )
            result = cursor.fetchone()
            if result:
                cursor.execute("""DELETE FROM appdb.standart_class WHERE id = %s""", (id,))
                cursor.execute("""DELETE FROM appdb.bookings WHERE Id_flight= %s AND Type_flight = 'standart class'""", (id,))
                cursor.execute("""DELETE FROM appdb.Offers WHERE Id_flight = %s""", (id,))
                connection.commit()
                
                return DELETE_SUCCESS
            else:
                return{"error": "vuelo no encontrado"} 
        else:
            return {"error":"tipo de vuelo no encontrado"}
    
    def delete_supplier(self, id:int):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        """
        Delete a supplier from database
        """
        cursor = connection.cursor()
        
        cursor.execute(
        """SELECT * FROM appdb.supplier WHERE id = %s""",
        (id,),
        )
        result = cursor.fetchone()
        if result:
            cursor.execute("""DELETE FROM appdb.supplier  WHERE id = %s""", (id,))      
            cursor.execute("""DELETE FROM appdb.first_class  WHERE ID_agency = %s""", (id,))
            cursor.execute("""DELETE FROM appdb.standart_class  WHERE ID_agency = %s""", (id,))
            connection.commit()
                      
            return DELETE_SUCCESS
        else:
            return {"error":"proveedor no encontrado"}        
            
    def show_flight(self, table_name:str,id:str ):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        try:
            if table_name == "all":
                cursor.execute('SELECT * FROM appdb.first_class')
                rows = cursor.fetchall()
                cursor.execute('SELECT * FROM appdb.standart_class')
                rows += cursor.fetchall()
                rowsj=[]
                for i in rows:
                    rowj ={
                    "id" : i[0],
                    "origin": i[1],
                    "destination": i[2],
                    "date": i[3],
                    "positions": i[4],
                    "hour": i[5],
                    "id_agency": i[6],
                    "cost": i[7]
                    }
                    rowsj.append(rowj)
    
                return rowsj
                
            else:
                if id == "all":
                    cursor.execute(
                        '''SELECT * FROM appdb.{}'''.format(table_name))
                    rows = cursor.fetchall()
                    rowsj=[]
                    for i in rows:
                        rowj ={
                        "id" : i[0],
                        "origin": i[1],
                        "destination": i[2],
                        "date": i[3],
                        "positions": i[4],
                        "hour": i[5],
                        "id_agency": i[6],
                        "cost": i[7]
                        }
                        rowsj.append(rowj)
    
                    return rowsj
                else:
                    cursor.execute(
                        '''SELECT * FROM appdb.{} WHERE id = {}'''.format(table_name, id))
                    rows = cursor.fetchall()
                    rowj ={
                    "id" :  rows[0][0],
                    "origin": rows[0][1],
                    "destination": rows[0][2],
                    "date":rows[0][3],
                    "positions": rows[0][4],
                    "hour": rows[0][5],
                    "id_agency": rows[0][6],
                    "cost": rows[0][7]
                    }
                    return rowj
        except:
            return{"message":"datos no encontrados"}

    def show_supplier(self,id:str):
        connection =mysql.connector.connect(user='sqladmin',password='Azure@123',host='appservermontoya.database.windows.net',database='appdb',port='1433')
        cursor = connection.cursor()
        if id == "all":
            cursor.execute(
            '''SELECT * FROM appdb.supplier''')
            rows = cursor.fetchall()
            rowsj=[]
            for i in rows:
                rowj ={
                "id" : i[0],
                "name": i[1],
                "contact": i[2],
                "Description": i[3],
                }
                rowsj.append(rowj)
  
            return rowsj
        else:
            try:
                id = int(id)
                cursor.execute(
                '''SELECT * FROM appdb.supplier WHERE id = %s''',(id,))
                rows = cursor.fetchall()
                rowj = {
                    "id": rows[0][0],
                    "name": rows[0][1],
                    "contact": rows[0][2],
                    "Description": rows[0][3]
                }
                return rowj
            except:
                {"message" : "datos no validos"}   
