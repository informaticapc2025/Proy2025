def register_routes(app):
    from app.routes.usuarios import usuarios_bp
    from app.routes.anuncio_routes import anuncio_bp
    from app.routes.reconocimiento_routes import reconocimiento_bp
    from app.routes.queja_routes import queja_bp  
    from app.routes.actividad_routes import actividad_bp

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(anuncio_bp)
    app.register_blueprint(reconocimiento_bp)
    app.register_blueprint(queja_bp)
    app.register_blueprint(actividad_bp)