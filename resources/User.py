from flask import request
from flask_restful import Resource
from model import db, User, UserSchema

user_schema = UserSchema()


class UserResource(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        if json_data is None:
            return {'message': 'No input data provided'}, 400
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user is not None:
            return {'message': 'That username is already taken'}, 400

        new_user = User(json_data['username'], json_data['password'], json_data.get('first_name'),
                        json_data.get('last_name'))
        db.session.add(new_user)
        db.session.commit()
        result = user_schema.dump(new_user).data
        return {'status': 'success', 'data': result}, 200

    def delete(self):
        json_data = request.get_json(force=True)
        if json_data is None:
            return {'message': 'No input data provided'}, 400
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422

        user_to_delete = User.query.filter_by(username=data['username'])
        user_deletion_obj = user_to_delete.first()
        supplied_password = json_data['password']
        if not user_deletion_obj.check_password(supplied_password):
            return {'message': 'Incorrect password supplied'}, 400
        else:
            result = user_schema.dump(user_deletion_obj).data
            user_to_delete.delete()
            db.session.commit()
            return {'status': 'success', 'data': result}, 200
