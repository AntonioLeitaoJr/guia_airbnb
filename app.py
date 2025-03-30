import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io
import os

# ⬇️ Detectar parâmetros da URL (atualizado)
query_params = st.query_params
mostrar_pesquisa = query_params.get("pesquisa", ["nao"])[0].lower() == "sim"
mostrar_admin = query_params.get("admin", ["nao"])[0].lower() == "sim"

# ⬇️ Definir menu dinâmico
opcoes_menu = ["🏠 Boas-vindas", "📘 Guia do Imóvel", "🗺️ Mapa", "🎉 Eventos"]
if mostrar_pesquisa:
    opcoes_menu.append("📝 Pesquisa")
if mostrar_admin:
    opcoes_menu += ["📲 Enviar Pesquisa", "📊 Ver Respostas", "⚙️ Configurações"]

from PIL import Image

# Carregar imagem local e exibir centralizada
imagem_logo = Image.open("simbolo_airbnb.jpg")
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image(imagem_logo, width=200)
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
