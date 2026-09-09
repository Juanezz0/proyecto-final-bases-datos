# ADSO STEAM

Sistema de gestión para tiendas de videojuegos diseñado para centralizar la administración de catálogo, inventario, usuarios y transacciones comerciales mediante una base de datos relacional.

---

## Integrantes

| Nombre | Documento | Correo Electrónico |
| :--- | :--- | :--- |
| **Juan Esteban Perez** | 1056774081 | `juanperez301207@gmail.com` |
| **Jose Daniel Lopez** | 1018236639 | `joselopezzabalaw` |

---

## Descripción del Proyecto

ADSO STEAM es una aplicación backend que modela la lógica transaccional de una plataforma de videojuegos. Permite estructurar relaciones críticas entre usuarios, órdenes de compra y control de inventario de títulos disponibles.

### Contexto del Problema
Muchas tiendas digitales operan sin una arquitectura de datos relacional sólida, lo que genera inconsistencias al consultar disponibilidad de productos, controlar stock en tiempo real y auditar compras históricas. ADSO STEAM resuelve esta dispersión centralizando la integridad referencial y las operaciones CRUD a través de una base de datos normalizada.

### Objetivo General
Desarrollar un sistema de gestión de videojuegos que permita administrar títulos, categorías, usuarios y compras mediante una base de datos relacional, utilizando **SQL** y **Python** con el ORM **Peewee**.

---

## Modelo de Datos

* **Genero:** Clasificación temática y categorías de los videojuegos.
* **Videojuego:** Catálogo de productos (nombre, precio unitario y stock disponible).
* **Usuario:** Perfiles de clientes registrados en el sistema.
* **Compra:** Encabezado de transacciones con fecha, estado y referencia de usuario.
* **DetalleCompra:** Tabla asociativa que vincula cada compra con los videojuegos adquiridos, cantidades y subtotales.

---

## Tecnologías Utilizadas

* **Lenguaje:** Python
* **ORM:** Peewee
* **Motores de Bases de Datos:**
  * SQLite *(desarrollo local / prototipado rápido)*
  * MySQL
  * PostgreSQL
* **Lenguaje de Consultas:** SQL estándar

---

## Estructura del Directorio

```text
proyecto-final-bases-datos/
├── README.md
├── app.py
├── sql/
│   ├── schema_sqlite.sql
│   ├── schema_mysql.sql
│   ├── schema_postgres.sql
│   └── seed_data.sql
├── docs/
│   └── der.png
└── evidencias/
