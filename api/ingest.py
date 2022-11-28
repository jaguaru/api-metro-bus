####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

import pandas as pd
import time

from queries import store_csv_data
from copomex import geocode_reverse

from app import mysql


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
try:
    #### leer el archivo CSV y pasarlo a una variable
    df = pd.read_csv('static/prueba_fetchdata_metrobus.csv', index_col=0)

    #### obtener los nombres de las columnas
    column_names = list(df.columns)

    #### obtener el numero de filas
    num_rows = int(df.shape[0])
    #print(' ----  num_rows  ', num_rows)

    #### inicializar contador
    count_rows = 0

    print('  ----  Cargando datos ...')

    #### obtener todas las filas del archivo
    for data in range(10):
    #for data in range(num_rows):

        date_updated = str(df.loc[count_rows, 'date_updated'])
        vehicle_id = str(df.loc[count_rows, 'vehicle_id'])
        vehicle_label = str(df.loc[count_rows, 'vehicle_label'])
        vehicle_current_status = str(df.loc[count_rows, 'vehicle_current_status'])

        position_latitude = str(df.loc[count_rows, 'position_latitude'])
        position_longitude = str(df.loc[count_rows, 'position_longitude'])
        geographic_point = str(df.loc[count_rows, 'geographic_point'])
        position_speed = str(df.loc[count_rows, 'position_speed'])
        position_odometer = str(df.loc[count_rows, 'position_odometer'])

        trip_schedule_relationship = str(df.loc[count_rows, 'trip_schedule_relationship'])
        #### reemplazar celadas vacias con none
        #### convertir de numero a cadena y eliminar el punto flotante
        trip_id = str(df.loc[count_rows, 'trip_id']).replace('.0', '').replace('nan', 'None')
        trip_start_date = str(df.loc[count_rows, 'trip_start_date']).replace('.0', '').replace('nan', 'None')
        trip_route_id = str(df.loc[count_rows, 'trip_route_id']).replace('.0', '').replace('nan', 'None')
        
        #### reducir el numero de decimales para obtener la alcaldia con las coordenadas
        lat_round = str(round(float(position_latitude), 6))
        lng_round = str(round(float(position_longitude), 6))

        alcaldia_cdmx = geocode_reverse(lat_round, lng_round)

        # print('--------------------------------------------------------')
        # print(' ----  date_updated  ', date_updated)
        # print('--------------------------------------------------------')
        # print(' ----  vehicle_id  ', vehicle_id)
        # print(' ----  vehicle_label  ', vehicle_label)
        # print(' ----  vehicle_current_status  ', vehicle_current_status)
        # print('--------------------------------------------------------')
        # print(' ----  position_latitude  ', position_latitude)
        # print(' ----  position_longitude  ', position_longitude)
        # print(' ----  geographic_point  ', geographic_point)
        # print(' ----  position_speed  ', position_speed)
        # print(' ----  position_odometer  ', position_odometer)
        # print('--------------------------------------------------------')
        # print(' ----  trip_schedule_relationship  ', trip_schedule_relationship)
        # print(' ----  trip_id  ', trip_id)
        # print(' ----  trip_start_date  ', trip_start_date)
        # print(' ----  trip_route_id  ', trip_route_id)
        # print('--------------------------------------------------------')
        # print('--------------------------------------------------------')
        # print(' ----  alcaldia_cdmx  ', alcaldia_cdmx)
        # print('--------------------------------------------------------')
        # print('--------------------------------------------------------')
        
        data_store = store_csv_data(date_updated, 
                                    vehicle_id, 
                                    vehicle_label, 
                                    vehicle_current_status, 
                                    position_latitude, 
                                    position_longitude, 
                                    geographic_point, 
                                    position_speed, 
                                    position_odometer, 
                                    trip_schedule_relationship, 
                                    trip_id, 
                                    trip_start_date, 
                                    trip_route_id,
                                    alcaldia_cdmx)

        # print('--------------------------------------------------------')
        # print(' ----  data_store  ', data_store)
        # print('--------------------------------------------------------')

        #### aumento del contador
        count_rows = count_rows + 1

        #### tiempo de espera para no saturar al API
        time.sleep(0.1)
    
except:
    print('  ----  Ocurrio un error al cargar los datos!')


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
print('  ----  Se terminaron de cargar todos los datos!')
print('--------------------------------------------')
print('--------------------------------------------')
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

