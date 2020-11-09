from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

import logging
from logging.handlers import SMTPHandler

from logging.handlers import RotatingFileHandler
import os


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

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='PythonDocker Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/pythondocker.log', maxBytes=20480,
                                       backupCount=20)
    #  I'm using a format that includes the timestamp, the logging level, the message and the source file and line number from where the log entry originated.
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('PythonDocker startup')

from app import routes, models, errors