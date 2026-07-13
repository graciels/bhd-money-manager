from dataclasses import dataclass, field

from models.cuenta import Cuenta
from models.movimiento import Movimiento


@dataclass
class EstadoCuenta:

    titular: str

    fecha_corte: str

    balance_inicial: float

    balance_final: float

    cuenta: Cuenta

    movimientos: list[Movimiento] = field(default_factory=list)