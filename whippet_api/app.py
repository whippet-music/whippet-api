from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

from config import DefaultConfig

db = SQLAlchemy()

from resources import Ping
from resources import Recommendation
from resources import Track
from resources import MetaData


def create_app():
    app = Flask(__name__)

    configure_app(app)
    configure_resources(app)
    configure_extensions(app)

    return app


def configure_app(app):
    app.config.from_object(DefaultConfig)
    app.config.from_pyfile('.env', silent=True)


def configure_resources(app):
    api = Api(app)

    api.add_resource(Ping, '/ping')
    api.add_resource(Recommendation, '/recommendations')
    api.add_resource(Track, '/tracks')
    api.add_resource(MetaData, '/meta_data')


def configure_extensions(app):
    db.init_app(app)


app = create_app()

from auth import authenticate, identity

jwt = JWT(app, authenticate, identity)
