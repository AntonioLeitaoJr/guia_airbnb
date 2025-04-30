import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import streamlit.components.v1 as components

from idiomas import pt, en, es

# 🔄 Detectar idioma
idioma = st.session_state.get("idioma", "pt")
textos = {"pt": pt, "en": en, "es": es}[idioma]

# Inicializar estados de sessão
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False
if "menu_index" not in st.session_state:
    st.session_state["menu_index"] = 0

# Ativação automática do modo pesquisa
query_params = st.query_params
if query_params.get("pesquisa") == "sim":
    st.session_state["modo_pesquisa"] = True
    st.session_state["menu_index"] = 4

# 🔠 Menu dinâmico com traduções
opcoes_menu = [
    f"🏠 {textos['boas_vindas']}",
    f"📘 {textos['guia_imovel']}",
    f"🗺️ {textos['mapa']}",
    f"🎉 {textos['eventos']}"
]
if st.session_state["modo_pesquisa"] and not st.session_state["modo_admin"]:
    opcoes_menu.append(f"📝 {textos['pesquisa']}")
if st.session_state["modo_admin"]:
    opcoes_menu += [
        f"📲 {textos['enviar_pesquisa']}",
        f"📊 {textos['ver_respostas']}",
        f"⚙️ {textos['configuracoes']}"
    ]

# Sidebar
with st.sidebar:
    # 🌐 Seletor de idioma estilizado
    st.markdown("""
        <style>
        .idioma-container {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
            justify-content: center;
        }
        .idioma-btn {
            font-size: 14px;
            padding: 5px 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: #f0f0f5;
            cursor: pointer;
            transition: 0.2s;
        }
        .idioma-btn:hover {
            background-color: #e0e0ff;
            border-color: #888;
        }
        </style>

        <p style="font-size: 15px; margin-bottom: 5px;">🌐 <strong>Idioma</strong></p>
        <div class="idioma-container">
            <form action="" method="post">
                <button name="idioma" value="pt" class="idioma-btn">Por</button>
                <button name="idioma" value="en" class="idioma-btn">Eng</button>
                <button name="idioma" value="es" class="idioma-btn">Esp</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

    if "idioma" in st.query_params:
        st.session_state["idioma"] = st.query_params["idioma"]
        st.experimental_rerun()

    # Logo do projeto
    imagem_logo = Image.open("simbolo_airbnb.jpg")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(imagem_logo, width=230)
    st.markdown("</div>", unsafe_allow_html=True)

    # Botão de login admin
    if st.button("🔐 Acesso Restrito"):
        st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

    if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
        senha = st.text_input("Digite a senha do administrador:", type="password")
        if senha == "admin123":
            st.session_state["modo_admin"] = True
            st.success("✅ Modo Admin ativado com sucesso!")
        elif senha != "":
            st.error("❌ Senha incorreta. Após 3 tentativas, o site será bloqueado!")

    # Título e menu traduzido
    st.markdown(f"""
        <h2 style='text-align: center; color: #262626;'>{textos['sidebar_title']}</h2>
        <p style='text-align: center; color: #888;'>{textos['navegar_para']}</p>
    """, unsafe_allow_html=True)

# Menu lateral
menu = st.sidebar.radio("", opcoes_menu, index=st.session_state["menu_index"])
if menu in opcoes_menu:
    st.session_state["menu_index"] = opcoes_menu.index(menu)

# Rotas
if menu.endswith(textos["boas_vindas"]):
    from paginas import boas_vindas
    boas_vindas.exibir()
elif menu.endswith(textos["guia_imovel"]):
    from paginas import guia_imovel
    guia_imovel.exibir()
elif menu.endswith(textos["mapa"]):
    from paginas import mapa
    mapa.exibir()
elif menu.endswith(textos["eventos"]):
    from paginas import eventos
    eventos.exibir()
elif menu.endswith(textos["pesquisa"]):
    from paginas import pesquisa
    pesquisa.exibir()
elif menu.endswith(textos["enviar_pesquisa"]):
    from paginas import admin_enviar
    admin_enviar.exibir()
elif menu.endswith(textos["ver_respostas"]):
    from paginas import admin_respostas
    admin_respostas.exibir()
elif menu.endswith(textos["configuracoes"]):
    from paginas import admin_config
    admin_config.exibir()
