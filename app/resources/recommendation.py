from flask_restful import Resource

RECOMMENDATIONS = [
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'id': 1, 'name': 'Smoke on the water', 'artist': 'Deep Purple'}
]

class Recommendation(Resource):
    def get(self):
        return RECOMMENDATIONS
