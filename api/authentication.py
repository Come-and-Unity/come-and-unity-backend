"""Authentication resource views"""
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from flask_restful import Resource
from flask_api import status
from flask import jsonify, request, session, make_response
from serializers.user_schema import LoginSchema
from app_config import API
from models.user import User
from app_config import BCRYPT

LOGIN_SCHEMA = LoginSchema()

JWT_TOKEN = 'jwt_token'


class LogoutResource(Resource):
    """
    Implementation sign out method
    """
    def get(self):
        """Get method for sign out"""
        session.clear()
        response = {
            'is_logout': True,
        }
        return make_response(response, status.HTTP_200_OK)


class LoginResource(Resource):
    """Implementation sign in method"""
    def post(self):
        """Post method for sign in"""
        try:
            data = LOGIN_SCHEMA.load(request.json)
            current_user = User.find_user(user_name=data['user_name'])
        except ValidationError as error:
            return make_response(jsonify(error.messages), status.HTTP_400_BAD_REQUEST)
        try:
            check_password = BCRYPT.check_password_hash(current_user.user_password, data['user_password'])
            if not check_password:
                raise AttributeError
        except AttributeError:
            response_object = {
                'Error': 'Your password or login is invalid'
            }
            return make_response(response_object, status.HTTP_400_BAD_REQUEST)

        session.permanent = True
        access_token = create_access_token(identity=current_user.id, expires_delta=False)
        session[JWT_TOKEN] = access_token
        response_object = {
            "access_token": access_token
        }
        return make_response(jsonify(response_object), status.HTTP_200_OK)


API.add_resource(LogoutResource, '/logout')
API.add_resource(LoginResource, '/login')