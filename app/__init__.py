from flask import Flask
from config import Config
# Flask-SQLAlchemy, an extension that provides a Flask-friendly wrapper to the popular
# SQLAlchemy package, which is an Object Relational Mapper (ORM)
from flask_sqlalchemy import SQLAlchemy
#Alembic: a database migrations tool for SQLAlchemy.
#flask_migrate: a wrapper for Alembic
from flask_migrate import Migrate

flask_app = Flask(__name__)

#flask_app.config.from_json("config.json")
flask_app.config.from_object(Config)
#get database objects
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes, models
