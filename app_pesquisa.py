import streamlit as st
import streamlit.components.v1 as components

# Redirecionador automático para o app principal com modo_pesquisa ativado
st.set_page_config(page_title="Guia Airbnb - Pesquisa", layout="wide")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h2>🔄 Redirecionando para a Pesquisa de Satisfação...</h2>
    <p>Por favor, aguarde alguns instantes.</p>
""", unsafe_allow_html=True)

# Script que ativa o modo_pesquisa e redireciona
components.html("""
    <script>
        localStorage.setItem("modo_pesquisa", "sim");
        window.location.href = "https://guiaairbnbleitao.streamlit.app";
    </script>
""", height=0)
