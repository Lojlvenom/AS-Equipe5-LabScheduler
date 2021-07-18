from flask import Flask,redirect,url_for,render_template,request
import sys
from database.database import Database
from models.User import User


# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    # app.run(port=5006,debug=True)

    db = Database()
    new_user=User('Carlos Antonio','email@email.com','senhaqualquer')

    db.add_user(data = new_user)
    new_user=User('Maria Lima','maria.lima@email.com','senhaqualquer')
    db.add_user(data = new_user)
    print(db.filter_user_by('name','Carlos Antonio'))
    print(db.login('maria.lima@email.com','senhaqualquer'))

    print(db.listAll())