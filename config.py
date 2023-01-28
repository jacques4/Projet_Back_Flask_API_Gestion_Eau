import os

#basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jacques@localhost:5432/flask_db'
SQLALCHEMY_TRACK_MODIFICATIONS  = False