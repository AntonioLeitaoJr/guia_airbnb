import streamlit as st

def exibir():
    st.markdown("""
    <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
        <h2 style="color:#ff914d;text-align:center;">🗺️ Mapa</h2>
        <p style="color:#eaeaea;text-align:center;">
            Explore o mapa abaixo para encontrar pontos de interesse próximos à sua hospedagem, incluindo restaurantes, farmácias, supermercados e atrações turísticas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.components.v1.html(
        '''
        <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1ZvQHCJBfEfJSD6iFA0f8zVFVM5aZ5_k&ehbc=2E312F" width="100%" height="500"></iframe>
        ''',
        height=520
    )
