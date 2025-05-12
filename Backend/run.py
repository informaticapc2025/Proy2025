from app import db, create_app
from sqlalchemy import text

app = create_app()

with app.app_context():
    result = db.session.execute(text("SELECT 1"))
    print("✅ Conexión exitosa:", result.scalar())
