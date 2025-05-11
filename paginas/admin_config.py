import streamlit as st
import qrcode
import io


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

 # Link direto para o segundo app de pesquisa
    link_pesquisa = "https://guiaairbnbpesquisa.streamlit.app/"

    # Gerar e exibir o QR Code com o novo link
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf)
    st.image(buf, caption="📱 Escaneie com a câmera do celular", use_container_width=False)

    # Exibir o link logo abaixo do QR Code
    st.markdown("""
        <div style="margin-top:20px; padding:10px; background-color:#f5f5f5; border-radius:8px; text-align:center;">
            <strong>Ou acesse diretamente:</strong><br>
            <a href="""" + link_pesquisa + """" target="_blank">""" + link_pesquisa + """</a>
        </div>
    """, unsafe_allow_html=True)
