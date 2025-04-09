import streamlit as st
import os

CAMINHO_ARQUIVO = "guia_imovel.txt"

# Conteúdo padrão se o arquivo não existir
def conteudo_padrao():
    return """
📘 Guia do Imóvel

**Wi-Fi:** Rede: `BelemGuest` | Senha: `senhaboa2025`

**Regras do condomínio:**
- Horário da piscina: 8h às 21h
- Sala de reuniões: agendar na portaria
- Silêncio entre 22h e 7h

**Outros detalhes:**
- Ar-condicionado: desligue ao sair
- Check-out: até às 11h
- Emergência: (91) 99999-9999
"""

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📘 Guia do Imóvel</h2>
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
        st.subheader("✏️ Editar conteúdo do Guia")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Conteúdo salvo com sucesso! ✅")
