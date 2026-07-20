import streamlit as st
import os
from idiomas import pt, en, es  # ✅ Importa os textos
from paginas.componentes import cabecalho_card

def exibir():
    idioma = st.session_state.get("idioma", "pt")
    textos = {"pt": pt, "en": en, "es": es}[idioma]

    CAMINHO_ARQUIVO = os.path.join("paginas", "textos_idiomas", f"eventos_{idioma}.txt")

    # Conteúdo padrão por idioma
    def conteudo_padrao():
        return {
            "pt": "🎉 Eventos\n\nConteúdo ainda não cadastrado.",
            "en": "🎉 Events\n\nContent not yet available.",
            "es": "🎉 Eventos\n\nContenido aún no registrado."
        }.get(idioma, "Idioma não suportado ainda.")

    # Criar o arquivo com conteúdo padrão se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            f.write(conteudo_padrao())

    # Carregar conteúdo
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Exibir título e conteúdo
    cabecalho_card(f"🎉 {textos['eventos']}", "Confira eventos, passeios e sugestões atualizadas para sua estadia.")

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown(conteudo)
    st.markdown("</div>", unsafe_allow_html=True)

    # Edição se for admin
    if st.session_state.get("modo_admin"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("✏️ Editar lista de eventos")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Eventos atualizados com sucesso! ✅")
