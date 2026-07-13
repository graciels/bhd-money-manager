from estadisticas.resumen import obtener_resumen

resumen = obtener_resumen()

print()

balance = resumen["creditos"] - resumen["debitos"]

print(f"MOVIMIENTOS: {resumen['movimientos']}")
print(f"DÉBITOS: RD$ {resumen['debitos']:.2f}")
print(f"CRÉDITOS: RD$ {resumen['creditos']:.2f}")
print(f"BALANCE: RD$ {balance:.2f}")