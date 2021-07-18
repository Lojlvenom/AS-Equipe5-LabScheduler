import sys

from flask import g, request
from flask_restful import Resource

import error.errors as error
from database.database import db

from models.test import Booking
import json


class BookingList(Resource):
    def __init__(self):
        pass
   
    
    def post(self):


       # try:

            # get 
        date, shift, email, lab_name = (
            request.json.get("date").strip(),
            request.json.get("shift").strip(),
            request.json.get("email").strip(),
            request.json.get("lab_name").strip()
        )

            # except Exception as why:

                #Check if Booking information is None
                # if date is None or shift is None or email is None or lab_name is None:
                #     return error.INVALID_INPUT_422

        test= Booking(date, shift, email, lab_name)
       # booking = Booking("1", "noy", "e@", "namw")

        db.add_booking(test)

        return test.toDict(),200

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