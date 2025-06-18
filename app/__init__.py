from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()  # Cargar variables de .env

    app = Flask(__name__)

    # Cargar config desde config.py
    app.config.from_object("config.Config")

    # Inicializar base de datos
    db.init_app(app)

    # Registrar rutas
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
