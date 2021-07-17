

class Booking():
    def __init__(self, ticket_id, date, shift, lab_name):
        
        self.ticket_id = ticket_id
        
        self.date = date

        self.shift = shift

        #self.username = username
        
        self.lab_name = lab_name

    def __repr__(self):
        return "<Booking(ticket_id='%s', date='%s', shift='%s, lab_name='%s)>" % (
            self.ticket_id,
            self.date,
            self.shift,
            self.lab_name
        )
