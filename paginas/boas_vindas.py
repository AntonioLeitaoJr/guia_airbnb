import streamlit as st
from idiomas import pt, en, es

# Detectar idioma
idioma = st.session_state.get("idioma", "pt")
textos = {"pt": pt, "en": en, "es": es}[idioma]

def exibir():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #1e1e1e;
        }

        .banner-img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5);
        }

        .welcome-box {
            background-color: #262626;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
        }

        .welcome-title {
            color: #ff914d;
            text-align: center;
            font-size: 36px;
            font-weight: 700;
        }

        .welcome-sub {
            color: #eaeaea;
            text-align: center;
            font-size: 18px;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.image("torre_evidence.jpg", use_container_width=True)

    st.markdown(f"""
        <div class="welcome-box">
            <div class="welcome-title">🏠 {textos['boas_vindas_titulo']}</div>
            <div class="welcome-sub">
                {textos['boas_vindas_texto']}
            </div>
        </div>
    """, unsafe_allow_html=True)
