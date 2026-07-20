import streamlit as st

from paginas.componentes import cabecalho_card

def exibir():
    idioma = st.session_state.get("idioma", "pt")

    textos = {
        "pt": {
            "titulo": "Mapa",
            "mensagem": "Explore o mapa abaixo para encontrar pontos de interesse próximos à sua hospedagem, incluindo restaurantes, farmácias, supermercados e atrações turísticas."
        },
        "en": {
            "titulo": "Map",
            "mensagem": "Explore the map below to find nearby points of interest, including restaurants, pharmacies, supermarkets, and tourist attractions."
        },
        "es": {
            "titulo": "Mapa",
            "mensagem": "Explora el mapa a continuación para encontrar puntos de interés cercanos, incluyendo restaurantes, farmacias, supermercados y atracciones turísticas."
        }
    }

    cabecalho_card(f"🗺️ {textos[idioma]['titulo']}", textos[idioma]["mensagem"])

    st.components.v1.html(
        '''
        <div class="map-frame">
            <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1ZvQHCJBfEfJSD6iFA0f8zVFVM5aZ5_k&ehbc=2E312F" width="100%" height="500" loading="lazy"></iframe>
        </div>
        ''',
        height=520
    )
