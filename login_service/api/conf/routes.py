from flask_restful import Api

from api.handles.userHandles import (Register, login, login_test)

def generete_routes(app):
    api = Api(app)
    
    api.add_resource(Register,"/auth/register")
    
    api.add_resource(login,"/auth/login")
    
    api.add_resource(login_test,"/auth/login-test")