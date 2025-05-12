import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:info2025@localhost:5432/ResiHub")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
