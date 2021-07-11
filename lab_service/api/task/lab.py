from flask_restful import Resource
from flask import request
import json

from api.lab.lab import LabService

class taskLab(Resource):

    def __init__(self):
       pass

    def get(self):

        return { "message": "Error", "result": "GET method not implemented" }, 500

    def put(self):

        return { "message": "Error", "result": "PUT method not implemented" }, 500

    def post(self):
        rec = request.get_json(force=True)

        name = rec['name']
        numberOfComputers = rec['numberOfComputers']

        lab = LabService()
        result = lab.addLab(name, numberOfComputers)
        del lab

        return result
        return { "message": "Error", "result": "POST method not implemented" }, 500

    def delete(self):
        return { "message": "Error", "result": "DELETE method not implemented" }, 500