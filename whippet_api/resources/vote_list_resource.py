from flask_restful import fields, marshal_with, abort, request, Resource
from flask_jwt import jwt_required, current_identity

from whippet_api.models import Track, Vote
from whippet_api.app import db


vote_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'track_id': fields.Integer,
    'vote_flag': fields.Boolean
}


class VoteListResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(vote_fields)
    def get(self):
        user_votes = Vote.query.filter_by(user_id=current_identity.id).all()
        return user_votes
