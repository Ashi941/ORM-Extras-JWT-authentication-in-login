from flask import Blueprint
from flask_restful import Api
from app.user.user_logic import GetUsers,UserLogin,UserInfo

user_bp = Blueprint('userbp', __name__)
api = Api(user_bp)

api.add_resource(GetUsers, '/user')
api.add_resource(UserLogin, '/login')
api.add_resource(UserInfo, '/info')


