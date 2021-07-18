from flask import Flask,redirect,url_for,render_template,request
from api.conf.routes import generete_routes

def create_app():
     app =Flask(__name__)
     app.config['DEBUG'] = True
     
     generete_routes(app)
     
     return app 

if __name__ == '__main__':
    app = create_app()
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5050,host='localhost',use_reloader=True)
