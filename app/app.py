from flask import Flask
from flask_restful import Resource, Api

from resources import Ping
from resources import Recommendation


def create_app():
    app = Flask(__name__)

    configure_resources(app)

    return app


def configure_resources(app):
    api = Api(app)

    api.add_resource(Ping, '/ping')
    api.add_resource(Recommendation, '/recommendations')
