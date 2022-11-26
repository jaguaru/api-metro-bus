import unittest
import requests


class TestAPIMetroBus(unittest.TestCase):
      
      #### test para la ruta del API de vehiculos_disponibles
      def test_available_vehicles(self):

          response = requests.get('http://0.0.0.0:7001/api/v1/vehicles/vehiculos_disponibles/')
          status_code = response.status_code
          expected = 200

          assert status_code == expected

      #### test para la ruta del API de ubicacion_vehiculo
      def test_location_vehicles(self):

          response = requests.post('http://0.0.0.0:7001/api/v1/vehicles/ubicacion_vehiculo/', json={ "vehicle_id": "737" })
          status_code = response.status_code
          expected = 200

          assert status_code == expected

      #### test para la ruta del API de alcaldias_disponibles
      def test_available_alcaldias(self):

          response = requests.get('http://0.0.0.0:7001/api/v1/vehicles/alcaldias_disponibles/')
          status_code = response.status_code
          expected = 200

          assert status_code == expected
    
      #### test para la ruta del API de unidades_en_alcaldia
      def test_unidades_alcaldias(self):

          response = requests.post('http://0.0.0.0:7001/api/v1/vehicles/unidades_en_alcaldia/', json={ "alcaldia_cdmx": "Iztapalapa" })
          status_code = response.status_code
          expected = 200

          assert status_code == expected




if __name__ == '__main__':
   unittest.main()

