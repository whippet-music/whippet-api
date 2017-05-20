from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

from config import DefaultConfig

db = SQLAlchemy()

from resources import PingResource
from resources import RecommendationResource
from resources import TrackResource
from resources import MetaDataResource


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

    api.add_resource(PingResource, '/ping')
    api.add_resource(TrackResource, '/tracks')
    api.add_resource(MetaDataResource, '/meta_data')
    api.add_resource(RecommendationResource, '/recommendations')


def configure_extensions(app):
    db.init_app(app)


app = create_app()

from auth import authenticate, identity

jwt = JWT(app, authenticate, identity)
