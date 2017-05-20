from flask_restful import Resource
from flask_jwt import jwt_required

TRACKS = [
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'id': 2, 'name': 'Personal Jesus', 'artist': 'Depeche Mode'},
    {'id': 3, 'name': 'Wrong', 'artist': 'Depeche Mode'},
    {'id': 4, 'name': 'Jaded', 'artist': 'Aerosmith'},
    {'id': 5, 'name': 'Dream On', 'artist': 'Aerosmith'},
    {'id': 6, 'name': 'Wish You Were Here', 'artist': 'Pink Floyd'}
]

class Track(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return TRACKS
