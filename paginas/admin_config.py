import streamlit as st

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">⚙️ Configurações</h2>
            <p style="color:#eaeaea;text-align:center;">
                Aqui você poderá configurar o link público, QR Code, exportação e envio de dados futuramente.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.warning("Em breve: envio automático de respostas por e-mail, edição visual do QR e muito mais! ✨")
