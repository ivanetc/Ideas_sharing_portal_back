# -*- coding: utf-8 -*-
import json

from flask import Flask, current_app
from pymorphy2 import MorphAnalyzer

from pluto_ideas_api.Classes.User import User

"""Initialize Flask app."""


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from pluto_ideas_api.API.User import GetUser
        from pluto_ideas_api.API.Idea import GetRelevantIdea
        # Register Data
        current_app.current_user = User(
            1,
            "Алекандр",
            "Сергеевич",
            "Иванец",
            "картинка",
            "Ярославль",
            "Управление трехмерного моделирование",
            ".net разработчик",
            "89052668317",
            "ivanetcas@polymetal.ru",
            ["Ачивка 1", "Ачивка 2", ],
        )
        with open('data\\data.json', encoding='UTF-8') as file:
            current_app.ideas = json.load(file)
        current_app.predictor = MorphAnalyzer()

        # Register Blueprints
        app.register_blueprint(GetUser.user_getuser_bp)
        app.register_blueprint(GetRelevantIdea.idea_getrelevantideas_bp)
        return app


if __name__ == "__main__":
    app = create_app()
    app.run()
