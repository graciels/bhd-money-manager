COMERCIOS = {

    "JUMBO": "JUMBO",

    "LA SIRENA": "LA SIRENA",

    "PEDIDOS YA": "PEDIDOSYA",
    "PEDIDOSYA": "PEDIDOSYA",

    "AMAZON": "AMAZON",

    "SHEIN": "SHEIN",

    "PRIME VIDEO": "PRIME VIDEO",

    "NETFLIX": "NETFLIX",

    "SPOTIFY": "SPOTIFY",

    "ALTICE": "ALTICE",

    "CLARO": "CLARO",

    "TIMBIT": "TIMBIT",

    "RICO HOTDOG": "RICO HOTDOG",

    "KAME HOUSE": "KAME HOUSE",

    "UBER": "UBER",

    "PAYPAL": "PAYPAL",

    "HOSTINGER": "HOSTINGER",

    "CANVA": "CANVA",

}

def obtener_comercio(descripcion):

    descripcion = descripcion.upper()

    for palabra, comercio in COMERCIOS.items():

        if palabra in descripcion:

            return comercio

    return ""