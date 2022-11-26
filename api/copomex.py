
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

import json
import requests

from config import Configuration


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

#### variable para obtener la llave del archivo de configuracion
API_KEY = Configuration().API_KEY_COPOMEX

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### funcion para obtener el municipio con las coordenadas de latitud and longitud de cada vehiculo
def geocode_reverse(latitude, longitude):

    #### url para obtener los datos mediante geocoding reverse
    url_copomex = 'https://api.copomex.com/query/info_cp_geocoding_reverse?lat=' + str(latitude) + '&lng=' + str(longitude) + '&token=' + API_KEY

    #### obtener el request del url
    response = requests.get(url_copomex)

    #### convierte la respuesta en texto y despues se convierte en json
    data = response.text
    json_loads = json.loads(data)

    #### obtener el municipio del json
    municipio = str(json_loads['response']['municipio'])

    return municipio

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

