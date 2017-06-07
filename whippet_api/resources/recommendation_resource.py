from flask_restful import fields, marshal_with, Resource
from flask_jwt import jwt_required, current_identity
from sqlalchemy  import func, desc

from whippet_api.models import Recommendation


recommendation_fields = {
    'user_id': fields.Integer,
    'track_id': fields.Integer
}


class RecommendationResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(recommendation_fields)
    def get(self):
        return Recommendation.query.filter_by(user_id=current_identity.id).limit(100).all()
