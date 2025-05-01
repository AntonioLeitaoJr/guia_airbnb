import streamlit as st

def exibir(idioma):
    textos = {
        "pt": {
            "titulo": "Bem-vindo à Torre Evidence!",
            "mensagem": "Esperamos que sua estadia seja confortável, segura e inesquecível.<br>Aqui você encontrará tudo o que precisa para aproveitar o melhor da hospedagem e da cidade de Belém - Pará."
        },
        "en": {
            "titulo": "Welcome to Torre Evidence!",
            "mensagem": "We hope your stay is comfortable, safe, and unforgettable.<br>Here you will find everything you need to enjoy the best of your stay and the city of Belém - Pará."
        },
        "es": {
            "titulo": "¡Bienvenido a Torre Evidence!",
            "mensagem": "Esperamos que su estadía sea cómoda, segura e inolvidable.<br>Aquí encontrará todo lo que necesita para disfrutar al máximo del alojamiento y de la ciudad de Belém - Pará."
        }
    }

    st.image("torre_evidence.jpg", use_container_width=True)

    st.markdown("""
        <style>
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

    st.markdown(f"""
        <div class="welcome-box">
            <div class="welcome-title">🏠 {textos[idioma]["titulo"]}</div>
            <div class="welcome-sub">{textos[idioma]["mensagem"]}</div>
        </div>
    """, unsafe_allow_html=True)
