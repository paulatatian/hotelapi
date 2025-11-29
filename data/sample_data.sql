-- ============================================
-- Script de Datos de Prueba
-- Sistema de Gestión Hotelera - HotelApp
-- ============================================

-- Limpiar datos existentes
TRUNCATE TABLE reservas CASCADE;
TRUNCATE TABLE huespedes RESTART IDENTITY CASCADE;
TRUNCATE TABLE habitaciones RESTART IDENTITY CASCADE;

-- ============================================
-- INSERCIÓN DE HUÉSPEDES
-- ============================================

INSERT INTO huespedes (nombre, email, telefono) VALUES
('Carlos Rodríguez', 'carlos.rodriguez@email.com', '3001234567'),
('María González', 'maria.gonzalez@email.com', '3009876543'),
('Juan Pérez', 'juan.perez@email.com', '3105551234'),
('Ana Martínez', 'ana.martinez@email.com', '3157778888'),
('Luis Fernández', 'luis.fernandez@email.com', '3209991111'),
('Sofia López', 'sofia.lopez@email.com', '3143332222'),
('Diego Ramírez', 'diego.ramirez@email.com', '3186664444'),
('Laura Sánchez', 'laura.sanchez@email.com', '3125557777'),
('Pedro Castro', 'pedro.castro@email.com', '3168889999'),
('Valentina Torres', 'valentina.torres@email.com', '3194443333');

-- ============================================
-- INSERCIÓN DE HABITACIONES
-- ============================================

INSERT INTO habitaciones (numero, tipo, precio) VALUES
-- Suites Premium
('101', 'Suite Presidencial', 500000),
('102', 'Suite Junior', 350000),
('103', 'Suite Ejecutiva', 400000),

-- Habitaciones Dobles
('201', 'Doble Standard', 200000),
('202', 'Doble Confort', 250000),
('203', 'Doble Deluxe', 280000),
('204', 'Doble Vista Mar', 320000),

-- Habitaciones Individuales
('301', 'Individual Standard', 150000),
('302', 'Individual Confort', 180000),
('303', 'Individual Business', 200000),

-- Habitaciones Familiares
('401', 'Familiar 4 Personas', 380000),
('402', 'Familiar 6 Personas', 450000);

-- ============================================
-- INSERCIÓN DE RESERVAS
-- ============================================

INSERT INTO reservas (huesped_id, habitacion_id, fecha_ingreso, fecha_salida) VALUES
-- Reservas activas (diciembre 2024 - enero 2025)
(1, 1, '2024-12-01', '2024-12-05'),  -- Carlos en Suite Presidencial
(2, 4, '2024-12-10', '2024-12-15'),  -- María en Doble Standard
(3, 8, '2024-12-15', '2024-12-18'),  -- Juan en Individual Standard
(4, 11, '2024-12-20', '2024-12-27'), -- Ana en Familiar 4P
(5, 2, '2024-12-28', '2025-01-03'),  -- Luis en Suite Junior

-- Reservas futuras (enero-febrero 2025)
(6, 7, '2025-01-05', '2025-01-12'),  -- Sofia en Doble Vista Mar
(7, 3, '2025-01-10', '2025-01-15'),  -- Diego en Suite Ejecutiva
(8, 9, '2025-01-15', '2025-01-20'),  -- Laura en Individual Confort
(9, 12, '2025-01-25', '2025-02-01'), -- Pedro en Familiar 6P
(10, 5, '2025-02-01', '2025-02-07'), -- Valentina en Doble Confort

-- Reservas históricas (noviembre 2024)
(1, 4, '2024-11-01', '2024-11-05'),
(3, 8, '2024-11-10', '2024-11-12'),
(5, 2, '2024-11-15', '2024-11-20');

-- ============================================
-- VERIFICACIÓN DE DATOS INSERTADOS
-- ============================================

-- Contar registros por tabla
SELECT 'Huéspedes' as tabla, COUNT(*) as total FROM huespedes
UNION ALL
SELECT 'Habitaciones' as tabla, COUNT(*) as total FROM habitaciones
UNION ALL
SELECT 'Reservas' as tabla, COUNT(*) as total FROM reservas;

-- Mostrar resumen de reservas
SELECT 
    h.nombre as huesped,
    hab.numero as habitacion,
    hab.tipo as tipo_habitacion,
    r.fecha_ingreso,
    r.fecha_salida,
    hab.precio as precio_noche
FROM reservas r
JOIN huespedes h ON r.huesped_id = h.id
JOIN habitaciones hab ON r.habitacion_id = hab.id
ORDER BY r.fecha_ingreso DESC
LIMIT 5;