import sys
sys.path.append('../server')
from flask import Flask
from flask_restx import Api, Resource
from instance import server
from rabbit_server import rabbit_instance as rb
import json

app, api = server.app, server.api 


notification_queue = 'notification_queue'

rb.create_queue(notification_queue)

@api.route('/notification')
class Notification(Resource):
    @api.doc(responses={ 200: 'OK', 403: 'invalid json' },
        params = {
        'reservation_hash':'hash cretaed on reservation service',
            "title":" title from reservation",
            "spaces":"chosen spaces to be reserved",
            "date_time":"date and time from reservation",
            "email_list":"list of participants emails",
            "obs":"some obs from reservations creator"
    },)
    
    def post(self,):
        body = api.payload
        print(body)
        if('reservation_hash' not in body):
            response_json = {
                "message":"invalid json"
            }
            return response_json, 403
        else:
            to_publish_json = json.dumps(body)
            response_json = {
                "message":"notification sent"
            }

            rb.publish(routing_key='notification_queue', body=to_publish_json)
            return response_json,200
    
server.run()





