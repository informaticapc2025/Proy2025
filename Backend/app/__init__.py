from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Cargar configuración desde tu clase Config
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # ✅ Habilitar CORS solo para el frontend que usas
    CORS(app, origins=["http://localhost:5173"])

    # IMPORTAR Y REGISTRAR BLUEPRINTS
    from app.routes.actividad_routes import actividad_bp
    from app.routes.anuncio_routes import anuncio_bp
    from app.routes.queja_routes import queja_bp
    from app.routes.reconocimiento_routes import reconocimiento_bp
    from app.routes.usuarios import usuarios_bp

    app.register_blueprint(actividad_bp)
    app.register_blueprint(anuncio_bp)
    app.register_blueprint(queja_bp)
    app.register_blueprint(reconocimiento_bp)
    app.register_blueprint(usuarios_bp)

    return app
