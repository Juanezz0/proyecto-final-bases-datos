from peewee import *
import datetime

MOTOR_ACTIVO = "sqlite"

if MOTOR_ACTIVO == "sqlite":
    db = SqliteDatabase('adso_steam.db')
elif MOTOR_ACTIVO == "mysql":
    db = MySQLDatabase(
        'nombre_db',
        user='usuario',
        password='password',
        host='localhost',
        port=3306,
        charset='utf8mb4'
    )
elif MOTOR_ACTIVO == "postgres" or MOTOR_ACTIVO == "postgresql":
    db = PostgresqlDatabase(
        'nombre_db',
        user='usuario',
        password='password',
        host='127.0.0.1',
        port=5432
    )
else:
    raise ValueError("Motor de base de datos no válido")



class BaseModel(Model):

    class Meta:
        database = db

class Genero(BaseModel):

    nombre = CharField(
        max_length=50,
        unique=True
    )


class Videojuego(BaseModel):

    nombre = CharField(
        max_length=100,
        unique=True
    )

    precio = DecimalField(
        max_digits=10,
        decimal_places=2,
        constraints=[
            Check('precio >= 0')
        ]
    )

    stock = IntegerField(
        default=0,
        constraints=[
            Check('stock >= 0')
        ]
    )

    genero = ForeignKeyField(
        Genero,
        backref='videojuegos',
        on_delete='CASCADE'
    )


class Usuario(BaseModel):

    nombre = CharField(
        max_length=100
    )

    correo = CharField(
        max_length=100,
        unique=True
    )


class Compra(BaseModel):

    usuario = ForeignKeyField(
        Usuario,
        backref='compras',
        on_delete='CASCADE'
    )

    fecha = DateTimeField(
        default=datetime.datetime.now
    )

    total = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


class DetalleCompra(BaseModel):

    compra = ForeignKeyField(
        Compra,
        backref='detalles',
        on_delete='CASCADE'
    )

    videojuego = ForeignKeyField(
        Videojuego,
        backref='detalles_compra',
        on_delete='CASCADE'
    )

    cantidad = IntegerField(
        constraints=[
            Check('cantidad > 0')
        ]
    )

    precio = DecimalField(
        max_digits=10,
        decimal_places=2,
        constraints=[
            Check('precio >= 0')
        ]
    )

def ejecutar_pruebas():

    db.connect()

    db.create_tables([
        Genero,
        Videojuego,
        Usuario,
        Compra,
        DetalleCompra
    ])

   

    genero, creado = Genero.get_or_create(
    nombre="Plataformas"
)

    genero2, creado = Genero.get_or_create(
    nombre="Acción"
)

    genero3, creado = Genero.get_or_create(
    nombre="RPG"
)

    usuario, creado = Usuario.get_or_create(
    correo="juan@gmail.com",
    defaults={
        'nombre': 'Juan'
    }
)

    usuario2, creado = Usuario.get_or_create(
    correo="jose@gmail.com",
    defaults={
        'nombre': 'Jose'
    }
)

    juego, creado = Videojuego.get_or_create(
    nombre="Super Mario Bros",
    defaults={
        'precio': 59.99,
        'stock': 100,
        'genero': genero
    }
)

    juego2, creado = Videojuego.get_or_create(
    nombre="Minecraft",
    defaults={
        'precio': 89.99,
        'stock': 50,
        'genero': genero2
    }
)

    juego3, creado = Videojuego.get_or_create(
    nombre="The Witcher 3",
    defaults={
        'precio': 79.99,
        'stock': 30,
        'genero': genero3
    }
)

    compra, creado = Compra.get_or_create(
    usuario=usuario,
    defaults={
        'total': 59.99
    }
)

    detalle, creado = DetalleCompra.get_or_create(
    compra=compra,
    videojuego=juego,
    defaults={
        'cantidad': 1,
        'precio': 59.99
    }
)

    db.close()


def operaciones_crud():
    db.connect()
    db.create_tables([
        Genero,
        Videojuego,
        Usuario,
        Compra,
        DetalleCompra
    ], safe=True)

    print("\n# OPERACIONES CRUD")

    # CREATE
    categoria = Genero.get_or_create(nombre="Deportes")[0]
    producto = Videojuego.get_or_create(
        nombre="FIFA 25",
        defaults={
            'precio': 450.00,
            'stock': 20,
            'genero': categoria
        }
    )[0]
    print(f"[CREATE] Registro creado con ID: {producto.id}")

    # READ
    print("[READ] Listando videojuegos:")
    for juego in Videojuego.select().join(Genero):
        print(f"- {juego.nombre} | Precio: ${juego.precio} | Categoría: {juego.genero.nombre}")

    # UPDATE
    producto.precio = 485.00
    producto.save()
    print(f"[UPDATE] Nuevo precio de {producto.nombre}: ${producto.precio}")

    # DELETE
    producto.delete_instance()
    print(f"[DELETE] Producto {producto.nombre} eliminado correctamente.")

    db.close()

if __name__ == '__main__':
    ejecutar_pruebas()
    operaciones_crud()
