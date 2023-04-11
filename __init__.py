from flask import Flask

def create_app():
    app = Flask(__name__)

    from .analyzer import analyzer as analyzer_blueprint
    app.register_blueprint(analyzer_blueprint)

    return app
