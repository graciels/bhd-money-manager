import re

from datetime import datetime

from models.movimiento import Movimiento
from comercios.extractor import obtener_comercio


def obtener_movimientos(texto, fecha_corte):

    movimientos = []

    anio_corte = int(fecha_corte[:4])
    mes_corte = int(fecha_corte[5:7])

    for linea in texto.splitlines():

        linea = linea.strip()

        if not re.match(r"\d{2}/\d{2}", linea):
            continue

        partes = linea.split()

        try:

            dia_mov, mes_mov = map(
                int,
                partes[0].split("/")
            )

            anio_mov = anio_corte

            if mes_mov > mes_corte:
                anio_mov -= 1

            fecha = datetime(
                anio_mov,
                mes_mov,
                dia_mov,
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
            comercio=obtener_comercio(descripcion),
            debito=debito,
            credito=credito,
            balance=balance,
        )

        movimientos.append(movimiento)

    return movimientos