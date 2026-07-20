import base64
from pathlib import Path

import streamlit as st


def _imagem_base64(caminho: str) -> str:
    return base64.b64encode(Path(caminho).read_bytes()).decode("utf-8")


def exibir(idioma):
    textos = {
        "pt": {
            "titulo": "Bem-vindo ao Apartamento 904 da Torre Evidence!",
            "mensagem": "Tudo o que você precisa para uma estadia confortável, segura e inesquecível em Belém - Pará.",
            "tag": "Guia digital do hóspede",
            "cards": [
                ("📶 Wi‑Fi e regras", "Consulte informações essenciais do apartamento em poucos toques."),
                ("🗺️ Mapa local", "Encontre restaurantes, farmácias, mercados e atrações próximas."),
                ("🎉 Eventos", "Veja recomendações e atualizações para aproveitar melhor a cidade."),
            ],
        },
        "en": {
            "titulo": "Welcome to Apartment 904 at Torre Evidence!",
            "mensagem": "Everything you need for a comfortable, safe and memorable stay in Belém - Pará.",
            "tag": "Digital guest guide",
            "cards": [
                ("📶 Wi‑Fi & rules", "Check the apartment essentials in just a few taps."),
                ("🗺️ Local map", "Find restaurants, pharmacies, markets and nearby attractions."),
                ("🎉 Events", "See recommendations and updates to enjoy the city."),
            ],
        },
        "es": {
            "titulo": "¡Bienvenido al Apartamento 904 de la Torre Evidence!",
            "mensagem": "Todo lo que necesitas para una estadía cómoda, segura e inolvidable en Belém - Pará.",
            "tag": "Guía digital del huésped",
            "cards": [
                ("📶 Wi‑Fi y reglas", "Consulta la información esencial del apartamento en pocos toques."),
                ("🗺️ Mapa local", "Encuentra restaurantes, farmacias, mercados y atracciones cercanas."),
                ("🎉 Eventos", "Mira recomendaciones y novedades para disfrutar la ciudad."),
            ],
        },
    }

    t = textos[idioma]
    imagem = _imagem_base64("torre_evidence.jpg")

    st.markdown(
        f"""
        <section class="hero-card">
            <div class="hero-image" style="background-image: url('data:image/jpeg;base64,{imagem}');">
                <div class="hero-content">
                    <div class="eyebrow">✨ {t["tag"]}</div>
                    <h1 class="hero-title">{t["titulo"]}</h1>
                    <p class="hero-subtitle">{t["mensagem"]}</p>
                </div>
            </div>
        </section>
        <div class="quick-grid">
            {''.join(f'<div class="metric-card"><strong>{titulo}</strong><span>{descricao}</span></div>' for titulo, descricao in t["cards"])}
        </div>
        """,
        unsafe_allow_html=True,
    )
