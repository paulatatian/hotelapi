from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/habitaciones", tags=["Habitaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Habitacion)
def crear_habitacion(habitacion: schemas.HabitacionCreate, db: Session = Depends(get_db)):
    nueva = models.Habitacion(**habitacion.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=list[schemas.Habitacion])
def listar_habitaciones(db: Session = Depends(get_db)):
    return db.query(models.Habitacion).all()
