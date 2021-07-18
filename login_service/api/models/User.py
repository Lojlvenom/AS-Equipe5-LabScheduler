from api.conf.auth import auth,jwt
from flask import g

class User():
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        
# Generates auth token.
    def generate_auth_token(self):
            token = jwt.dumps({"email": self.email})

            # Return admin flag.
            return token

    # Generates a new access token from refresh token.
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):

        # Create a global none user.
        g.user = None

        try:
            # Load token.
            data = jwt.loads(token)

        except Exception:
            # If any error return false.
            return False

        # Check if email and admin permission variables are in jwt.
        if "email" in data:

            # Set email from jwt.
            g.user = data["email"]

            return True

        return False