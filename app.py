from flask import Blueprint
from flask_restful import Api
from resources.User import UserResource
from resources.Country import CountryResource
from resources.UserLogin import UserLoginResource
from resources.UserLogout import UserLogoutResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# routes
api.add_resource(UserResource, '/user')
api.add_resource(CountryResource, '/country')
api.add_resource(UserLoginResource, '/login')
api.add_resource(UserLogoutResource, '/logout')
