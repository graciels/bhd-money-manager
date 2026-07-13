from pathlib import Path

from pdf.parser import leer_estado


def procesar_estados(carpeta):

    estados = []

    carpeta = Path(carpeta)

    for archivo in sorted(carpeta.glob("*.pdf")):

        print(f"📄 Procesando: {archivo.name}")

        try:

            estado = leer_estado(archivo)

            estados.append(estado)

        except Exception as e:

            print(f"\n❌ Error en: {archivo.name}")

            raise

    return estados