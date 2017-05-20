from flask_restful import Resource
from flask_jwt import jwt_required

from whippet_api import models


class MetaData(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return models.MetaData.query.all()
