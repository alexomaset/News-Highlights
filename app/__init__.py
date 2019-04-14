from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    """
    Intializing the app
    Function that takes configuration setting key as an argument
    Args:
        config_name: name of configuration used
    """
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    # Registering the BluePrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

       # setting the config
    from .request import configure_request
    configure_request(app)

    return app