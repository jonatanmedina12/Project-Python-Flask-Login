from flask import Flask,render_template
from .Controller import auth_vista


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='Dev'
    )

    # Registrar Blueprint
    app.register_blueprint(auth_vista.bp)

    @app.route("/")
    def index():
        return render_template('index.html')

    return app
