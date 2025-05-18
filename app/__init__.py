from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)

    from .routes import main  			# <--- import your blueprint
    app.register_blueprint(main)  		# <--- register your blueprint

    return app
