from config.routes import generate_routes
import sys
from database.database import Database
from models.booking import Booking
from flask import Flask



def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True

    generate_routes(app)

    return app




if __name__ == '__main__':

    app = create_app()

    app.run(port=5008, debug=True, host='localhost', use_reloader=True)






    # db = Database()
    # booking = Booking(1, "17/07", "noite", "email1", "Lab 3")
    # db.add_booking(booking)

    # booking2 = Booking(2,"18/07","matutino","email2","Lab 3")
    # db.add_booking(booking2)

    # booking3 = Booking(3,"18/07","matutino","email3","Lab 3")
    # db.add_booking(booking3)

    # booking4 = Booking(4,"19/07","matutino","email3","Lab 3")
    # db.add_booking(booking4)

    # for i in range(len(db.booking_list)):
    #     print(db.booking_list[i])

    # db.remove_booking(2)
    # for i in range(len(db.booking_list)):
    #     print(db.booking_list[i])

    