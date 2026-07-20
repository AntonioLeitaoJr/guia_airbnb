import streamlit as st

from config import get_app_url, get_pesquisa_url
from paginas.componentes import cabecalho_card, mostrar_qr_code


def exibir():
    cabecalho_card(
        "⚙️ Configurações",
        "Aqui você pode consultar o link público, QR Code e mensagens prontas para envio aos hóspedes.",
    )

    app_url = get_app_url()
    link_pesquisa = get_pesquisa_url()

    st.warning(f"""Mensagem para enviar ao hóspede na entrada!
               
---               
               
Olá! 😊
Estamos muito felizes por saber que você escolheu se hospedar conosco!
Preparamos tudo com carinho para que sua experiência seja tranquila, segura e inesquecível.
Antes mesmo da sua chegada, você já pode acessar nosso Guia Digital com todas as informações úteis sobre o apartamento, o condomínio e a cidade:
👉 {app_url}
Seja muito bem-vindo! Estamos à disposição para o que precisar. 💙

---

Hello! 😊
We’re thrilled to know that you’ve chosen to stay with us!
We’ve prepared everything with care so your experience will be smooth, safe, and unforgettable.
Even before your arrival, you can access our Digital Guide with all the useful information about the apartment, the building, and the city:
👉 {app_url}
Welcome! We’re here for anything you need. 💙

---

¡Hola! 😊
¡Estamos muy felices de saber que elegiste hospedarte con nosotros!
Hemos preparado todo con cariño para que tu experiencia sea tranquila, segura e inolvidable.
Incluso antes de tu llegada, ya puedes acceder a nuestra Guía Digital con toda la información útil sobre el apartamento, el condominio y la ciudad:
👉 {app_url}
¡Bienvenido! Estamos a tu disposición para lo que necesites. 💙""")

    st.warning(f"""Mensagem para enviar ao hóspede na saída!

---
               
Olá! 👋 Esperamos que sua estadia tenha sido maravilhosa! 🌟
Para nos ajudar a sempre melhorar, pedimos apenas 1 minutinho:
Clique aqui 👉 {link_pesquisa} e responda nossa pesquisa rápida.
Sua opinião é muito importante para nós! ❤
Muito obrigado!

---

Hello! 👋 We hope your stay was wonderful! 🌟
To help us keep improving, we kindly ask for just 1 minute:
Click here 👉 {link_pesquisa} and answer our quick survey.
Your opinion is very important to us! ❤
Thank you very much!

---

¡Hola! 👋 ¡Esperamos que tu estadía haya sido maravillosa! 🌟
Para ayudarnos a mejorar siempre, te pedimos solo un minutito:
Haz clic aquí 👉 {link_pesquisa} y responde nuestra encuesta rápida.
¡Tu opinión es muy importante para nosotros! ❤
¡Muchas gracias!""")

    mostrar_qr_code(link_pesquisa)

    st.markdown(f"""
        <div style="margin-top:20px; padding:10px; background-color:#f5f5f5; border-radius:8px; text-align:center;">
            <strong>Ou acesse diretamente:</strong><br>
            <a href="{link_pesquisa}" target="_blank">{link_pesquisa}</a>
        </div>
    """, unsafe_allow_html=True)
