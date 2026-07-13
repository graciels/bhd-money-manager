import sqlite3
from pathlib import Path


DB_PATH = Path("data/money.db")


def conectar():

    DB_PATH.parent.mkdir(exist_ok=True)

    conexion = sqlite3.connect(DB_PATH)

    conexion.row_factory = sqlite3.Row

    return conexion


def crear_tablas():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuentas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            numero TEXT NOT NULL,

            moneda TEXT NOT NULL,

            titular TEXT NOT NULL

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            cuenta_id INTEGER NOT NULL,

            fecha TEXT NOT NULL,

            descripcion TEXT NOT NULL,

            debito REAL NOT NULL,

            credito REAL NOT NULL,

            balance REAL NOT NULL,

            categoria TEXT,

            FOREIGN KEY (cuenta_id)
                REFERENCES cuentas(id)

        )
    """)

    conexion.commit()
    conexion.close()


def limpiar_tablas():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("DELETE FROM movimientos")
    cursor.execute("DELETE FROM cuentas")

    conexion.commit()
    conexion.close()