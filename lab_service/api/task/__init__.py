from flask_restful import Api
from mainLab import flaskApp
from api.task.lab import *

restServer = Api(flaskApp)

restServer.add_resource(taskLab, "/api/lab/<name>")
restServer.add_resource(taskLabList, "/api/lab")
