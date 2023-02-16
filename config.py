import os

#basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jacques@localhost:5432/FLASK_DB'
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jacques@localhost:5432/FLASK_BD'
SQLALCHEMY_TRACK_MODIFICATIONS  = False
JWT_SECRET_KEY = "JWT_SECRET_KEY"
#app.config['SECRET_KEY']='96c82bfeb75e764e979e3205303fe70f'