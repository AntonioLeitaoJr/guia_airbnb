import streamlit as st
import os

def exibir():
    idioma = st.session_state.get("idioma", "pt")
    PASTA = os.path.join("paginas", "textos_idiomas")
    CAMINHO_ARQUIVO = os.path.join(PASTA, f"guia_imovel_{idioma}.txt")

    # 🛡 Garantir que a pasta existe
    os.makedirs(PASTA, exist_ok=True)

    textos_padrao = {
        "pt": """
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
""",
        "en": """
📘 Property Guide

**Wi-Fi:** Network: `BelemGuest` | Password: `senhaboa2025`

**Condo rules:**
- Pool hours: 8 AM to 9 PM
- Meeting room: schedule at front desk
- Quiet hours: 10 PM to 7 AM

**Other details:**
- Air conditioning: turn off when leaving
- Check-out: by 11 AM
- Emergency: +55 91 99999-9999
""",
        "es": """
📘 Guía del Inmueble

**Wi-Fi:** Red: `BelemGuest` | Contraseña: `senhaboa2025`

**Reglas del condominio:**
- Horario de la piscina: 8h a 21h
- Sala de reuniones: reservar en la recepción
- Silencio entre 22h y 7h

**Otros detalles:**
- Aire acondicionado: apáguelo al salir
- Check-out: hasta las 11h
- Emergencia: +55 91 99999-9999
"""
    }

    # Criar arquivo se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            f.write(textos_padrao.get(idioma, "Conteúdo não disponível."))

    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📘 Guia do Imóvel</h2>
    """, unsafe_allow_html=True)

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    st.markdown(conteudo, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.get("modo_admin"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("✏️ Editar conteúdo do Guia")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Conteúdo salvo com sucesso! ✅")
