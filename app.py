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
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False

# ⬇️ Ativação automática do modo pesquisa via localStorage
import streamlit.components.v1 as components
components.html("""
    <script>
        if (localStorage.getItem("modo_pesquisa") === "sim") {
            window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'modo_pesquisa', value: true}, '*');
        }
    </script>
""", height=0)

# ⬇️ Menu lateral
opcoes_menu = ["🏠 Boas-vindas", "📘 Guia do Imóvel", "🗺️ Mapa", "🎉 Eventos"]
if st.session_state["modo_pesquisa"]:
    opcoes_menu.append("📝 Pesquisa")
if st.session_state["modo_admin"]:
    opcoes_menu += ["📲 Enviar Pesquisa", "📊 Ver Respostas", "⚙️ Configurações"]

imagem_logo = Image.open("simbolo_airbnb.jpg")
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image(imagem_logo, width=230)
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <h2 style='text-align: center; color: #262626;'>Guia do Hóspede</h2>
    <p style='text-align: center; color: #888;'>Navegar para:</p>
""", unsafe_allow_html=True)
menu = st.sidebar.radio("", opcoes_menu)

# ✅ Estilo e botão flutuante funcional
st.markdown("""
    <style>
        div[data-testid="stButton"] > button.floating-btn {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #ff914d;
            color: white;
            padding: 10px 16px;
            border-radius: 10px;
            font-weight: bold;
            z-index: 10000;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Botão real com classe customizada (funciona!)
if st.button("🔐 Acesso Restrito", key="btn_flutuante", help="Clique para entrar como admin", args=(), kwargs={}, type="secondary"):
    st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

# Campo de login
if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
    senha = st.text_input("Digite a senha do administrador:", type="password")
    if senha == "admin123":
        st.session_state["modo_admin"] = True
        st.success("✅ Modo Admin ativado com sucesso!")
    elif senha != "":
        st.error("❌ Senha incorreta.")

# ⬇️ Rotas
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
