
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


db = Database()

# client.collection('labs').add({
#     'name': "LAB01",
#     'numberOfComputers': 15,
# })