from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/reservas", tags=["Reservas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear una reserva
@router.post("/", response_model=schemas.Reserva)
def crear_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    # Verificar que el huésped existe
    huesped = db.query(models.Huesped).filter(models.Huesped.id == reserva.huesped_id).first()
    if not huesped:
        raise HTTPException(status_code=404, detail="Huésped no encontrado")
    
    # Verificar que la habitación existe
    habitacion = db.query(models.Habitacion).filter(models.Habitacion.id == reserva.habitacion_id).first()
    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    
    nueva_reserva = models.Reserva(**reserva.dict())
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    return nueva_reserva

# Listar todas las reservas
@router.get("/", response_model=list[schemas.Reserva])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(models.Reserva).all()

# Obtener una reserva por ID
@router.get("/{reserva_id}", response_model=schemas.Reserva)
def obtener_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

# Actualizar reserva
@router.put("/{reserva_id}", response_model=schemas.Reserva)
def actualizar_reserva(reserva_id: int, datos: schemas.ReservaCreate, db: Session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    for key, value in datos.dict().items():
        setattr(reserva, key, value)
    db.commit()
    db.refresh(reserva)
    return reserva

# Eliminar reserva
@router.delete("/{reserva_id}")
def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    db.delete(reserva)
    db.commit()
    return {"mensaje": "Reserva eliminada correctamente"}
