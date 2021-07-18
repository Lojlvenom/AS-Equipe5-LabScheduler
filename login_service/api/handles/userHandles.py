import logging

from flask import g, request
from flask_restful import Resource
from api.conf.auth import auth,refresh_jwt

import api.error.errors as error
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
            return error.INVALID_INPUT_422
        
        if username is None or email is None or password is None:
            return error.INVALID_INPUT_422
        
        if db.filter_user_by("email",email):
            return error.ALREADY_EXIST
        
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
        except Exception:
            return error.INVALID_INPUT_422
        
        if email is None or password is None:
            return error.INVALID_INPUT_422
        
        user = db.login(email,password)
                
        if user is None:
            return error.UNAUTHORIZED
        
        access_token = user.generate_auth_token()
        
        refresh_token = refresh_jwt.dumps({'email':email})
        
        return {
            "acess_token": access_token.decode(),
            "refresh_token": refresh_token.decode(),
        }

