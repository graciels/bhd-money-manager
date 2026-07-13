import re


def obtener_fecha_corte(texto):

    match = re.search(r"\d{4}-\d{2}-\d{2}", texto)

    if match:
        return match.group()

    return ""


def obtener_numero_cuenta(texto):

    match = re.search(r"X{7}-(\d{3}-\d)", texto)

    if match:
        return match.group(1)

    return ""


def obtener_moneda(texto):

    if "RD$" in texto:
        return "RD$"

    if "USD" in texto:
        return "USD"

    if "EUR" in texto:
        return "EUR"

    return ""


def obtener_balances(texto):

    lineas = [
        linea.strip()
        for linea in texto.splitlines()
        if linea.strip()
    ]

    indice = None

    for i, linea in enumerate(lineas):

        if linea.lower() == "balance inicial":
            indice = i
            break

    if indice is None:
        raise ValueError("No se encontró Balance Inicial")

    numeros = []

    for linea in lineas[indice + 1:]:

        valor = linea.replace(",", "")

        if re.fullmatch(r"\d+\.\d+", valor):

            numeros.append(float(valor))

            if len(numeros) == 3:
                break

    if len(numeros) < 3:
        raise ValueError("No se pudieron obtener los balances.")

    balance_inicial = numeros[0]
    balance_final = numeros[2]

    return balance_inicial, balance_final
    balance_final = float(
        obtener_valor_despues(
            lineas,
            "Balance Final"
        ).replace(",", "")
    )

    return balance_inicial, balance_final

def obtener_valor_despues(lineas, etiqueta):

    for i, linea in enumerate(lineas):

        if linea.lower() == etiqueta.lower():

            for siguiente in lineas[i + 1:]:

                texto = siguiente.replace(",", "")

                if re.fullmatch(r"\d+\.\d+", texto):
                    return siguiente

    raise ValueError(f"No se encontró un valor para '{etiqueta}'.")

def obtener_titular(texto):

    lineas = [
        linea.strip()
        for linea in texto.splitlines()
        if linea.strip()
    ]

    for i, linea in enumerate(lineas):

        if "@" in linea:

            return lineas[i - 4]

    return ""