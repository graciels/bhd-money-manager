from database.database import conectar

conexion = conectar()

cursor = conexion.cursor()

cursor.execute("""
SELECT

    fecha_corte,

    balance_inicial,

    balance_final

FROM estados

ORDER BY fecha_corte
""")

filas = cursor.fetchall()

conexion.close()

print()

for fila in filas:

    print(
        fila["fecha_corte"],
        fila["balance_inicial"],
        fila["balance_final"],
    )