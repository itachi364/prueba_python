from flask import Flask
from flasgger import Swagger
from .controllers import user_blueprint

def create_app():
    app = Flask(__name__)

    # Configuración de Flasgger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/"
    }

    swagger_template = {
        "info": {
            "title": "User Management API",
            "description": "API for managing users",
            "version": "1.0.0"
        },
        "basePath": "/api"
    }

    # Inicializar Flasgger con la aplicación Flask
    Swagger(app, config=swagger_config, template=swagger_template)

    # Registrar el blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    return app