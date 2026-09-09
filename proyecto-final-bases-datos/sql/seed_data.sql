-- seed_data.sql
-- Inserción de datos de prueba (compatible en la medida de lo posible con SQLite, MySQL, PostgreSQL)

-- 1. Insertar Géneros (Mínimo 5)
INSERT INTO Genero (nombre) VALUES ('Acción');
INSERT INTO Genero (nombre) VALUES ('RPG');
INSERT INTO Genero (nombre) VALUES ('Deportes');
INSERT INTO Genero (nombre) VALUES ('Terror');
INSERT INTO Genero (nombre) VALUES ('Aventura');

-- 2. Insertar Videojuegos (Mínimo 5)
-- Asumiendo los IDs 1 a 5 para los géneros creados arriba
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('GTA V', 29.99, 150, 1);
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('Minecraft', 19.99, 500, 5);
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('Resident Evil 4', 39.99, 80, 4);
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('The Witcher 3', 25.00, 120, 2);
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('EA Sports FC 24', 59.99, 200, 3);
INSERT INTO Videojuego (nombre, precio, stock, genero_id) VALUES ('Cyberpunk 2077', 49.99, 100, 2);

-- 3. Insertar Usuarios (Mínimo 5)
INSERT INTO Usuario (nombre, correo) VALUES ('Juan Perez', 'juan@example.com');
INSERT INTO Usuario (nombre, correo) VALUES ('Maria Gomez', 'maria@example.com');
INSERT INTO Usuario (nombre, correo) VALUES ('Carlos Ruiz', 'carlos@example.com');
INSERT INTO Usuario (nombre, correo) VALUES ('Ana Torres', 'ana@example.com');
INSERT INTO Usuario (nombre, correo) VALUES ('Luis Fernandez', 'luis@example.com');

-- 4. Insertar Compras (Mínimo 5)
INSERT INTO Compra (usuario_id, total) VALUES (1, 29.99);
INSERT INTO Compra (usuario_id, total) VALUES (2, 59.98);
INSERT INTO Compra (usuario_id, total) VALUES (3, 19.99);
INSERT INTO Compra (usuario_id, total) VALUES (4, 84.99);
INSERT INTO Compra (usuario_id, total) VALUES (5, 25.00);

-- 5. Insertar Detalles de Compra (Mínimo 5)
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (1, 1, 1, 29.99);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (2, 2, 1, 19.99);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (2, 3, 1, 39.99);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (3, 2, 1, 19.99);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (4, 4, 1, 25.00);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (4, 5, 1, 59.99);
INSERT INTO DetalleCompra (compra_id, videojuego_id, cantidad, precio) VALUES (5, 4, 1, 25.00);

-- ==========================================
-- CONSULTA DE PRUEBA (JOIN)
-- ==========================================
-- Mostrar Videojuego + Género
SELECT 
    v.nombre AS Videojuego, 
    v.precio AS Precio, 
    g.nombre AS Genero 
FROM 
    Videojuego v
JOIN 
    Genero g ON v.genero_id = g.id;
