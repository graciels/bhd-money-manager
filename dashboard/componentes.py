import pandas as pd
import streamlit as st

from consultas.categorias import gastos_por_categoria


def mostrar_grafico_categorias():

    datos = pd.DataFrame(
        [dict(fila) for fila in gastos_por_categoria()]
    )

    datos = datos.rename(
        columns={
            "categoria": "Categoría",
            "total": "Monto",
        }
    )

    st.subheader("🥧 Gastos por categoría")

    st.bar_chart(
        datos.set_index("Categoría")
    )