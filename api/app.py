####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

from flask import Flask
from flask_mysqldb import MySQL

from itsdangerous import URLSafeTimedSerializer

from config import Configuration


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
#### variables de conexion a base de datos
PROD_HOST = 'localhost'
PROD_PORT = '3306'
PROD_USER = 'api_metrobus'
PROD_PASS = 'MetroBusUser01'
PROD_DB_NAME = 'ApiMetroBus'

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

app = Flask(__name__)

app.config.from_object(Configuration)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
#### configuracion para convertir a json
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
#### configuracion para conexion de base de datos
app.config['MYSQL_HOST'] = PROD_HOST
app.config['MYSQL_PORT'] = int(PROD_PORT)
app.config['MYSQL_DB'] = PROD_DB_NAME
app.config['MYSQL_USER'] = PROD_USER
app.config['MYSQL_PASSWORD'] = PROD_PASS
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

if mysql:
    print('--------------------------------------------')
    print('  ----  Connected to ApiMetroBus DB!')
    print('--------------------------------------------')
else:
    print('--------------------------------------------')
    print('  ----  Connection Error!')
    print('--------------------------------------------')

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

expiration = 300
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"], expiration)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

