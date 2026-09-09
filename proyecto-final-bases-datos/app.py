from peewee import *
import datetime

db = SqliteDatabase('adso_steam.db')



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

    print("========================================")
    print(" CONECTADO A SQLITE - ADSO STEAM")
    print("========================================")

    genero, creado = Genero.get_or_create(
        nombre="Plataformas"
    )

    juego, creado = Videojuego.get_or_create(
        nombre="Super Mario Bros",
        defaults={
            'precio': 59.99,
            'stock': 100,
            'genero': genero
        }
    )

    print("\n[CREATE]")
    print("Videojuego creado/verificado correctamente.")
    print(f"Nombre: {juego.nombre}")

    print("\n[READ]")
    print("Videojuegos registrados:")
    for juego in Videojuego.select():
         print(
            f"ID: {juego.id} | "
            f"Nombre: {juego.nombre} | "
            f"Precio: ${juego.precio} | "
            f"Stock: {juego.stock}"
        )

    print("\n[JOIN]")
    print("Videojuegos y sus géneros:")

    consulta = (
        Videojuego
        .select(Videojuego, Genero)
        .join(Genero)
    )

    for juego in consulta:

        print(
            f"{juego.nombre} → "
            f"{juego.genero.nombre}"
        )

    juego_update = Videojuego.get(
        Videojuego.nombre == "Super Mario Bros"
    )

    juego_update.precio = 49.99
    juego_update.save()

    print("\n[UPDATE]")
    print(
        f"Nuevo precio de {juego_update.nombre}: "
        f"${juego_update.precio}"
    )

    juego_delete = Videojuego.get(
        Videojuego.nombre == "Super Mario Bros"
    )

    juego_delete.delete_instance()

    genero_delete = Genero.get(
        Genero.nombre == "Plataformas"
    )

    genero_delete.delete_instance()

    print("\n[DELETE]")
    print(
        "Videojuego y género eliminados correctamente."
    )


    print("\n========================================")
    print(" PRUEBAS CRUD FINALIZADAS")
    print("========================================")

    db.close()

if __name__ == '__main__':
    ejecutar_pruebas()