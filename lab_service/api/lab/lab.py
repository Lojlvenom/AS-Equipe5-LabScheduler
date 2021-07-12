from api.lab.database import client as cl

class LabService():

    def addLab(self, name, numberOfComputers):
        data = {
            'name': name,
            'numberOfComputers': numberOfComputers,
        }

        doc_ref = cl.collection('labs').add(data)
        return { "message": "Ok", "result": data }, 200

    def listAllLab(self):
        docs = cl.collection('labs').stream()
        result = []
        for doc in docs:
            result.append(u'{}: {}'.format(doc.id, doc.to_dict()))
        return result
