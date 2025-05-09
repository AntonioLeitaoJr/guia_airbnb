import streamlit as st
import os
from idiomas import pt, en, es

# 1️⃣ Obter idioma atual da sessão (padrão: pt)
idioma = st.session_state.get("idioma", "pt")
textos = {"pt": pt, "en": en, "es": es}[idioma]

# 2️⃣ Montar caminho correto do arquivo
CAMINHO_ARQUIVO = os.path.join("paginas", "textos_idiomas", f"eventos_{idioma}.txt")

# 3️⃣ Conteúdo padrão caso o arquivo ainda não exista
def conteudo_padrao():
    return {
        "pt": """
        "🎉 Eventos\n\nConteúdo ainda não cadastrado."
        """,
        "en": """
        "🎉 Events\n\nContent not yet available."
        """,
        "es": """
        "🎉 Eventos\n\nContenido aún no registrado."
    """
    }.get(idioma, "Idioma não suportado ainda.")

# 4️⃣ Exibir conteúdo
def exibir():
    st.markdown(f"""
        <div style="background-color:#262626;padding:30px;border-radius:15px;
                    box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">🎉 {textos['eventos']}</h2>
    """, unsafe_allow_html=True)

    # Criar o arquivo com conteúdo padrão se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            f.write(conteudo_padrao())

    # Carregar e exibir conteúdo
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    st.markdown(conteudo, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # 5️⃣ Modo admin: permite editar o texto
    if st.session_state.get("modo_admin"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("✏️ Editar lista de eventos")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Eventos atualizados com sucesso! ✅")
