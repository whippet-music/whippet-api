from flask_restful import Resource
from flask_jwt import jwt_required

from whippet_api.models import Track


class TrackResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return Track.query.all()
