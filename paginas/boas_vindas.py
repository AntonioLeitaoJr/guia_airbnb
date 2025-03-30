import streamlit as st

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

    st.markdown("""
        <div class="welcome-box">
            <div class="welcome-title">🏠 Bem-vindo à Torre Evidence!</div>
            <div class="welcome-sub">
                Esperamos que sua estadia seja confortável, segura e inesquecível.<br>
                Aqui você encontrará tudo o que precisa para aproveitar o melhor da hospedagem e da cidade de Belém.
            </div>
        </div>
    """, unsafe_allow_html=True)
