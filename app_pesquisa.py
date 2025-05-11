import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Guia Airbnb - Pesquisa", layout="wide")

# Estilo centralizado e com fonte moderna
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Mensagens multilíngues
st.markdown("""
    <h2>🔄 Redirecionando para a Pesquisa de Satisfação...</h2>
    <p>Por favor, aguarde alguns instantes.</p>
    <h2>🔄 Redirecting to the Satisfaction Survey...</h2>
    <p>Please wait a moment.</p>
    <h2>🔄 Redirigiendo a la Encuesta de Satisfacción...</h2>
    <p>Por favor, espera unos instantes.</p>
""", unsafe_allow_html=True)

# Script com delay para redirecionamento e ativação do modo_pesquisa
components.html("""
    <script>
        localStorage.setItem("modo_pesquisa", "sim");
        setTimeout(function() {
            window.location.href = "https://guiaairbnbleitao.streamlit.app";
        }, 1500); // Redireciona após 1,5 segundos
    </script>
""", height=0)
