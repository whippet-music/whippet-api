from flask_restful import fields, marshal_with, Resource
from flask_jwt import jwt_required
from sqlalchemy  import func, desc

from whippet_api.models import Track


recommendation_fields = {
    'track_id': fields.Integer
}


class RecommendationResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(recommendation_fields)
    def get(self):
        tracks = Track.query.order_by(func.random()).limit(10).all()
        return [{'track_id': track.id} for track in tracks]
