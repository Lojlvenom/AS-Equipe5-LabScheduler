from config.routes import generate_routes
import sys
from database.database import Database

from flask import Flask



def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True

    generate_routes(app)

    return app


if __name__ == '__main__':

    app = create_app()

    app.run(port=5008, debug=True, host='localhost', use_reloader=True)



    