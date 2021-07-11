import sys
sys.path.append('../server')
from flask import Flask
from flask_restx import Api, Resource
from instance import server
from rabbit_server import channel
import json
app, api = server.app, server.api 

@api.route('/test_notification')
class Notification(Resource):
    def get(self,):
        channel.basic_publish(exchange='', routing_key='notify_queue', body='algum teste aleatorio')
        return "notification sent",200
server.run()





