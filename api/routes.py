####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
import datetime

from app import app

from flask import Flask


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

#### muestra la fecha y hora actual al iniciar el servidor
datetime_now_str = str(datetime.datetime.now())
print('---------------------------------------------------------')
print('  ----  Fecha y hora ', datetime_now_str)
print('---------------------------------------------------------')

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### mensaje de bienvenida
@app.route('/', methods=["GET", "POST"])
def inicio():
    return 'Bienvenido al API MetroBus CDMX!'

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

