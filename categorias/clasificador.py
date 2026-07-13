from categorias.reglas import CATEGORIAS


def clasificar(descripcion):

    descripcion = descripcion.upper()

    for palabra, categoria in CATEGORIAS.items():

        if palabra in descripcion:

            return categoria

    return "Sin categoría"