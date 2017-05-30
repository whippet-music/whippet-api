from flask_restful import reqparse, fields, marshal_with, Resource
from flask_jwt import jwt_required

from whippet_api.models import Track


track_fields = {
    'id': fields.Integer,
    'artist_name': fields.String,
    'title': fields.String,
    'release': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int,
                          action='append',
                          location='args')


class TrackResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(track_fields)
    def get(self):
        args = parser.parse_args()
        if 'id' in args and not args['id'] == None:
            return Track.query.filter(Track.id.in_(args['id'])).all()
        else:
            return Track.query.limit(10).all()
