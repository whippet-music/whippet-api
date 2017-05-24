from flask_restful import fields, marshal_with, abort, request, Resource
from flask_jwt import jwt_required, current_identity

from whippet_api.models import Track, Vote
from whippet_api.app import db


track_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'track_id': fields.Integer,
    'vote_flag': fields.Boolean
}


class TrackVoteResource(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(track_fields)
    def post(self, track_id):
        track = Track.query.get(track_id)
        if not track:
            abort(404, message="Track {} does not exist".format(track_id))
        vote_data = request.get_json()
        print vote_data
        vote = Vote(user_id=current_identity.id,
                    track_id=track_id,
                    vote_flag=vote_data['vote_flag'])
        db.session.add(vote)
        db.session.commit()
        return vote


    def delete(self, track_id):
        vote = Vote.query.filter_by(user_id=current_identity.id,
                                    track_id = track_id).first()
        if not vote:
            abort(404, message="Vote does not exist")
        db.session.delete(vote)
        db.session.commit()
