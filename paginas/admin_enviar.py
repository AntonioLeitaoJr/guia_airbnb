import streamlit as st
import qrcode
import io

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📲 Enviar Pesquisa</h2>
            <p style="color:#eaeaea;text-align:center;">
                Escaneie o QR Code abaixo ou acesse diretamente o link para responder à pesquisa de satisfação.<br>
                Ideal para ser impresso e deixado no apartamento.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Link da página principal do app
    link_pesquisa = "https://guiaairbnbleitao.streamlit.app"

    # Gerar QR Code apontando para a raiz
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf)
    st.image(buf, caption="📱 Escaneie com a câmera do celular", use_container_width=False)

    # Exibir o link com instrução clara
    st.markdown(f"""
        <div style="margin-top:20px; padding:10px; background-color:#f5f5f5; border-radius:8px; text-align:center;">
            <strong>Ou acesse diretamente:</strong><br>
            <a href="{link_pesquisa}" target="_blank">{link_pesquisa}</a>
        </div>
        <script>
            localStorage.setItem("modo_pesquisa", "sim");
        </script>
    """, unsafe_allow_html=True)
