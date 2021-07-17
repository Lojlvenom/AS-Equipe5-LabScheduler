import sys
import error.errors as error
import database.database as db


class Register(Resource):
    @staticmethod
    def post():

        try:
            # get 
            username, labname, date, shift = (
                request.json.get("username").strip(),
                request.json.get("labname").strip(),
                request.json.get("date").strip(),
                request.json.get("shift").strip()
            )

            except Exception as why:

            # Check if Booking information is None
            if username is None or labname is None or date is None or shift is None:
                return error.INVALID_INPUT_422

            # Get booking if its free
            booking = db.filterby(labname=labname, date=date, shift=shift).first()

            # Check booking if its free
            if booking is not None:
                return error.ALREADY_EXIST

            booking = Booking(ticket_id=ticket_id, date=date, shift=shift)

            db.add_booking(booking)

            return {"status": "registration completed."}
