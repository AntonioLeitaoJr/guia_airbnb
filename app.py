import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import streamlit.components.v1 as components

from idiomas import pt, en, es

# ===== BOTÃO HAMBÚRGUER COM SUPRESSÃO REAL DA SETA =====
components.html("""
    <script>
        const observer = new MutationObserver(() => {
            const btn = window.parent.document.querySelector('[data-testid="collapsedControl"]');
            if (btn) btn.style.display = "none";
        });
        observer.observe(window.parent.document, { childList: true, subtree: true });

        function abrirSidebar() {
            const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
            if (sidebar) sidebar.style.transform = 'translateX(0%)';
        }

        // Botão hamburguer
        const botao = document.createElement("div");
        botao.id = "customMenuBtn";
        botao.innerHTML = `
            <div class="menu-line"></div>
            <div class="menu-line"></div>
            <div class="menu-line"></div>
        `;
        botao.onclick = abrirSidebar;
        Object.assign(botao.style, {
            position: 'fixed',
            top: '10px',
            left: '10px',
            width: '45px',
            height: '45px',
            background: '#ffffffcc',
            borderRadius: '50%',
            boxShadow: '0 2px 4px rgba(0,0,0,0.3)',
            zIndex: 1000,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer'
        });
        const linha = () => {
            const div = document.createElement("div");
            div.style.width = "20px";
            div.style.height = "2px";
            div.style.background = "#333";
            div.style.margin = "3px 0";
            return div;
        };
        botao.appendChild(linha());
        botao.appendChild(linha());
        botao.appendChild(linha());
        document.body.appendChild(botao);
    </script>
""", height=0)

# ✅ Estados
if "idioma" not in st.session_state:
    st.session_state["idioma"] = "pt"
if "modo_admin" not in st.session_state:
    st.session_state["modo_admin"] = False
if "modo_pesquisa" not in st.session_state:
    st.session_state["modo_pesquisa"] = False
if "mostrar_login" not in st.session_state:
    st.session_state["mostrar_login"] = False

idioma = st.session_state["idioma"]
textos = {"pt": pt, "en": en, "es": es}[idioma]

query_params = st.query_params
if query_params.get("pesquisa") == "sim":
    st.session_state["modo_pesquisa"] = True

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("""
        <style>
        .idioma-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
        }
        .idioma-container .stButton > button {
            min-width: 60px;
            padding: 6px 12px;
            font-size: 14px;
            border-radius: 8px;
            background-color: #f0f0f5;
            border: 1px solid #ccc;
        }
        </style>
        <p style="font-size: 15px; margin-bottom: 6px;">🌐 <strong>Idioma</strong></p>
        <div class="idioma-container">
    """, unsafe_allow_html=True)

    if st.button("Português", key="idioma_pt"):
        st.session_state["idioma"] = "pt"
        st.rerun()
    if st.button("English", key="idioma_en"):
        st.session_state["idioma"] = "en"
        st.rerun()
    if st.button("Español", key="idioma_es"):
        st.session_state["idioma"] = "es"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔐 Acesso Restrito"):
        st.session_state["mostrar_login"] = not st.session_state["mostrar_login"]

    if st.session_state["mostrar_login"] and not st.session_state["modo_admin"]:
        senha = st.text_input("Digite a senha do administrador:", type="password")
        if senha == "admin123":
            st.session_state["modo_admin"] = True
            st.success("✅ Modo Admin ativado com sucesso!")
        elif senha != "":
            st.error("❌ Senha incorreta. Após 3 tentativas, o site será bloqueado!")

    st.markdown("<hr>", unsafe_allow_html=True)
    imagem_logo = Image.open("simbolo_airbnb.jpg")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(imagem_logo, width=230)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== MENU SUPERIOR COM ESTILO =====
botoes = [
    ("🏠", textos["boas_vindas"]),
    ("📘", textos["guia_imovel"]),
    ("🗺️", textos["mapa"]),
    ("🎉", textos["eventos"])
]
if st.session_state["modo_pesquisa"] and not st.session_state["modo_admin"]:
    botoes.append(("📝", textos["pesquisa"]))
if st.session_state["modo_admin"]:
    botoes.append(("⚙️", textos["configuracoes"]))

if "menu_index" not in st.session_state:
    st.session_state["menu_index"] = textos["boas_vindas"]

st.markdown("""
    <style>
    .menu-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .menu-botao {
        padding: 8px 16px;
        border-radius: 8px;
        border: 2px solid #888;
        background-color: #f9f9f9;
        font-size: 16px;
        cursor: pointer;
        text-align: center;
        color: #333;
        font-weight: normal;
        transition: 0.3s;
    }
    .menu-botao:hover {
        background-color: #eee;
        border-color: #666;
    }
    .menu-ativo {
        background-color: #003366;
        color: white !important;
        font-weight: bold;
        border-color: #003366;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="menu-container">', unsafe_allow_html=True)
cols = st.columns(len(botoes))
for i, (emoji, nome) in enumerate(botoes):
    ativo = (st.session_state["menu_index"] == nome)
    classe = "menu-botao menu-ativo" if ativo else "menu-botao"
    if cols[i].button(f"{emoji} {nome}", key=f"menu_{nome}"):
        st.session_state["menu_index"] = nome
st.markdown('</div>', unsafe_allow_html=True)

# ===== ROTAS =====
menu = st.session_state["menu_index"]

if menu == textos["boas_vindas"]:
    from paginas import boas_vindas
    boas_vindas.exibir(st.session_state["idioma"])
elif menu == textos["guia_imovel"]:
    from paginas import guia_imovel
    guia_imovel.exibir()
elif menu == textos["mapa"]:
    from paginas import mapa
    mapa.exibir()
elif menu == textos["eventos"]:
    from paginas import eventos
    eventos.exibir()
elif menu == textos["pesquisa"]:
    from paginas import pesquisa
    pesquisa.exibir()
elif menu == textos["configuracoes"]:
    from paginas import admin_config
    admin_config.exibir()
