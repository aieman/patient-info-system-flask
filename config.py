import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # Calculates the absolute path to the directory where Config.py file is
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')  
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'abce1234'
