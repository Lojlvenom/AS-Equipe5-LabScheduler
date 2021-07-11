from flask_restful import Api
from mainLab import flaskApp
from api.task.lab import taskLab

restServer = Api(flaskApp)

restServer.add_resource(taskLab, "/api/lab")