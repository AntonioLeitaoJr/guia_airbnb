import io

import qrcode
import streamlit as st


def cabecalho_card(titulo: str, descricao: str | None = None) -> None:
    descricao_html = f"""
            <p style="color:#eaeaea;text-align:center;">
                {descricao}
            </p>
    """ if descricao else ""
    st.markdown(f"""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">{titulo}</h2>
            {descricao_html}
        </div>
    """, unsafe_allow_html=True)


def mostrar_qr_code(link: str, caption: str = "📱 Escaneie com a câmera do celular") -> None:
    img_qr = qrcode.make(link)
    buf = io.BytesIO()
    img_qr.save(buf, format="PNG")
    buf.seek(0)
    st.image(buf, caption=caption, use_container_width=False)
