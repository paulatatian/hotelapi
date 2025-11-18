from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Huesped(Base):
    __tablename__ = "huespedes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String)

    reservas = relationship("Reserva", back_populates="huesped")

class Habitacion(Base):
    __tablename__ = "habitaciones"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    precio = Column(Integer, nullable=False)

    reservas = relationship("Reserva", back_populates="habitacion")

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    huesped_id = Column(Integer, ForeignKey("huespedes.id"))
    habitacion_id = Column(Integer, ForeignKey("habitaciones.id"))
    fecha_ingreso = Column(Date, nullable=False)
    fecha_salida = Column(Date, nullable=False)

    huesped = relationship("Huesped", back_populates="reservas")
    habitacion = relationship("Habitacion", back_populates="reservas")
