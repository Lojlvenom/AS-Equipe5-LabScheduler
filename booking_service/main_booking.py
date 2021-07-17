import sys
from database.database import Database
from models.booking import Booking


if __name__ == '__main__':
    db = Database()
    booking = Booking(1, "17/07", "noite", "Lab 3")
    db.add_booking(booking)

    booking2 = Booking(2,"18/07","matutino","Lab 3")
    db.add_booking(booking2)

    booking3 = Booking(3,"18/07","matutino","Lab 3")
    db.add_booking(booking3)

    for i in range(len(db.booking_list)):
        print(db.booking_list[i])

    db.remove_booking(booking2)
    for i in range(len(db.booking_list)):
        print(db.booking_list[i])