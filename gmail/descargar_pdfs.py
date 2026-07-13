import base64

from config import ORIGINALES_DIR


def obtener_correos(servicio, query):

    respuesta = (
        servicio.users()
        .messages()
        .list(userId="me", q=query)
        .execute()
    )

    return respuesta.get("messages", [])


def obtener_mensaje(servicio, message_id):

    return (
        servicio.users()
        .messages()
        .get(userId="me", id=message_id)
        .execute()
    )


def descargar_adjunto(servicio, attachment_id, message_id, nombre_archivo):

    archivo = (
        servicio.users()
        .messages()
        .attachments()
        .get(
            userId="me",
            messageId=message_id,
            id=attachment_id,
        )
        .execute()
    )

    datos = base64.urlsafe_b64decode(archivo["data"])

    ruta = ORIGINALES_DIR / nombre_archivo

    with open(ruta, "wb") as f:
        f.write(datos)

    return ruta