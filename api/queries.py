####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

import json

from app import app, mysql


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para guardar la informacion del archivo CSV en la base de datos
def store_csv_data(date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia_cdmx):

    saved = None

    try:
        with app.app_context():
             cursor = mysql.connection.cursor()
             data_insert = 'INSERT INTO ubica_vehicle (date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia_cdmx) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
             values = (date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia_cdmx)
             cursor.execute(data_insert, values)
             mysql.connection.commit()
             cursor.close()

        saved = True
    
    except:
        saved = False

    return saved

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para obtener toda la informacion de los vehiculos
def get_all_data():

    all_buses = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT ubica_vehicle.id, ubica_vehicle.date_updated, ubica_vehicle.vehicle_id, ubica_vehicle.vehicle_label, ubica_vehicle.vehicle_current_status, ubica_vehicle.position_latitude, ubica_vehicle.position_longitude, ubica_vehicle.geographic_point, ubica_vehicle.position_speed, ubica_vehicle.position_odometer, ubica_vehicle.trip_schedule_relationship, ubica_vehicle.trip_id, ubica_vehicle.trip_start_date, ubica_vehicle.trip_route_id FROM ubica_vehicle'
        cursor.execute(query_bus)
        all_buses = cursor.fetchall()
        cursor.close()
   
    except:
        all_buses = None

    return all_buses

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para obtener los vehiculos disponibles
def get_available_vehicles():

    all_buses = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT ubica_vehicle.vehicle_id, ubica_vehicle.vehicle_label, ubica_vehicle.vehicle_current_status FROM ubica_vehicle'
        cursor.execute(query_bus)
        all_buses = list(cursor.fetchall())
        cursor.close()
   
    except:
        all_buses = None

    return all_buses

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para obtener el vehiculo por el id
def get_vehicle_by_id():

    one_bus = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT ubica_vehicle.vehicle_id, ubica_vehicle.position_latitude, ubica_vehicle.position_longitude, ubica_vehicle.geographic_point, ubica_vehicle.position_speed, ubica_vehicle.position_odometer, ubica_vehicle.trip_schedule_relationship, ubica_vehicle.trip_id, ubica_vehicle.trip_start_date, ubica_vehicle.trip_route_id FROM ubica_vehicle'
        cursor.execute(query_bus)
        one_bus = list(cursor.fetchall())
        cursor.close()

    except:
        one_bus = None

    return one_bus

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para obtener las alcaldias disponibles
def get_available_alcaldias():

    alcaldias = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT ubica_vehicle.alcaldia_cdmx, ubica_vehicle.geographic_point, ubica_vehicle.vehicle_current_status FROM ubica_vehicle'
        cursor.execute(query_bus)
        alcaldias = list(cursor.fetchall())
        cursor.close()

    except:
        alcaldias = None

    return alcaldias

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para verificar si la alcaldia existe
def get_alcaldia_exist(alcaldia):

    alcaldias = None
    status = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT alcaldia_cdmx FROM ubica_vehicle WHERE alcaldia_cdmx = "' + str(alcaldia) + '"'
        cursor.execute(query_bus)
        alcaldia = cursor.fetchall()
        cursor.close()

        if alcaldia:
            status = True
        else:
            status = False

    except:
        status = None

    return status

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion de consulta para obtener las unidades que esten dentro de una alcaldia
def get_vehicles_in_alcaldia():

    alcaldias = None

    try:
        cursor = mysql.connection.cursor()
        query_bus = 'SELECT ubica_vehicle.vehicle_id, ubica_vehicle.vehicle_label, ubica_vehicle.alcaldia_cdmx FROM ubica_vehicle'
        cursor.execute(query_bus)
        alcaldias = list(cursor.fetchall())
        cursor.close()

    except:
        alcaldias = None

    return alcaldias

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

