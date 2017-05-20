from flask_restful import Resource
from flask_jwt import jwt_required

from whippet_api.models import MetaData


class MetaDataResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return MetaData.query.all()
