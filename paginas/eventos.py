import streamlit as st

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">🎉 Eventos</h2>
            <p style="color:#eaeaea;text-align:center;">
                Confira os eventos e atrações culturais que estão acontecendo na cidade durante o período da sua estadia!
            </p>
            <ul style="color:#eaeaea;font-size:16px;">
                <li>26 a 30 de março: Feira da Amazônia - Hangar</li>
                <li>27 de março: Show de MPB no Theatro da Paz</li>
                <li>28 de março: Feira Gastronômica na Estação das Docas</li>
                <li>28 de março: Feira de carros</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
