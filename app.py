import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io
import os

# Inicializar estados de sessão
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False

# Área de login para administradores e pesquisa
with st.sidebar.expander("🔐 Acesso Restrito"):
    senha_admin = st.text_input("Senha do Admin", type="password", key="senha_admin")
    senha_pesquisa = st.text_input("Senha da Pesquisa", type="password", key="senha_pesquisa")

    if senha_admin == "admin123":
        st.session_state["modo_admin"] = True
        st.success("✅ Modo Admin ativado!")

    if senha_pesquisa == "pesquisa123":
        st.session_state["modo_pesquisa"] = True
        st.success("✅ Modo Pesquisa ativado!")

# ⬇️ Definir menu dinâmico
opcoes_menu = ["🏠 Boas-vindas", "📘 Guia do Imóvel", "🗺️ Mapa", "🎉 Eventos"]

if st.session_state["modo_pesquisa"]:
    opcoes_menu.append("📝 Pesquisa")
if st.session_state["modo_admin"]:
    opcoes_menu += ["📲 Enviar Pesquisa", "📊 Ver Respostas", "⚙️ Configurações"]

# Carregar imagem local e exibir centralizada
imagem_logo = Image.open("simbolo_airbnb.jpg")
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image(imagem_logo, width=230)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Título estilizado
st.sidebar.markdown("""
    <h2 style='text-align: center; color: #262626;'>Guia do Hóspede</h2>
    <p style='text-align: center; color: #888;'>Navegar para:</p>
""", unsafe_allow_html=True)

# Menu lateral
menu = st.sidebar.radio("", opcoes_menu)

# ⬇️ Rotas para cada página
if menu == "🏠 Boas-vindas":
    from paginas import boas_vindas
    boas_vindas.exibir()

elif menu == "📘 Guia do Imóvel":
    from paginas import guia_imovel
    guia_imovel.exibir()

elif menu == "🗺️ Mapa":
    from paginas import mapa
    mapa.exibir()

elif menu == "🎉 Eventos":
    from paginas import eventos
    eventos.exibir()

elif menu == "📝 Pesquisa":
    from paginas import pesquisa
    pesquisa.exibir()

elif menu == "📲 Enviar Pesquisa":
    from paginas import admin_enviar
    admin_enviar.exibir()

elif menu == "📊 Ver Respostas":
    from paginas import admin_respostas
    admin_respostas.exibir()

elif menu == "⚙️ Configurações":
    from paginas import admin_config
    admin_config.exibir()
