from flask import Flask

flaskApp = Flask(__name__)

if __name__ == '__main__':
    from api.task import *
    flaskApp.run(host='127.0.0.1', port=5005, use_reloader=True)