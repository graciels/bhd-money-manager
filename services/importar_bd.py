from database.database import conectar
from categorias.clasificador import clasificar


def guardar_cuenta(cuenta, titular):

    conexion = conectar()

    cursor = conexion.cursor()

    # Buscar si la cuenta ya existe
    cursor.execute(
        """
        SELECT id
        FROM cuentas
        WHERE numero = ?
        """,
        (cuenta.numero,),
    )

    fila = cursor.fetchone()

    if fila:

        conexion.close()

        return fila["id"]

    # Si no existe, crearla
    cursor.execute(
        """
        INSERT INTO cuentas (

            numero,

            moneda,

            titular

        )
        VALUES (?, ?, ?)
        """,
        (
            cuenta.numero,
            cuenta.moneda,
            titular,
        ),
    )

    cuenta_id = cursor.lastrowid

    conexion.commit()

    conexion.close()

    return cuenta_id

def guardar_movimientos(cuenta_id, movimientos):

    conexion = conectar()

    cursor = conexion.cursor()

    datos = []

    for movimiento in movimientos:

        datos.append(
    (
        cuenta_id,
        movimiento.fecha.isoformat(),
        movimiento.descripcion,
        movimiento.comercio,
        movimiento.debito,
        movimiento.credito,
        movimiento.balance,
        clasificar(
            movimiento.descripcion
        ),
    )
)

    print("Insertando", len(datos), "movimientos")     

    cursor.executemany(
        """
        INSERT INTO movimientos (
            cuenta_id,
            fecha,
            descripcion,
            comercio,
            debito,
            credito,
            balance,
            categoria
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        datos,
    )

    conexion.commit()
    conexion.close()