-- ============================================
-- Script de Creación de Base de Datos
-- Sistema de Gestión Hotelera - HotelApp
-- ============================================

-- Eliminar tablas si existen (para recrear desde cero)
DROP TABLE IF EXISTS reservas CASCADE;
DROP TABLE IF EXISTS huespedes CASCADE;
DROP TABLE IF EXISTS habitaciones CASCADE;

-- ============================================
-- Tabla: HUESPEDES
-- Descripción: Almacena información de los huéspedes del hotel
-- ============================================
CREATE TABLE huespedes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    CONSTRAINT email_unique UNIQUE (email)
);

-- Índice para búsquedas rápidas por email
CREATE INDEX idx_huespedes_email ON huespedes(email);

-- Comentarios de la tabla
COMMENT ON TABLE huespedes IS 'Registro de huéspedes del hotel';
COMMENT ON COLUMN huespedes.id IS 'Identificador único del huésped';
COMMENT ON COLUMN huespedes.nombre IS 'Nombre completo del huésped';
COMMENT ON COLUMN huespedes.email IS 'Correo electrónico único';
COMMENT ON COLUMN huespedes.telefono IS 'Número de contacto';

-- ============================================
-- Tabla: HABITACIONES
-- Descripción: Catálogo de habitaciones disponibles
-- ============================================
CREATE TABLE habitaciones (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    precio INTEGER NOT NULL,
    CONSTRAINT numero_unique UNIQUE (numero),
    CONSTRAINT precio_positivo CHECK (precio > 0)
);

-- Índice para búsquedas por tipo de habitación
CREATE INDEX idx_habitaciones_tipo ON habitaciones(tipo);

-- Comentarios de la tabla
COMMENT ON TABLE habitaciones IS 'Catálogo de habitaciones del hotel';
COMMENT ON COLUMN habitaciones.id IS 'Identificador único de la habitación';
COMMENT ON COLUMN habitaciones.numero IS 'Número de habitación único';
COMMENT ON COLUMN habitaciones.tipo IS 'Tipo de habitación (Suite, Doble, Individual, etc.)';
COMMENT ON COLUMN habitaciones.precio IS 'Precio por noche en pesos colombianos';

-- ============================================
-- Tabla: RESERVAS
-- Descripción: Gestión de reservas de habitaciones
-- ============================================
CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    huesped_id INTEGER NOT NULL,
    habitacion_id INTEGER NOT NULL,
    fecha_ingreso DATE NOT NULL,
    fecha_salida DATE NOT NULL,
    
    -- Llaves foráneas
    CONSTRAINT fk_huesped 
        FOREIGN KEY (huesped_id) 
        REFERENCES huespedes(id) 
        ON DELETE CASCADE,
    
    CONSTRAINT fk_habitacion 
        FOREIGN KEY (habitacion_id) 
        REFERENCES habitaciones(id) 
        ON DELETE CASCADE,
    
    -- Restricciones de validación
    CONSTRAINT fecha_valida 
        CHECK (fecha_salida > fecha_ingreso)
);

-- Índices para optimizar consultas
CREATE INDEX idx_reservas_huesped ON reservas(huesped_id);
CREATE INDEX idx_reservas_habitacion ON reservas(habitacion_id);
CREATE INDEX idx_reservas_fechas ON reservas(fecha_ingreso, fecha_salida);

-- Comentarios de la tabla
COMMENT ON TABLE reservas IS 'Registro de reservas de habitaciones';
COMMENT ON COLUMN reservas.id IS 'Identificador único de la reserva';
COMMENT ON COLUMN reservas.huesped_id IS 'Referencia al huésped que reserva';
COMMENT ON COLUMN reservas.habitacion_id IS 'Referencia a la habitación reservada';
COMMENT ON COLUMN reservas.fecha_ingreso IS 'Fecha de check-in';
COMMENT ON COLUMN reservas.fecha_salida IS 'Fecha de check-out';

-- ============================================
-- Verificación de creación exitosa
-- ============================================
SELECT 
    'Tabla creada: ' || tablename as status
FROM pg_tables 
WHERE schemaname = 'public' 
    AND tablename IN ('huespedes', 'habitaciones', 'reservas')
ORDER BY tablename;