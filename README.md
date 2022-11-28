Adquisición de Datos y Consumo de API del Metro Bus de la CDMX
==============================================================


![Diagrama Pipeline para la Adquisición de Datos y Consumo de API del Metro Bus de la CDMX]



Descargar Repositorio:
----------------------

    $ git clone https://github.com/jaguaru/api-metro-bus.git


Creacion de Imagen con Docker:
------------------------------

Abrir el directorio api/

    $ cd api-metro-bus/api

Crear la imagen del contenedor

    $ docker build -t api-metro-bus .

Activar el contenedor

    $ docker run -it -p 7000:7001 api-metro-bus


Automatización de Docker con Kubernetes:
----------------------------------------

Iniciar minikube

    $ minikube start

Cargar la imagen de Docker

    $ minikube image load api-metro-bus

Abrir el directorio kubernetes

    $ cd kubernetes

Crear despliegue del clúster

    $ kubectl apply -f apimetrobus-deployment.yaml

Ver clúster desplegado

    $ kubectl get deploy

Ver los pods creados

    $ kubectl get pod

Aumentar el número de replicas desplegadas

    $ kubectl scale deployment api-metro-bus --replicas=4

Crear un servicio para publicar la aplicación

    $ kubectl apply -f apimetrobus-service.yaml

Ver el servicio creado

    $ kubectl get svc

Crear el recurso de ingreso

    $ kubectl apply -f apimetrobus-ingress.yaml


Iniciar el servidor sin Docker:
--------------------------------

Abrir el directorio kubernetes

    $ cd api-metro-bus

Crear el directorio para el entorno virtual
    
    $ mkdir vserver

Crear el entorno virtual
    
    $ virtualenv -p python3 vserver

Activar el entorno virtual

    $ source vserver/bin/activate

Entorno virtual activado
    
    (vserver) $

Abrir el directorio api/

    (vserver) $ cd api

Instalar la paqueteria

    (vserver) $ pip install -r requirements.txt

Iniciar el servidor

    (vserver) $ python3 main.py

Servidor activado

    $ --------------------------------------------
    $ ----  Connected to ApiMetroBus DB!
    $ --------------------------------------------
    $ ---------------------------------------------------------
    $ ----  Fecha y hora  2022-11-28 00:00:00.000000
    $ ---------------------------------------------------------
    $ * Serving Flask app 'app'
    $ * Debug mode: on
    $ WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    $ * Running on all addresses (0.0.0.0)
    $ * Running on http://127.0.0.1:7001
    $ * Running on http://170.120.0.1:7001
    $ Press CTRL+C to quit
    $ * Restarting with stat
    $ --------------------------------------------
    $ ----  Connected to ApiMetroBus DB!
    $ --------------------------------------------
    $ ---------------------------------------------------------
    $ ----  Fecha y hora  2022-11-28 00:00:00.000000
    $ ---------------------------------------------------------
    $ * Debugger is active!
    $ * Debugger PIN: 905-978-493


Consumo del API 
===============

Usando el comando curl
----------------------

Obtener todos los vehiculos disponibles

    $ curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/api/v1/vehicles/vehiculos_disponibles/

Obtener la ubicacion de un vehiculo mediante el vehicle_id

    $ curl -H "Content-Type: application/json" -X POST -d '{ "vehicle_id": "737" }' http://0.0.0.0:7001/api/v1/vehicles/ubicacion_vehiculo/

Obtener todos las alcaldias disponibles

    $ curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/api/v1/vehicles/alcaldias_disponibles/

Obtener todas las unidades dentro de una alcaldia

    $ curl -H "Content-Type: application/json" -X POST -d '{ "alcaldia_cdmx": "Iztapalapa" }' http://0.0.0.0:7001/api/v1/vehicles/unidades_en_alcaldia/


Hacer las pruebas unitarias
===========================

Abrir una consola y seguir las instrucciones en la sección Iniciar el servidor sin Docker

Abrir otra consola y ejecutar los siguientes pasos

Abrir el directorio api-metro-bus/

    $ cd api-metro-bus

Activar el entorno virtual

    $ source vserver/bin/activate

Entorno virtual activado
    
    (vserver) $

Abrir el directorio test/

    (vserver) $ cd api/test

Ejecutar el script de las pruebas

    (vserver) $ python3 unit_test_api.py

Resultado de pruebas

    $ ....
    $ ----------------------------------------------------------------------
    $ Ran 4 tests in 0.060s

    $ OK


Crear la base de datos
======================

 Nombre de la base de datos: ApiMetroBus

 Crear la tabla ubica_vehicles

    $ cd database

 Ver archivo create_table.py

 Modificar las variables de conexion a base de datos en el archivo app.py

    PROD_HOST = '<host>'
    PROD_PORT = '<port>'
    PROD_USER = '<user>'
    PROD_PASS = '<pass>'
    PROD_DB_NAME = 'ApiMetroBus'


Cargar los datos del Metro Bus del archivo CSV
==============================================

Abrir el directorio api-metro-bus/

    $ cd api-metro-bus

Activar el entorno virtual

    $ source vserver/bin/activate

Entorno virtual activado
    
    (vserver) $

Abrir el directorio api/

    (vserver) $ cd api

Ejecutar el script para cargar los datos

    (vserver) $ python3 ingest.py

Resultado de los datos guardados en la base de datos

    $ --------------------------------------------
    $   ----  Connected to ApiMetroBus DB!
    $ --------------------------------------------
    $   ----  Cargando datos ...
    $   ----  Se terminaron de cargar todos los datos!
    $ --------------------------------------------
    $ --------------------------------------------
