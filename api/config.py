import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#### configuracion de clase para variables globales
class Configuration(object):
      DEBUG = True
      #DEBUG = False
      SECRET_KEY = 'ArkonDataSuperSecretKey1234@"$]*&('
      STATIC_DIR = os.path.join(BASE_DIR, 'static')
      API_KEY_COPOMEX = 'c7ed64ec-1490-4ed7-8403-eb28f2b684a2'