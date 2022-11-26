import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#### configuracion de clase para variables globales
class Configuration(object):
      DEBUG = True
      #DEBUG = False
      SECRET_KEY = 'ArkonDataSuperSecretKey1234@"$]*&('
      STATIC_DIR = os.path.join(BASE_DIR, 'static')
      API_KEY_COPOMEX = '3c2d14a5-4c57-444e-b1a0-418f59eabd6a'