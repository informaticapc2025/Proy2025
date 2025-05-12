from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from app.config import Config
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.usuarios import usuarios_bp
    from app.routes.anuncio_routes import anuncio_bp

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(anuncio_bp)

    return app

