class Booking():
    def __init__(self, date, shift, email, lab_name):
        self.ticket_id = 0
        self.date = date
        self.shift = shift
        self.email= email
        self.lab_name = lab_name

    def toDict(self):
        return {
            "ticket_id" : self.ticket_id,
            "date": self.date,
            "shift": self.shift,
            "email": self.email,
            "lab_name": self.lab_name
        }

    def change_id(self, ticket_id):
        self.ticket_id = ticket_id