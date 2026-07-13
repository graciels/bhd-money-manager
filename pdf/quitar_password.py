from pypdf import PdfReader, PdfWriter

from config import PDF_PASSWORD


def quitar_password(pdf_entrada, pdf_salida):

    reader = PdfReader(pdf_entrada)

    if reader.is_encrypted:
        reader.decrypt(PDF_PASSWORD)

    writer = PdfWriter()

    for pagina in reader.pages:
        writer.add_page(pagina)

    with open(pdf_salida, "wb") as salida:
        writer.write(salida)