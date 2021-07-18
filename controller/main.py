import sys

from flask.globals import request
sys.path.append('../server')
from flask import Flask,request
from flask_restx import Api, Resource
from instance import server
from rabbit_server import rabbit_instance as rb
import json
import requests

app, api = server.app, server.api 


notification_queue = 'notification_queue'
URL_AUTH_REGISTER="http://localhost:5006/auth/register"
URL_AUTH_LOGIN="http://localhost:5006/auth/login"
URL_BOOKING="http://localhost:5008/api/booking"

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


@api.route('/register')
class ResgisterUser(Resource):
    
    def post(self):
        body = request.get_json(force=True)
        
        result = requests.post(url=URL_AUTH_REGISTER, json = body)
        return result.json(),200

@api.route('/login')
class Login(Resource):
    
    def post(self):
        body = request.get_json(force=True)
        
        result = requests.post(url=URL_AUTH_LOGIN, json = body)
        
        return result.json(),200
  

@api.route('/booking')
class BookingService(Resource):
    def get(self):
        req = requests.get(URL_BOOKING)

        json_req = req.json()

        return json_req,200

    def post(self):
        body = request.get_json(force=True)

        result = requests.post(url=URL_BOOKING, json = body)

        return {result},200


@api.route('/booking/<ticket_id>')
class BookingDeleteService(Resource):
    def delete(self, ticket_id):
        req = requests.delete(url=URL_BOOKING +"/"+ ticket_id)
        
        return req,204



server.run()





