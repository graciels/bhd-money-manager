from database.database import conectar


def obtener_saldos_actuales():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT

            c.numero,

            e.balance_final,

            e.fecha_corte

        FROM estados e

        INNER JOIN cuentas c

            ON c.id = e.cuenta_id

        WHERE e.id IN (

            SELECT MAX(id)

            FROM estados

            GROUP BY cuenta_id

        )

        ORDER BY c.numero
    """)

    filas = cursor.fetchall()

    conexion.close()

    return filas