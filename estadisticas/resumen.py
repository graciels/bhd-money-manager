from database.database import conectar


def obtener_resumen():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) total_movimientos,

            SUM(debito) total_debitos,

            SUM(credito) total_creditos

        FROM movimientos
    """)

    fila = cursor.fetchone()

    conexion.close()

    return {
        "movimientos": fila["total_movimientos"],
        "debitos": fila["total_debitos"] or 0,
        "creditos": fila["total_creditos"] or 0,
    }