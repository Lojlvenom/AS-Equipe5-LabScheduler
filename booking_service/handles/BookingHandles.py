import sys

from flask import g, request
from flask_restful import Resource

import error.errors as error
from database.database import db

from models.booking import Booking
import json

import requests

URL = 'http://localhost:5000/notification'


class BookingList(Resource):
    def __init__(self):
        pass
   
    
    def post(self):


       # try:

            # get 
        date, shift, email, lab_name, title, obs = (
            request.json.get("date").strip(),
            request.json.get("shift").strip(),
            request.json.get("email").strip(),
            request.json.get("lab_name").strip(),
            request.json.get("title").strip(),
            request.json.get("obs").strip()
        )
        
        
            # except Exception as why:

                #Check if Booking information is None
                # if date is None or shift is None or email is None or lab_name is None:
                #     return error.INVALID_INPUT_422
        
        if db.check_booking(date,shift,lab_name):
            return error.ALREADY_EXIST
        
        booking = Booking(date, shift, email, lab_name,title,obs)
        db.add_booking(booking)

        # Chamar Notify
        PARAMS = {
            "reservation_hash": booking.ticket_id,
            "title": booking.title,
            "spaces": booking.lab_name,
            "date_time": booking.date + " - " + booking.shift,
            "email_list": [booking.email],
            "obs": booking.obs
            }
        
        result = requests.post(url=URL, json=PARAMS)

        return {"booking": booking.toDict(),
                "notification": result.json()},200

    def get(self):
        bookings = db.list_booking_all()
        results = []

        for booking in bookings:
            results.append(booking.toDict())
        
        return results, 200

class BookingDelList(Resource):
    def __init__(self):
        pass

    def delete(self, data):
        
        db.remove_booking(data)

        return '', 204
    
    def get(self, data):
        by = db.list_booking_by(data)
        result = []
        for bookings in by:
            result.append(bookings.toDict())
        return result,200