from dataclasses import dataclass
from datetime import date


@dataclass
class Movimiento:

    fecha: date

    descripcion: str

    debito: float

    credito: float

    balance: float

    categoria: str = ""