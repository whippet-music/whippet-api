from flask_restful import Resource
from flask_jwt import jwt_required


class Track(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return models.Track.query.all()
