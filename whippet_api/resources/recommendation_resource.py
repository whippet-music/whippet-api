from flask_restful import reqparse, fields, marshal_with, Resource
from flask_jwt import jwt_required
from sqlalchemy  import func, desc

from whippet_api.models import Track, Vote


recommendation_fields = {
    'track_id': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('limit', type=float, location='args')


class RecommendationResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(recommendation_fields)
    def get(self):
        args = parser.parse_args()
        query = Track.query.outerjoin(Vote).filter(Vote.id == None).order_by(func.random())
        if 'limit' in args and args['limit']:
            total_count = query.count()
            limit_count = args['limit'] * total_count
            query = query.limit(limit_count)
        tracks = query.all()
        return [{'track_id': track.id} for track in tracks]
