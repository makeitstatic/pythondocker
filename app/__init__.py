from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# "set FLASK_DEBUG=1" in environment for debug mode

# initialize app instance
app = Flask(__name__)

# fetch config
app.config.from_object(Config)  # uppercase one is the class from config.py

# DB instance
db = SQLAlchemy(app)

# Migration engine handles schema updates
migrate = Migrate(app, db)

# Specify login page for Flask-Login
login = LoginManager(app)
# 'login' refers to url_for() in routes.py
login.login_view = 'login'

from app import routes, models