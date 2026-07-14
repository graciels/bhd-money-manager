from database.database import conectar


def guardar_estado(cuenta_id, estado):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO estados (

            cuenta_id,

            fecha_corte,

            balance_inicial,

            balance_final

        )
        VALUES (?, ?, ?, ?)
        """,
        (
            cuenta_id,
            estado.fecha_corte,
            estado.balance_inicial,
            estado.balance_final,
        ),
    )

    conexion.commit()

    conexion.close()