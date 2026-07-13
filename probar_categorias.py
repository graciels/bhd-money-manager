from database.database import conectar

conexion = conectar()

cursor = conexion.cursor()

cursor.execute("""
SELECT
    categoria,
    COUNT(*) cantidad
FROM movimientos
GROUP BY categoria
ORDER BY cantidad DESC
""")

print()

for fila in cursor.fetchall():

    print(
        f"{fila['categoria']:<20}"
        f"{fila['cantidad']}"
    )

conexion.close()