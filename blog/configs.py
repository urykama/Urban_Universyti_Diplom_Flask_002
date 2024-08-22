import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.abspath(path='')

DEBUG = os.getenv('DEBUG')
#TESTING = os.getenv('TESTING')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/blog/db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '12345678l'
WTF_CSRF_ENABLED = True
FLASK_ADMIN_SWATCH = 'cosmo'
OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'

