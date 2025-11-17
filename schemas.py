from pydantic import BaseModel
from datetime import date

# Huesped
class HuespedBase(BaseModel):
    nombre: str
    email: str
    telefono: str

class HuespedCreate(HuespedBase):
    pass

class Huesped(HuespedBase):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2

# Habitacion
class HabitacionBase(BaseModel):
    numero: str
    tipo: str
    precio: int

class HabitacionCreate(HabitacionBase):
    pass

class Habitacion(HabitacionBase):
    id: int
    class Config:
        from_attributes = True

# Reserva
class ReservaBase(BaseModel):
    huesped_id: int
    habitacion_id: int
    fecha_ingreso: date
    fecha_salida: date

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int
    class Config:
        from_attributes = True
