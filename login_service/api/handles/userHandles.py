import logging

from flask import g, request
from flask_restful import Resource

from models.User import User
from database.database import Database

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
        
        #f username is None or email is None or password is None:
            #missing data