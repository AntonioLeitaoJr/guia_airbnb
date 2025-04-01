import streamlit as st
import qrcode
import io

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📲 Enviar Pesquisa</h2>
            <p style="color:#eaeaea;text-align:center;">
                Copie o link abaixo e envie para o hóspede após o check-out.<br>
                Ou imprima o QR Code para deixar no apartamento.
            </p>
        </div>
    """, unsafe_allow_html=True)

    link_pesquisa = "https://guiaairbnbleitao.streamlit.app"

    # Input de link com cópia personalizada
    copiado = st.button("📋 Copiar Link da Pesquisa")
    if copiado:
        st.toast("Link copiado! Agora é só colar.", icon="📎")
        st.write("")

    st.markdown(f"""
        <script>
        window.onload = function() {{
            window.localStorage.setItem("forcar_pesquisa", "pesquisa123");
        }};
        </script>

        <input type="text" value="{link_pesquisa}" id="linkPesquisa" readonly style="width: 100%; padding: 8px; border-radius: 5px; border: none; margin-bottom: 10px;">
        <button onclick="navigator.clipboard.writeText(document.getElementById('linkPesquisa').value)" style="background-color:#ff914d;color:white;padding:10px 16px;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">
            📋 Copiar Link da Pesquisa
        </button>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📱 QR Code para Avaliação")
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf)
    st.image(buf, caption="Escaneie com a câmera do celular", use_container_width=False)