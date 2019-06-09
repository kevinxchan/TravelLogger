from flask_login import logout_user
from flask_restful import Resource


class UserLogoutResource(Resource):

    def get(self):
        logout_user()
        return {'message': 'Successfully logged out'}, 200
