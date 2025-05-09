import streamlit as st

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

    st.markdown(f"""
    <div style="background-color:#262626;padding:30px;border-radius:15px;
                box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
        <h2 style="color:#ff914d;text-align:center;">🗺️ {textos[idioma]["titulo"]}</h2>
        <
