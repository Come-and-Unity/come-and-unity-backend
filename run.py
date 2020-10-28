from app_config import APP
from api.authentication import LogoutResource
from api.user_profile import ProfileResource

if __name__ == '__main__':
    APP.run(debug=True)