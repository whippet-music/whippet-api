from flask import Flask
from flask_restful import Resource, Api

from config import DefaultConfig
from extensions import db, jwt

from auth import authenticate, identity

from resources import PingResource
from resources import TrackResource
from resources import TrackVoteResource
from resources import VoteListResource
from resources import RecommendationResource
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
    api.add_resource(TrackVoteResource, '/tracks/<int:track_id>/vote')
    api.add_resource(VoteListResource, '/votes')
    api.add_resource(MetaDataResource, '/meta_data')
    api.add_resource(RecommendationResource, '/recommendations')


def configure_extensions(app):
    db.init_app(app)

    jwt.authentication_handler(authenticate)
    jwt.identity_handler(identity)
    jwt.init_app(app)
