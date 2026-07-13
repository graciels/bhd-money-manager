import re

from models.movimiento import Movimiento
from datetime import datetime


def obtener_movimientos(texto):

    movimientos = []

    for linea in texto.splitlines():

        linea = linea.strip()

        if not re.match(r"\d{2}/\d{2}", linea):
            continue

        print(linea)

        partes = linea.split()

        try:

            fecha = datetime.strptime(
                f"2026/{partes[0]}",
                "%Y/%d/%m"
            ).date()

            balance = float(
                partes[-1].replace(",", "")
            )

            monto = float(
                partes[-2].replace(",", "")
            )

        except:

            continue

        descripcion = " ".join(partes[1:-2])
        descripcion_mayus = descripcion.upper()

        if (
            "CREDITO" in descripcion_mayus
            or "TRANSFERENCIA RECIBIDA" in descripcion_mayus
            or "DEPOSITO" in descripcion_mayus
            or "PAGO INTERESES" in descripcion_mayus
        ):
            debito = 0
            credito = monto
        else:
            debito = monto
            credito = 0

    movimiento = Movimiento(
        fecha=fecha,
        descripcion=descripcion,
        debito=debito,
        credito=credito,
        balance=balance,
)

    movimientos.append(movimiento)

    return movimientos