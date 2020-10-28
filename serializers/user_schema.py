"""Schema for user-service"""
from marshmallow import fields
from app_config import MARSHMALLOW
from models.user import User


class UserSchema(MARSHMALLOW.ModelSchema):
    """
    Schema for User Model
    """
    class Meta:
        """
        Class meta for model schema by user
        """
        model = User


class LoginSchema(MARSHMALLOW.Schema):
    """
    Schema for Auth functionality
    """
    user_name = fields.Str()
    user_password = fields.Str()