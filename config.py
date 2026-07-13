from pathlib import Path

from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

# Carpeta raíz
BASE_DIR = Path(__file__).resolve().parent

# Credenciales
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"

# Contraseña del PDF
PDF_PASSWORD = os.getenv("PDF_PASSWORD")

# Carpetas
DATA_DIR = BASE_DIR / "data"
ORIGINALES_DIR = DATA_DIR / "originales"
SIN_PASSWORD_DIR = DATA_DIR / "sin_password"
EXCEL_DIR = DATA_DIR / "excel"

# Crear carpetas si no existen
for carpeta in [ORIGINALES_DIR, SIN_PASSWORD_DIR, EXCEL_DIR]:
    carpeta.mkdir(parents=True, exist_ok=True)