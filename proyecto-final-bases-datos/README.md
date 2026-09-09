ADSO STEAM
Integrantes
Juan Esteban Perez (1056774081/juanperez301207@gmail.com)
Jose Daniel Lopez (1018236639/joselopezzabalaw)
Descripción

ADSO STEAM es un sistema de gestión de videojuegos que permite administrar géneros, videojuegos, usuarios y compras.

Contexto del problema

Actualmente, una tienda o plataforma de videojuegos puede manejar información sobre videojuegos, géneros, usuarios y compras. Esta información no se encuentra organizada en una base de datos, puede ser difícil consultar los productos disponibles, controlar el stock, registrar las compras y mantener relacionados los datos.

Por esto, se plantea crear ADSO STEAM, un sistema que permita organizar y administrar esta información mediante una base de datos relacional.

Objetivo general

Desarrollar un sistema de gestión de videojuegos que permita administrar videojuegos, géneros, usuarios y compras mediante una base de datos relacional, utilizando SQL y Python con el ORM Peewee

Entidades
Genero: almacena los géneros de los videojuegos.
Videojuego: almacena información como nombre, precio y stock.
Usuario: registra los usuarios del sistema.
Compra: registra las compras realizadas.
DetalleCompra: relaciona las compras con los videojuegos.
Tecnologías
Python
Peewee
SQLite
SQL
MySQL
PostgreSQL

Instalación

Instalar Peewee:

pip install peewee
Ejecución

Ejecutar el programa con:

python app.py
Estructura
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