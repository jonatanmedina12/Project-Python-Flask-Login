from flask import Flask, render_template
from .Controller import auth_vista
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='Dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///Tareas.db"
    )

    db.init_app(app)

    with app.app_context():
        from .Models import modelo  # Importar modelos dentro del contexto de la aplicación
        db.create_all()  # Crear todas las tablas definidas en los modelos

    # Registrar Blueprint
    app.register_blueprint(auth_vista.bp)

    @app.route("/")
    def index():

        return render_template('index.html')


    return app
