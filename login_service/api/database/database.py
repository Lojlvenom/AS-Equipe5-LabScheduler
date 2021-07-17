from models.User import User


class Database():
    def __init__(self):
        self.list = []


    def add_user(self,data):
        self.list.append(data)
