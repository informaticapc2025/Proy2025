from app import db, create_app
from sqlalchemy import inspect, text

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # Probar conexión
        result = db.session.execute(text("SELECT 1"))
        print("✅ Conexión exitosa:", result.scalar())

        # Crear tablas
        db.create_all()
        print("✅ Tablas creadas correctamente")

        # Mostrar tablas existentes
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print("📋 Tablas en la base de datos:", tables)

        # Listar rutas:
        for rule in app.url_map.iter_rules():
            print("📌 Ruta disponible:", rule)

    app.run(debug=False, port=5000)
