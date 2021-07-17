from flask_restful import Resource
from flask import request
import json

from api.lab.lab import LabService

class taskLab(Resource):

    def __init__(self):
       pass

    def put(self):

        return { "message": "Error", "result": "PUT method not implemented" }, 500

    def delete(self, name):
        lab = LabService()
        result = lab.removeLab(name)
        return result

class taskLabList(Resource):

    def __init__(self):
       pass

    def get(self):
        lab = LabService()
        result = lab.listAllLab()
        return result

    def post(self):
        rec = request.get_json(force=True)

        name = rec['name']
        numberOfComputers = rec['numberOfComputers']

        lab = LabService()
        result = lab.addLab(name, numberOfComputers)
        del lab

        return result
    


