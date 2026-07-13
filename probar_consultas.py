from consultas.categorias import gastos_por_categoria

print()
print("GASTOS POR CATEGORÍA")
print("-" * 40)

for fila in gastos_por_categoria():

    print(
        f"{fila['categoria']:<20}"
        f"RD$ {fila['total']:>10.2f}"
    )