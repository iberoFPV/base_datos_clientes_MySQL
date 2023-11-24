import os  # Se utiliza para acceder a las variables

from flask import Flask  # Importamos Flask


# Funcion para trabajar por varias instancias
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        # Configuración
        SECRET_KEY="mikey",  # Cambiar mikey cuando deployamos un proyecto real para complicarle la vida a los hack
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE=os.environ.get("FLASK_DATABASE"),
    )

    from . import db

    db.init_app(app)

    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route("/hola")
    def hola():
        return "Chanchito Feliz"

    return app
