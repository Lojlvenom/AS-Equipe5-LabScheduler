from flask import Flask,redirect,url_for,render_template,request
import sys
from database.database import Database
from models.User import User


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5006,debug=True)