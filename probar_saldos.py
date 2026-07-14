from consultas.saldos import obtener_saldos_actuales

print()

print("SALDOS ACTUALES")

print("-" * 40)

total = 0

for fila in obtener_saldos_actuales():

    total += fila["balance_final"]

    print(
        f"{fila['numero']}    "
        f"RD$ {fila['balance_final']:,.2f}"
    )

print("-" * 40)

print(f"TOTAL: RD$ {total:,.2f}")