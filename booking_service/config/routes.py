from flask_restful import Api

from handles.BookingHandles import (BookingList, BookingDelList)

def generate_routes(app):

    api = Api(app)

    api.add_resource(BookingList, "/api/booking")
    api.add_resource(BookingDelList, "/api/booking/<data>")
