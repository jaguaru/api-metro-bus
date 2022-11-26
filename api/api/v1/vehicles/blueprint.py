####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

from queries import get_available_vehicles, get_vehicle_by_id, get_available_alcaldias
from queries import get_vehicles_in_alcaldia, get_alcaldia_exist

from flask import Flask, Blueprint, redirect, url_for, request, jsonify, make_response
from app import app, mysql


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

#### variable para creacion de la ruta blueprint
api_metro_bus = Blueprint('/v1/vehicles', __name__)

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  Ejemplo para consumo de API mediante el comando curl
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/api/v1/vehicles/vehiculos_disponibles/
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### ruta para obtener todos los vehiculos disponibles
@api_metro_bus.route('/vehiculos_disponibles/', methods=["GET"])
def get_available_buses():
    
    status = '1' #### estado disponible
    #### usar la funcion filter para obtener los vehiculos disponibles
    available_vehicles = list(filter(lambda x: x['vehicle_current_status'] == status, get_available_vehicles()))
    
    try:
        #### si el valor de la funcion no esta vacia se envia la informacion obtenida
        if available_vehicles:
           return jsonify(available_vehicles), 200
        #### si el valor de la funcion esta vacia se envia un mensaje
        else:
           msg_status = {'msg': 'Es posible que los vehiculos no esten disponibles'}
           return jsonify(msg_status), 200
    
    except:
        #### en caso de una excepcion se envia un mensaje de error
        msg_error = {'msg': 'Not Found - Error'}
        return jsonify(msg_error), 400

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  Ejemplo para consumo de API mediante el comando curl
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  ejemplo cuando el vehiculo no existe en la base de datos
####--------------------------------------------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "vehicle_id": "001" }' http://0.0.0.0:7001/api/v1/vehicles/ubicacion_vehiculo/
####--------------------------------------------------------------------------------------------------------------
####  ejemplo cuando el vehiculo si existe en la base de datos
####--------------------------------------------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "vehicle_id": "737" }' http://0.0.0.0:7001/api/v1/vehicles/ubicacion_vehiculo/
####--------------------------------------------------------------------------------------------------------------
#### ruta para obtener la ubicacion de un vehiculo mediante el vehicle_id
@api_metro_bus.route('/ubicacion_vehiculo/', methods=["POST"])
def get_bus_by_id():

    #### obtener el vehicle_id de la peticion
    vehicle_id = str(request.json.get('vehicle_id'))

    #### usar la funcion filter para obtener el vehiculo por vehicle_id
    vehicle_by_id = list(filter(lambda x: x['vehicle_id'] == vehicle_id, get_vehicle_by_id()))

    try:
       #### si el valor de la funcion no esta vacia se envia la informacion obtenida
       if vehicle_by_id:
          return jsonify(vehicle_by_id), 200
       #### si el valor de la funcion esta vacia se envia un mensaje
       else:
          msg_status = {'msg': 'El ID del vehiculo no existe!'}
          return jsonify(msg_status), 200
    
    except:
       #### en caso de una excepcion se envia un mensaje de error
       msg_error = {'msg': 'Not Found - Error'}
       return jsonify(msg_error), 400

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  Ejemplo para consumo de API mediante el comando curl
####--------------------------------------------------------------------------------------------------------------
####  curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/api/v1/vehicles/alcaldias_disponibles/
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### ruta para obtener todos las alcaldias disponibles
@api_metro_bus.route('/alcaldias_disponibles/', methods=["GET"])
def get_available_alcadias():
    
    status = '1' #### estado disponible
    #### usar la funcion filter para seleccionar las alcaldias disponibles
    available_alcaldias = list(filter(lambda x: x['vehicle_current_status'] == status, get_available_alcaldias()))
    
    try:
        #### si el valor de la funcion no esta vacia se envia la informacion obtenida
        if available_alcaldias:
           return jsonify(available_alcaldias), 200
        #### si el valor de la funcion esta vacia se envia un mensaje
        else:
           msg_status = {'msg': 'Es posible que los alcaldias no esten disponibles'}
           return jsonify(msg_status), 200
    
    except:
        #### en caso de una excepcion se envia un mensaje de error
        msg_error = {'msg': 'Not Found - Error'}
        return jsonify(msg_error), 400

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  Ejemplo para consumo de API mediante el comando curl
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
####  ejemplo cuando no existen los vehiculos dentro de una alcaldia en la base de datos
####--------------------------------------------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "alcaldia_cdmx": "Tuxtla Gutiérrez" }' http://0.0.0.0:7001/api/v1/vehicles/unidades_en_alcaldia/
####--------------------------------------------------------------------------------------------------------------
####  ejemplo cuando existen los vehiculos dentro de una alcaldia en la base de datos
####--------------------------------------------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST -d '{ "alcaldia_cdmx": "Iztapalapa" }' http://0.0.0.0:7001/api/v1/vehicles/unidades_en_alcaldia/
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### ruta para obtener todas las unidades dentro de una alcaldia
@api_metro_bus.route('/unidades_en_alcaldia/', methods=["POST"])
def get_unidad_alcaldia():
    
    #### obtener la alcaldia de la peticion
    alcaldia = str(request.json.get('alcaldia_cdmx'))

    #### verificar si la alcaldia existe
    alcaldia_exist = get_alcaldia_exist(alcaldia)

    #### si alcaldia no esta vacia y alcaldia_exist es igual a True
    if alcaldia and alcaldia_exist:

       #### usar la funcion filter para obtener los vehiculos dentro de la alcaldia
       unidad_alcaldia = list(filter(lambda x: x['alcaldia_cdmx'] == alcaldia, get_vehicles_in_alcaldia()))

       try:
          #### si el valor de la funcion no esta vacia se envia la informacion obtenida
          if unidad_alcaldia:
             return jsonify(unidad_alcaldia), 200
          #### si el valor de la funcion esta vacia se envia un mensaje
          else:
             msg_status = {'msg': 'Es posible que el vehiculo no este dentro de la alcaldia'}
             return jsonify(msg_status), 200
      
       except:
          #### en caso de una excepcion se envia un mensaje de error
          msg_error = {'msg': 'Not Found - Error'}
          return jsonify(msg_error), 400
    
    else:
       msg_error = {'msg': 'La alcaldia no existe o no es correcta'}
       return jsonify(msg_error), 200

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

