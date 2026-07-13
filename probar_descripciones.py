from database.database import conectar

conexion = conectar()

cursor = conexion.cursor()

cursor.execute("""
SELECT
    descripcion,
    COUNT(*) cantidad
FROM movimientos
WHERE categoria = 'Sin categoría'
GROUP BY descripcion
ORDER BY cantidad DESC
LIMIT 100
""")

print()

for fila in cursor.fetchall():

    print(
        f"{fila['cantidad']:>3}   "
        f"{fila['descripcion']}"
    )

conexion.close()