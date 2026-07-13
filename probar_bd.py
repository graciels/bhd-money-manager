from database.database import conectar

conexion = conectar()
cursor = conexion.cursor()

cursor.execute("SELECT COUNT(*) FROM movimientos")
print("Total movimientos:", cursor.fetchone()[0])

cursor.execute("""
SELECT cuenta_id, COUNT(*)
FROM movimientos
GROUP BY cuenta_id
""")

print()

for fila in cursor.fetchall():
    print(
        "Cuenta:", fila["cuenta_id"],
        "Movimientos:", fila["COUNT(*)"]
    )

conexion.close()