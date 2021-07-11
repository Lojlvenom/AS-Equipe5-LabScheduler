from api.lab.database import client as cl

class LabService():

    def addLab(self, name, numberOfComputers):
        data = {
            'name': name,
            'numberOfComputers': numberOfComputers,
        }

        doc_ref = cl.collection('labs').add(data)
        return { "message": "Ok", "result": data }, 200