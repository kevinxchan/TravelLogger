from flask import request
from flask_login import login_user, current_user
from flask_restful import Resource
from model import User, UserSchema

user_schema = UserSchema()


class UserLoginResource(Resource):

    def get(self):
        if current_user.is_authenticated:
            return {'message': 'User {} is authenticated'.format(current_user)}, 200
        else:
            return {'message': 'User {} is not authenticated'.format(current_user)}, 400

    def post(self):
        json_data = request.get_json(force=True)
        if json_data is None:
            return {'message': 'No input data provided'}, 400
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(username=data['username']).first()
        supplied_password = json_data['password']
        if user is None or not user.check_password(supplied_password):
            return {'message': 'Invalid username or password provided'}, 400
        remember_status = json_data['remember']
        login_user(user, remember=remember_status)
        return {'message': 'Successfully logged in'}, 200
