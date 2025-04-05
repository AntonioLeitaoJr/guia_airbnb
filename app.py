import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io
import os
import streamlit.components.v1 as components

# Inicializar estados de sessão
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False

# 🔓 Ativação automática do modo pesquisa (via localStorage)
components.html("""
    <script>
        if (localStorage.getItem("modo_pesquisa") === "sim") {
            window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'modo_pesquisa', value: true}, '*');
        }
    </script>
""", height=0)

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

# ✅ Botão flutuante para modo admin
st.markdown("""
    <style>
        .botao-flutuante {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #ff914d;
            color: white;
            padding: 12px 18px;
            border-radius: 12px;
            font-weight: bold;
            z-index: 9999;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
            cursor: pointer;
        }
    </style>
    <div class='botao-flutuante'>
        <form action='#' method='post'>
            <button name='mostrar_login' type='submit'>🔐 Acesso Restrito</button>
        </form>
    </div>
""", unsafe_allow_html=True)

# Detectar clique no botão (simulado via formulário HTML)
if st.session_state.get("mostrar_login"):
    st.session_state["mostrar_login"] = False
else:
    if st.button("🔐 Acesso Restrito", key="botao_admin", help="Clique para entrar como administrador"):
        st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

# Formulário de login quando ativado
if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
    senha = st.text_input("Digite a senha do administrador:", type="password", key="input_admin")
    if senha == "admin123":
        st.session_state["modo_admin"] = True
        st.success("✅ Modo Admin ativado com sucesso!")
    elif senha != "":
        st.error("❌ Senha incorreta.")

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
