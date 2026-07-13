from consultas.comercios import top_comercios

print()
print("TOP COMERCIOS")
print("-" * 70)

for fila in top_comercios():

    print(
        f"{fila['total']:>12.2f}   "
        f"{fila['cantidad']:>3}x   "
        f"{fila['comercio']}"
    )