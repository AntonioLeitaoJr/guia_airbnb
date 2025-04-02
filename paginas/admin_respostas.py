import streamlit as st
import pandas as pd
import os

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📊 Ver Respostas</h2>
            <p style="color:#eaeaea;text-align:center;">
                Visualize abaixo as respostas da pesquisa de satisfação.
            </p>
        </div>
    """, unsafe_allow_html=True)
    if not os.path.exists("respostas.csv"):

        st.info("Ainda não há respostas registradas.")
    else:
        df = pd.read_csv("respostas.csv")
        st.dataframe(df, use_container_width=True)
        st.download_button("📂 Baixar Excel", data=df.to_csv(index=False), file_name="respostas.csv", mime="text/csv")
