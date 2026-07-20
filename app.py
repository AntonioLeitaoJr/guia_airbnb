import streamlit as st
from PIL import Image

from config import get_config
from idiomas import en, es, pt
from paginas.componentes import aplicar_estilo_global

aplicar_estilo_global()

PAGINAS = {
    "boas_vindas": {
        "emoji": "🏠",
        "label": "boas_vindas",
        "modulo": "boas_vindas",
        "admin": False,
        "pesquisa": False,
    },
    "guia_imovel": {
        "emoji": "📘",
        "label": "guia_imovel",
        "modulo": "guia_imovel",
        "admin": False,
        "pesquisa": False,
    },
    "mapa": {
        "emoji": "🗺️",
        "label": "mapa",
        "modulo": "mapa",
        "admin": False,
        "pesquisa": False,
    },
    "eventos": {
        "emoji": "🎉",
        "label": "eventos",
        "modulo": "eventos",
        "admin": False,
        "pesquisa": False,
    },
    "pesquisa": {
        "emoji": "📝",
        "label": "pesquisa",
        "modulo": "pesquisa",
        "admin": False,
        "pesquisa": True,
    },
    "configuracoes": {
        "emoji": "⚙️",
        "label": "configuracoes",
        "modulo": "admin_config",
        "admin": True,
        "pesquisa": False,
    },
    "enviar_pesquisa": {
        "emoji": "📲",
        "label": "enviar_pesquisa",
        "modulo": "admin_enviar",
        "admin": True,
        "pesquisa": False,
    },
    "ver_respostas": {
        "emoji": "📊",
        "label": "ver_respostas",
        "modulo": "admin_respostas",
        "admin": True,
        "pesquisa": False,
    },
}

# ✅ Idioma padrão
if "idioma" not in st.session_state:
    st.session_state["idioma"] = "pt"

idioma = st.session_state["idioma"]
textos = {"pt": pt, "en": en, "es": es}[idioma]

# ✅ Estados
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False
if "tentativas_login" not in st.session_state:
    st.session_state["tentativas_login"] = 0

# ✅ Ativação automática por link
query_params = st.query_params
if query_params.get("pesquisa") == "sim":
    st.session_state["modo_pesquisa"] = True
    st.session_state["menu_index"] = "pesquisa"

# ===== SIDEBAR (idioma e login apenas) =====
with st.sidebar:
    st.markdown("### 🌐 Idioma")
    if st.button("Português", key="idioma_pt"):
        st.session_state["idioma"] = "pt"
        st.rerun()
    if st.button("English", key="idioma_en"):
        st.session_state["idioma"] = "en"
        st.rerun()
    if st.button("Español", key="idioma_es"):
        st.session_state["idioma"] = "es"
        st.rerun()

    if st.button("🔐 Acesso Restrito"):
        st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

    if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
        if st.session_state["tentativas_login"] >= 3:
            st.error("❌ Acesso bloqueado após 3 tentativas incorretas nesta sessão.")
        else:
            senha = st.text_input("Digite a senha do administrador:", type="password")
            senha_admin = get_config("ADMIN_PASSWORD", "admin123")
            if senha and senha == senha_admin:
                st.session_state["modo_admin"] = True
                st.session_state["tentativas_login"] = 0
                st.success("✅ Modo Admin ativado com sucesso!")
            elif senha:
                st.session_state["tentativas_login"] += 1
                st.error("❌ Senha incorreta.")

    if st.session_state["modo_admin"] and st.button("🚪 Sair do Admin"):
        st.session_state["modo_admin"] = False
        st.session_state["menu_index"] = "boas_vindas"
        st.rerun()

    # 🔻 Logo
    st.markdown("<hr>", unsafe_allow_html=True)
    imagem_logo = Image.open("simbolo_airbnb.jpg")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(imagem_logo, width=230)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== MENU SUPERIOR COM ESTILO =====
menu_keys = ["boas_vindas", "guia_imovel", "mapa", "eventos"]

if st.session_state["modo_pesquisa"] and not st.session_state["modo_admin"]:
    menu_keys.append("pesquisa")
if st.session_state["modo_admin"]:
    menu_keys.extend(["configuracoes", "enviar_pesquisa", "ver_respostas"])

if "menu_index" not in st.session_state or st.session_state["menu_index"] not in menu_keys:
    st.session_state["menu_index"] = "boas_vindas"

st.markdown("#### ✨ Navegação rápida")

cols = st.columns(len(menu_keys))
for i, pagina_key in enumerate(menu_keys):
    pagina = PAGINAS[pagina_key]
    label = textos[pagina["label"]]
    prefixo = "● " if st.session_state["menu_index"] == pagina_key else ""
    if cols[i].button(f"{prefixo}{pagina['emoji']} {label}", key=f"menu_{pagina_key}"):
        st.session_state["menu_index"] = pagina_key

# ===== ROTAS =====
menu = st.session_state["menu_index"]

if menu == "boas_vindas":
    from paginas import boas_vindas
    boas_vindas.exibir(st.session_state["idioma"])
elif menu == "guia_imovel":
    from paginas import guia_imovel
    guia_imovel.exibir()
elif menu == "mapa":
    from paginas import mapa
    mapa.exibir()
elif menu == "eventos":
    from paginas import eventos
    eventos.exibir()
elif menu == "pesquisa":
    from paginas import pesquisa
    pesquisa.exibir()
elif menu == "configuracoes":
    from paginas import admin_config
    admin_config.exibir()
elif menu == "enviar_pesquisa":
    from paginas import admin_enviar
    admin_enviar.exibir()
elif menu == "ver_respostas":
    from paginas import admin_respostas
    admin_respostas.exibir()
