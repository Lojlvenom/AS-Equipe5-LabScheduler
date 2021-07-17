

#from booking_service.models.booking import Booking


class Database():
    
    def __init__(self):

        self.booking_list = []

    def add_booking(self, booking):

        self.booking_list.append(booking)

    def remove_booking(self, ticket_id):

        for i in range(len(self.booking_list)):
            if self.booking_list[i].ticket_id == ticket_id:
                del(self.booking_list[i])
                break
    
    def list_booking_all(self):

            return self.booking_list
    
    # def search_booking(self):

    #     for i in range(len(self.booking_list)):
    #         if (self.booking_list[i].self == self):
    #             return 1



    # def list_booking_by(self, email):

    #     x = filter(self.booking_list, self.booking_list.email)
    #     for i in x:
    #         print(i)


db = Database()




    
