from dataclasses import dataclass
from datetime import date


@dataclass
class Movimiento:

    fecha: date

    descripcion: str

    comercio: str = ""

    debito: float = 0

    credito: float = 0

    balance: float = 0

    categoria: str = ""