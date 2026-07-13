from database.database import conectar


def gastos_por_categoria():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            categoria,
            SUM(debito) total
        FROM movimientos
        WHERE debito > 0
        GROUP BY categoria
        ORDER BY total DESC
    """)

    resultados = cursor.fetchall()

    conexion.close()

    return resultados