from flask import Flask
from flask_restful import Resource, Api
from resources import ping_resource

app = Flask(__name__)
api = Api(app)

api.add_resource(ping_resource.PingResource, '/ping')

if __name__ == '__main__':
    app.run(debug=True)
