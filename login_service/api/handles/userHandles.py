import logging

from flask import g, request
from flask_restful import Resource
from api.conf.auth import auth,refresh_jwt

from api.models.User import User
from api.database.database import db

class Register(Resource):
    
    @staticmethod
    def post():
        
        try:
            username, email, password = (
                request.json.get("username").strip(),
                request.json.get("password").strip(),
                request.json.get("email").strip(),
            )
        except Exception as why:
            logging.info("password or email is wrong. " + str(why))
        
        if username is None or email is None or password is None:
            return "ERROR",422
        
        if db.filter_user_by("email",email):
            return "ERROR"
        
        new_user=User(username,email,password)
        
        db.add_user(new_user)
        
        return {"status":"registration completed."},200
    
class login(Resource):
    
    @staticmethod
    def post():
        
        try:
            email,password = {
                request.json.get("email").strip(),
                request.json.get("password").strip() 
            }
        except Exception as why:
            return "ERROR1",422
        
        if email is None or password is None:
            return "ERROR2",422
        
        user = db.login(email,password)
                
        if user is None:
            return "ERROR3",422
        
        access_token = user.generate_auth_token()
        
        refresh_token = refresh_jwt.dumps({'email':email})
        
        return {
            "acess_token": access_token.decode(),
            "refresh_token": refresh_token.decode(),
        }
        