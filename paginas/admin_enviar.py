import streamlit as st

from config import get_pesquisa_url
from paginas.componentes import cabecalho_card, mostrar_qr_code


def exibir():
    cabecalho_card(
        "📲 Enviar Pesquisa",
        "Escaneie o QR Code abaixo ou acesse diretamente o link para responder à pesquisa de satisfação.<br>Ideal para ser impresso e deixado no apartamento.",
    )

    link_pesquisa = get_pesquisa_url()
    mostrar_qr_code(link_pesquisa)

    st.markdown(f"""
        <div style="margin-top:20px; padding:10px; background-color:#f5f5f5; border-radius:8px; text-align:center;">
            <strong>Ou acesse diretamente:</strong><br>
            <a href="{link_pesquisa}" target="_blank">{link_pesquisa}</a>
        </div>
    """, unsafe_allow_html=True)
