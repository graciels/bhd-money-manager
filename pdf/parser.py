from pypdf import PdfReader

from models.cuenta import Cuenta
from models.estado_cuenta import EstadoCuenta
from pdf.movimientos import obtener_movimientos
from pdf.encabezado import obtener_balances
from pdf.encabezado import obtener_titular

from pdf.encabezado import (
    obtener_fecha_corte,
    obtener_moneda,
    obtener_numero_cuenta,
)


def leer_pdf(ruta_pdf):

    reader = PdfReader(ruta_pdf)

    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text()

    return texto


def leer_estado(ruta_pdf):

    texto = leer_pdf(ruta_pdf)

    cuenta = Cuenta(
        numero=obtener_numero_cuenta(texto),
        moneda=obtener_moneda(texto),
    )

    
    balance_inicial, balance_final = obtener_balances(texto)

    estado = EstadoCuenta(

    titular=obtener_titular(texto),

    fecha_corte=obtener_fecha_corte(texto),

    balance_inicial=balance_inicial,

    balance_final=balance_final,

    cuenta=cuenta,

    movimientos=obtener_movimientos(texto),
)

    return estado