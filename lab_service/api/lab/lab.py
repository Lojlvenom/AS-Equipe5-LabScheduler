from api.model.lab import Lab
from api.lab.database import db

class LabService():

    def addLab(self, name, numberOfComputers):
        lab = Lab(name,numberOfComputers)
        db.add(lab)
        return { "message": "Ok", "result": lab.toDict() }, 200

    def listAllLab(self):
        labs = db.listAll()
        result = []
        for lab in labs:
            result.append(lab.toDict())
        return result, 200
