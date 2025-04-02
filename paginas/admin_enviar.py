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

    st.markdown("""
        <script>
        function copiarTexto() {
            var texto = document.getElementById("linkPesquisa").value;
            navigator.clipboard.writeText(texto);
            const streamlitEvent = new Event("copiadoStreamlit");
            window.dispatchEvent(streamlitEvent);
        }
        </script>
        <input type="text" value="""" + link_pesquisa + """" id="linkPesquisa" readonly style="width: 100%; padding: 8px; border-radius: 5px; border: none; margin-bottom: 10px;">
        <button onclick="copiarTexto()" style="background-color:#ff914d;color:white;padding:10px 16px;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">
            📋 Copiar Link da Pesquisa
        </button>
    """, unsafe_allow_html=True)

    # Função para exibir toast se evento JS for disparado
    st.markdown("""
        <script>
        window.addEventListener("copiadoStreamlit", () => {
            Streamlit.setComponentValue("copiado");
        });
        </script>
    """, unsafe_allow_html=True)

    if st.session_state.get("copiado_toast") != True:
        st.session_state["copiado_toast"] = False

    copied = st.experimental_get_query_params().get("copiado")
    if copied and not st.session_state["copiado_toast"]:
        st.toast("Link copiado! Agora é só colar.", icon="📎")
        st.session_state["copiado_toast"] = True

    st.markdown("---")

    st.subheader("📱 QR Code para Avaliação")
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf)
    st.image(buf, caption="Escaneie com a câmera do celular", use_container_width=False)