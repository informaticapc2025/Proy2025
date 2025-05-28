from .usuarios import usuarios_bp
from .anuncio_routes import anuncio_bp
from .reconocimiento_routes import reconocimiento_bp

def register_routes(app):
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(anuncio_bp)
    app.register_blueprint(reconocimiento_bp)
