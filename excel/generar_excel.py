from openpyxl import Workbook


def generar_excel(movimientos, ruta):

    wb = Workbook()

    ws = wb.active

    ws.title = "Movimientos"

    ws.append([
        "Fecha",
        "Descripción",
        "Débito",
        "Crédito",
        "Balance",
        "Categoría",
    ])

    for movimiento in movimientos:

        ws.append([
            movimiento.fecha.isoformat(),
            movimiento.descripcion,
            movimiento.debito,
            movimiento.credito,
            movimiento.balance,
            movimiento.categoria,
        ])

    wb.save(ruta)