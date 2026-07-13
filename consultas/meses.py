from database.database import conectar


def gastos_por_mes():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT

            substr(fecha, 1, 7) mes,

            SUM(debito) gastos,

            SUM(credito) ingresos

        FROM movimientos

        GROUP BY mes

        ORDER BY mes
    """)

    filas = cursor.fetchall()

    conexion.close()

    return filas