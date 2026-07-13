import re

from models.movimiento import Movimiento
from datetime import datetime


def obtener_movimientos(texto):

    movimientos = []

    for linea in texto.splitlines():

        linea = linea.strip()

        if not re.match(r"\d{2}/\d{2}", linea):
            continue

        partes = linea.split()

        fecha = datetime.strptime(
    f"2026/{partes[0]}",
    "%Y/%d/%m"
).date()

        referencia = partes[1]

        balance = float(
            partes[-1].replace(",", "")
        )

        monto = float(
            partes[-2].replace(",", "")
        )

        descripcion = " ".join(partes[2:-2])

        movimiento = Movimiento(
            fecha=fecha,
            descripcion=descripcion,
            debito=monto,
            credito=0,
            balance=balance,
        )

        movimientos.append(movimiento)

    return movimientos