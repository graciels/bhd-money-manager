from consultas.meses import gastos_por_mes

datos = gastos_por_mes()

print(type(datos))
print()

for fila in datos[:3]:
    print(dict(fila))