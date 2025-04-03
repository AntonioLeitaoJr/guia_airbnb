import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Redirecionando...", layout="wide")

st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h2 style="color:#ff914d;">🔄 Redirecionando para a pesquisa...</h2>
        <p>Se isso não acontecer em alguns segundos, <a href="https://guiaairbnbleitao.streamlit.app">clique aqui</a>.</p>
    </div>
""", unsafe_allow_html=True)

# Ativa o modo_pesquisa no navegador e redireciona
components.html("""
    <script>
        localStorage.setItem("modo_pesquisa", "sim");
        window.location.replace("https://guiaairbnbleitao.streamlit.app");
    </script>
""", height=0)
