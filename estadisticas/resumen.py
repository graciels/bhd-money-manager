from database.database import conectar
from consultas.saldos import obtener_saldos_actuales


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

    saldos = obtener_saldos_actuales()

    saldo_total = sum(
        fila["balance_final"]
        for fila in saldos
    )

    return {

        "movimientos": fila["total_movimientos"],

        "debitos": fila["total_debitos"] or 0,

        "creditos": fila["total_creditos"] or 0,

        "saldo_total": saldo_total,

        "saldos": saldos,

    }