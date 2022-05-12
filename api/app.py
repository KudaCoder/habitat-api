from flask import Flask

from api.config import Config
from api import blueprints, models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    models.init_app(app)
    blueprints.api.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
    )
