import streamlit as st
import os

CAMINHO_ARQUIVO = "eventos.txt"

# Conteúdo padrão se o arquivo não existir
def conteudo_padrao():
    return """
🎉 Eventos

Confira os eventos e atrações culturais que estão acontecendo na cidade durante o período da sua estadia!

- 26 a 30 de março: Feira da Amazônia - Hangar
- 27 de março: Show de MPB no Theatro da Paz
- 28 de março: Feira Gastronômica na Estação das Docas
- 28 de março: Feira de carros
"""

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">🎉 Eventos</h2>
    """, unsafe_allow_html=True)

    # Criar arquivo com conteúdo padrão se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            f.write(conteudo_padrao())

    # Carregar e exibir conteúdo
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    st.markdown(conteudo, unsafe_allow_html=True)

    st.markdown("""</div>""", unsafe_allow_html=True)

    # Modo edição se admin estiver ativado
    if st.session_state.get("modo_admin"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("✏️ Editar lista de eventos")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Eventos atualizados com sucesso! ✅")
