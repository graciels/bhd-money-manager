from database.database import conectar


def top_comercios(limit=20):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT

            CASE

                WHEN comercio = '' OR comercio IS NULL
                THEN descripcion

                ELSE comercio

            END AS comercio,

            SUM(debito) total,

            COUNT(*) cantidad

        FROM movimientos

        WHERE debito > 0

        GROUP BY comercio

        ORDER BY total DESC

        LIMIT ?
        """,
        (limit,),
    )

    filas = cursor.fetchall()

    conexion.close()

    return filas