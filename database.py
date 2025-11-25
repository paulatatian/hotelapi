import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Usar variable de entorno si existe, sino usar valor por defecto
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1940@localhost:5432/hotel_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()