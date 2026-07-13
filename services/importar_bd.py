from database.database import conectar


def guardar_cuenta(cuenta, titular):

    conexion = conectar()

    cursor = conexion.cursor()

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
                movimiento.debito,
                movimiento.credito,
                movimiento.balance,
                None,   # categoría (por ahora)
            )
        )

    print("Insertando", len(datos), "movimientos")     

    cursor.executemany(
        """
        INSERT INTO movimientos (
            cuenta_id,
            fecha,
            descripcion,
            debito,
            credito,
            balance,
            categoria
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        datos,
    )

    conexion.commit()
    conexion.close()