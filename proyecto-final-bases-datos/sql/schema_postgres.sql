-- schema_postgres.sql
-- Motor: PostgreSQL

DROP TABLE IF EXISTS DetalleCompra CASCADE;
DROP TABLE IF EXISTS Compra CASCADE;
DROP TABLE IF EXISTS Usuario CASCADE;
DROP TABLE IF EXISTS Videojuego CASCADE;
DROP TABLE IF EXISTS Genero CASCADE;

CREATE TABLE Genero (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Videojuego (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL UNIQUE,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0),
    genero_id INTEGER NOT NULL,
    FOREIGN KEY (genero_id) REFERENCES Genero(id)
);

CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Compra (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);

CREATE TABLE DetalleCompra (
    id SERIAL PRIMARY KEY,
    compra_id INTEGER NOT NULL,
    videojuego_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    FOREIGN KEY (compra_id) REFERENCES Compra(id),
    FOREIGN KEY (videojuego_id) REFERENCES Videojuego(id)
);
