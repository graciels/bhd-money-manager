from pathlib import Path

from pdf.quitar_password import quitar_password


def preparar_pdfs():

    origen = Path("data/originales")
    destino = Path("data/sin_password")

    destino.mkdir(exist_ok=True)

    cantidad = 0

    for archivo in origen.glob("*.pdf"):

        salida = destino / archivo.name

        if salida.exists():
            print(f"⏩ {archivo.name} ya estaba preparado.")
            continue

        print(f"🔓 {archivo.name}")

        quitar_password(
            archivo,
            salida,
        )

        cantidad += 1

    print()
    print(f"✅ PDFs preparados: {cantidad}")