import pandas as pd
import streamlit as st

from paginas.componentes import cabecalho_card
from paginas.servico_sheets import listar_respostas


def exibir():
    cabecalho_card("📊 Ver Respostas", "Visualize abaixo as respostas da pesquisa de satisfação.")

    try:
        valores = listar_respostas()
    except Exception:
        st.error("Não foi possível carregar as respostas do Google Sheets agora.")
        return

    if not valores:
        st.info("Ainda não há respostas registradas.")
        return

    if len(valores) > 1:
        df = pd.DataFrame(valores[1:], columns=valores[0])
    else:
        df = pd.DataFrame(valores)

    st.dataframe(df, use_container_width=True)
    st.download_button(
        "📂 Baixar CSV",
        data=df.to_csv(index=False),
        file_name="respostas.csv",
        mime="text/csv",
    )
