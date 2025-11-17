from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/huespedes", tags=["Huespedes"])

# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo huésped
@router.post("/", response_model=schemas.Huesped)
def crear_huesped(huesped: schemas.HuespedCreate, db: Session = Depends(get_db)):
    nuevo = models.Huesped(**huesped.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar todos los huéspedes
@router.get("/", response_model=list[schemas.Huesped])
def listar_huespedes(db: Session = Depends(get_db)):
    return db.query(models.Huesped).all()

# Obtener un huésped por ID
@router.get("/{huesped_id}", response_model=schemas.Huesped)
def obtener_huesped(huesped_id: int, db: Session = Depends(get_db)):
    huesped = db.query(models.Huesped).filter(models.Huesped.id == huesped_id).first()
    if not huesped:
        raise HTTPException(status_code=404, detail="Huésped no encontrado")
    return huesped

# Actualizar un huésped
@router.put("/{huesped_id}", response_model=schemas.Huesped)
def actualizar_huesped(huesped_id: int, datos: schemas.HuespedCreate, db: Session = Depends(get_db)):
    huesped = db.query(models.Huesped).filter(models.Huesped.id == huesped_id).first()
    if not huesped:
        raise HTTPException(status_code=404, detail="Huésped no encontrado")
    for key, value in datos.dict().items():
        setattr(huesped, key, value)
    db.commit()
    db.refresh(huesped)
    return huesped

# Eliminar un huésped
@router.delete("/{huesped_id}")
def eliminar_huesped(huesped_id: int, db: Session = Depends(get_db)):
    huesped = db.query(models.Huesped).filter(models.Huesped.id == huesped_id).first()
    if not huesped:
        raise HTTPException(status_code=404, detail="Huésped no encontrado")
    db.delete(huesped)
    db.commit()
    return {"mensaje": "Huésped eliminado correctamente"}
