class Booking():
    def __init__(self, date, shift, email, lab_name,title="",obs=""):
        self.ticket_id = 0
        self.title = title
        self.date = date
        self.shift = shift
        self.email= email 
        self.lab_name = lab_name
        self.obs = obs

    def toDict(self):
        return {
            "title": self.title,
            "ticket_id" : self.ticket_id,
            "date": self.date,
            "shift": self.shift,
            "email": self.email,
            "lab_name": self.lab_name,
            "obs": self.obs
        }

    def change_id(self, ticket_id):
        self.ticket_id = ticket_id