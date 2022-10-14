from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movie_ns
from views.director import director_ns
from views.genre import genre_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)

    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == "__main__":
    app = create_app(Config())

    configure_app(app)

    app.run()
