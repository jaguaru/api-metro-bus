import routes
from app import app

#### configuraciones de conexion para ip y puerto del servidor

#### servidor visible externamente
#### variables para conexion del servidor
HOST = '0.0.0.0'
PORT = 7001

#### importando el archivo de rutas blueprint
from api.v1.vehicles.blueprint import api_metro_bus

#### configuracion de ruta del blueprint
app.register_blueprint(api_metro_bus, url_prefix='/api/v1/vehicles')


#### inicia el servidor flask
if __name__ == '__main__':
   app.run(host=HOST, port=PORT)