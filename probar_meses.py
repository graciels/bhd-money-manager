from consultas.meses import gastos_por_mes

print()
print("GASTOS POR MES")
print("-" * 45)

for fila in gastos_por_mes():

    print(
        f"{fila['mes']}   "
        f"Gastos: RD$ {fila['gastos']:>10.2f}   "
        f"Ingresos: RD$ {fila['ingresos']:>10.2f}"
    )