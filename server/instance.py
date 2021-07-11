from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
         self.app = Flask(__name__)
         self.api = Api(self.app, version='1.0',
                        title='ILS - IFAM LAB SCHEDULER',
                        doc='/docs')
    def run(self, ):
        self.app.run(
            # retirar o debug true para o deploy
            debug=True
           
        )
server = Server()