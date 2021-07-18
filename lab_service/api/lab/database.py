
from api.model.lab import Lab

class Database():

    def __init__(self):
        self.list = [
            Lab("LAB01",15),
            Lab("LAB02",18),
            Lab("LAB03",23)
        ]

    def listAll(self):
        return self.list

    def add(self,data):
        self.list.append(data)

    def delete(self, data):
        for i in range(len(self.list)):
            if self.list[i].nome == data:
                del(self.list[i])
                break

    def listBy(self, data):
        for i in range(len(self.list)):
            if self.list[i].nome == data:
                return self.list[i]



db = Database()
