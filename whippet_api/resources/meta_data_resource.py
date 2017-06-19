from flask import request
from flask_restful import fields, marshal_with, reqparse, Resource
from flask_jwt import jwt_required

from whippet_api.models import MetaData, Track


meta_data_fields = {
    'id': fields.Integer,
    'track_id': fields.Integer,
    'year': fields.Integer,
    'artist_familiarity': fields.Float,
    'artist_hotness': fields.Float,
    'artist_latitude': fields.Float,
    'artist_longitude': fields.Float,
    'duration': fields.Float,
    'end_of_fade_in': fields.Float,
    'key': fields.Integer,
    'key_confidence': fields.Float,
    'loudness': fields.Float,
    'mode': fields.Integer,
    'mode_confidence': fields.Float,
    'song_hotness': fields.Float,
    'start_of_fade_out': fields.Float,
    'tempo': fields.Float,
    'time_signature': fields.Integer,
    'time_signature_confidence': fields.Float,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
}

# parser = reqparse.RequestParser()
# parser.add_argument('track_id', type=int,
#                                 action='append',
#                                 location='args')


class MetaDataResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(meta_data_fields)
    def post(self):
        # args = parser.parse_args()
        json_data = request.get_json()
        if 'track_ids' in json_data and json_data['track_ids']:
            return MetaData.query.filter(MetaData.track_id.in_(json_data['track_ids'])).all()
        else:
            return MetaData.query.limit(10).all()
