from flask_restful import Resource
from flask_jwt import jwt_required

RECOMMENDATIONS = [
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'}
]

class Recommendation(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return RECOMMENDATIONS
