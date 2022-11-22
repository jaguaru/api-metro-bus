import routes
from app import app

#### configuraciones de conexion para ip y puerto del servidor

#### localhost server
#HOST = '127.0.1.2'

#### externally visible server
HOST = '0.0.0.0'
PORT = 7001

#### inicia el servidor flask
if __name__ == '__main__':
   app.run(host=HOST, port=PORT)