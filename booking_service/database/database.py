

#from booking_service.models.booking import Booking


class Database():
    
    def __init__(self):

        self.booking_list = []

    def add_booking(self, booking):
        
        booking.change_id(self.set_booking_id())
        self.booking_list.append(booking)

    def remove_booking(self, data):

        for i in range(len(self.booking_list)):
            if self.booking_list[i].ticket_id == int(data):
                del(self.booking_list[i])
                break
    
    def list_booking_all(self):

            return self.booking_list
    
    def set_booking_id(self):

        if len(self.booking_list) == 0:
            return 1
        else:
            return self.booking_list[-1].ticket_id + 1


    def check_booking(self, c_date, c_shift, c_lab_name):

        for i in range(len(self.booking_list)):
            if self.booking_list[i].date == c_date and self.booking_list[i].shift == c_shift and self.booking_list[i].lab_name == c_lab_name:
                return True
        return False


    # def search_booking(self):

    #     for i in range(len(self.booking_list)):
    #         if (self.booking_list[i].self == self):
    #             return 1



    def list_booking_by(self, data):
        results = []
        for booking in self.booking_list:
            if booking.email == data:
                results.append(booking)
        return results

db = Database()




    
