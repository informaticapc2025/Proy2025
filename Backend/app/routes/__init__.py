from app.routes.usuarios import usuarios_bp

def register_routes(app):
    app.register_blueprint(usuarios_bp)
