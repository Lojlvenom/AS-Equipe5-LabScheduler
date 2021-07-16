
class Lab():

    def __init__(self, nome, numberOfComputers):
        self.nome = nome
        self.numberOfComputers = numberOfComputers

    def toDict(self):
        return {
            "name" : self.nome,
            "numberOfComputers" : self.numberOfComputers
        }