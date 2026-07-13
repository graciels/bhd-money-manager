from services.preparar_pdfs import preparar_pdfs
from services.procesar_estados import procesar_estados
from database.database import crear_tablas


def main():

    crear_tablas()

    preparar_pdfs()

    estados = procesar_estados("data/sin_password")

    print()
    print("=" * 60)
    print(f"Estados procesados: {len(estados)}")
    print("=" * 60)

    for estado in estados:

        print(
            f"{estado.fecha_corte} | "
            f"{estado.cuenta.numero} | "
            f"{len(estado.movimientos)} movimientos"
        )


if __name__ == "__main__":
    main()