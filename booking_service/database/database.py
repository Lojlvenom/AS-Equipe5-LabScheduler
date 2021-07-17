

#from booking_service.models.booking import Booking


class Database():
    def __init__(self):

        self.booking_list = []

    def add_booking(self, booking):

        self.booking_list.append(booking)

    def remove_booking(self, booking):

        
        self.booking_list.remove(booking)

   # def search_booking(self,booking):



    
