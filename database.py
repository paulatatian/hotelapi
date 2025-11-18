
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia postgres:tu_contraseña@localhost:5432/hotel_db según tu usuario, contraseña y DB
DATABASE_URL = "postgresql://postgres:1940@localhost:5432/hotel_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
