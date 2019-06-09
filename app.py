from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.User import UserResource
from resources.Country import CountryResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# routes
# api.add_resource(Hello, '/hello')
api.add_resource(UserResource, '/user')
api.add_resource(CountryResource, '/country')
