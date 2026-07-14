import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from estadisticas.resumen import obtener_resumen

from consultas.meses import gastos_por_mes
import pandas as pd


from dashboard.componentes import mostrar_grafico_categorias

st.set_page_config(

    page_title="BHD Money Manager",

    page_icon="💰",

    layout="wide",

)

st.title("💰 BHD Money Manager")

resumen = obtener_resumen()

st.write("Mi dashboard de finanzas personales del 2025-2026")


col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📄 Movimientos",
        resumen["movimientos"],
    )

with col2:

    st.metric(
        "📈 Ingresos",
        f"RD$ {resumen['creditos']:,.2f}",
    )

with col3:

    st.metric(
        "📉 Gastos",
        f"RD$ {resumen['debitos']:,.2f}",
    )

with col4:

    st.metric(
    "💰 Saldo Total",
    f"RD$ {resumen['saldo_total']:,.2f}",
)
    
    st.divider()

st.subheader("💳 Cuentas")

columnas = st.columns(len(resumen["saldos"]))

for columna, cuenta in zip(columnas, resumen["saldos"]):

    with columna:

        st.metric(
            label=f"💳 Cuenta {cuenta['numero']}",
            value=f"RD$ {cuenta['balance_final']:,.2f}",
        )

st.divider()

st.subheader("📈 Ingresos vs Gastos por mes")

datos = pd.DataFrame(
    [dict(fila) for fila in gastos_por_mes()]
)

datos = datos.rename(
    columns={
        "mes": "Mes",
        "gastos": "Gastos",
        "ingresos": "Ingresos",
    }
)

datos = datos.set_index("Mes")

st.line_chart(datos)

st.divider()

mostrar_grafico_categorias()