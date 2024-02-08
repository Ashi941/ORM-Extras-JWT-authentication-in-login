from flask_restful import  Resource
from app.user.user_tables import Users
from app import db
from flask import request
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity

class GetUsers(Resource):
    def get(self):
        user = Users.query.all()
        if user:
            return {'username': user.username, 'email':user.email}
        else:
            return {'message':'User not found'},404
       
    # to create users
       
    def post(self):
        try:
            data = request.get_json()
            new_user = Users (
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                mobile=data.get('mobile'),
                city=data.get('city'),
                designation=data.get('designation')
 
 
            )
            db.session.add(new_user)
            db.session.commit()
            return {'message':'User registered sucessfully'},201
        except Exception as e:
            print(e)
            return {'message':'User registration failed'},500
        
        #logic for user login
class UserLogin(Resource):
    def post(self):
        try:
            data =request.get_json()
            username = data.get('username')
            password = data.get('password')
            #Check is the username actually exists or not in DB
            user = Users.query.filter_by(username=username).first()
            
            if user:
                #logic to aunthenticate
                if user and user.password == password:
                    #Create jwt token for the user
                    access_token = create_access_token(identity = user.id)
                    return {'access_token':access_token},200
                return{'message':'User login failed'},401
            else:
                return{'message':'User not found'},400
        except Exception as e:
            print(e)
            return{"message":"No user found"},500
#To check whether the any user is there or not
class UserInfo(Resource):
    #token authorisation that is after login any further request will need the access token(expires after a while)
    @jwt_required()
    def get(self):
        
        #Identify the user whi just logged in
        current_user = get_jwt_identity()
        user = Users.query.get(current_user)
        user_data = {
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'mobile':user.mobile,
            'city':user.city,
            'designation':user.designation

                    }
        
    
        return user_data, 200
