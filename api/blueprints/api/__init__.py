from flask_smorest import Api

from .habitat import bp as habi_bp

api = Api()

def init_app(app):
    app.config["API_TITLE"] = "Habitat API"
    app.config["API_VERSION"] = "v0.0.1"
    app.config["OPENAPI_VERSION"] = "3.0.2"

    api.init_app(app)
    api.register_blueprint(habi_bp, url_prefix="/api/")
    