from flask_restful import Resource
from flask import request
import json

from api.lab.lab import LabService

class taskLab(Resource):

    def __init__(self):
       pass

    def get(self, name):
        lab = LabService()
        result = lab.listLab(name)
        del lab
        return result

    def delete(self, name):
        lab = LabService()
        result = lab.removeLab(name)
        del lab
        return result

class taskLabList(Resource):

    def __init__(self):
       pass

    def get(self):
        lab = LabService()
        result = lab.listAllLab()
        del lab
        return result

    def post(self):
        rec = request.get_json(force=True)

        name = rec['name']
        numberOfComputers = rec['numberOfComputers']

        lab = LabService()
        result = lab.addLab(name, numberOfComputers)
        del lab

        return result
    


