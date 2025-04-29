import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import streamlit.components.v1 as components

# Inicializar estados de sessão
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False
if "menu_index" not in st.session_state:
    st.session_state["menu_index"] = 0  # índice da opção selecionada no menu lateral

# Ativação automática do modo pesquisa
query_params = st.query_params
if query_params.get("pesquisa") == "sim":
    st.session_state["modo_pesquisa"] = True
    st.session_state["menu_index"] = 4  # Define como selecionada a aba "Pesquisa"

# Definir menu dinâmico
opcoes_menu = ["🏠 Boas-vindas", "📘 Guia do Imóvel", "🗺️ Mapa", "🎉 Eventos"]
# Mostrar aba de pesquisa só se NÃO estiver no modo admin
if st.session_state["modo_pesquisa"] and not st.session_state["modo_admin"]:
    opcoes_menu.append("📝 Pesquisa")

# Mostrar abas administrativas apenas para admin
if st.session_state["modo_admin"]:
    opcoes_menu += ["📲 Enviar Pesquisa", "⚙️ Configurações"]

with st.sidebar:
    st.markdown("### 🌐 Idioma")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🇧🇷", key="idioma_br"):
            st.session_state["idioma"] = "pt"
    with col2:
        if st.button("🇺🇸", key="idioma_us"):
            st.session_state["idioma"] = "en"
    with col3:
        if st.button("🇪🇸", key="idioma_es"):
            st.session_state["idioma"] = "es"

# Sidebar com logo
imagem_logo = Image.open("simbolo_airbnb.jpg")
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image(imagem_logo, width=230)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# ✅ Novo botão dentro da barra lateral
if st.sidebar.button("🔐 Acesso Restrito"):
    st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

# Campo de login (só aparece se o botão for clicado)
if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
    senha = st.sidebar.text_input("Digite a senha do administrador:", type="password")
    if senha == "admin123":
        st.session_state["modo_admin"] = True
        st.success("✅ Modo Admin ativado com sucesso!")
    elif senha != "":
        st.error("❌ Senha incorreta. Após 3 tentativas, o site será bloqueado!")

# Título estilizado
st.sidebar.markdown("""
    <h2 style='text-align: center; color: #262626;'>Guia do Hóspede</h2>
    <p style='text-align: center; color: #888;'>Navegar para:</p>
""", unsafe_allow_html=True)

# Menu lateral com índice controlado
menu = st.sidebar.radio("", opcoes_menu, index=st.session_state["menu_index"])

# Atualizar índice quando a pessoa clicar
if menu in opcoes_menu:
    st.session_state["menu_index"] = opcoes_menu.index(menu)

# Rotas
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
