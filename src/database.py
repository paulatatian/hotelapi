import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Usar variable de entorno si existe, sino usar valor por defecto
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1940@localhost:5432/hotel_db"
)

# Crear engine de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para modelos
Base = declarative_base()

# Función helper para obtener la sesión de base de datos
def get_db():
    """
    Generador que proporciona una sesión de base de datos.
    Se usa como dependencia en los endpoints de FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()