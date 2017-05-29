from flask_restful import fields, marshal_with, Resource
from flask_jwt import jwt_required

from whippet_api.models import Track


track_fields = {
    'id': fields.Integer,
    'artist_name': fields.String,
    'title': fields.String,
    'release': fields.String
}


class TrackResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(track_fields)
    def get(self):
        return Track.query.limit(10).all()
