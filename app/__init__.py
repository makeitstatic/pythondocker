from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager



# initialize app instance
app = Flask(__name__)

# fetch config
app.config.from_object(Config) #uppercase one is the class from config.py

# DB instance
db = SQLAlchemy(app)

# Migration engine handles updates
migrate = Migrate(app, db)

login = LoginManager(app)



from app import routes, models