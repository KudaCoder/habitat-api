from flask import Flask

from . import blueprints, models
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    models.init_app(app)

    app.register_blueprint(blueprints.api.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
