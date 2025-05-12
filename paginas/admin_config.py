import streamlit as st
import qrcode
import io

def exibir():
    # Cabeçalho visual da aba
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">⚙️ Configurações</h2>
            <p style="color:#eaeaea;text-align:center;">
                Aqui você poderá configurar o link público, QR Code, exportação e envio de dados futuramente.
            </p>
        </div>
    """, unsafe_allow_html=True)
    # Mensagem multilíngue em st.warning (com aspas corrigidas)
    st.warning("""Olá! 👋 Esperamos que sua estadia tenha sido maravilhosa! 🌟
Para nos ajudar a sempre melhorar, pedimos apenas 1 minutinho:
Clique aqui 👉 https://guiaairbnbpesquisa.streamlit.app/ e responda nossa pesquisa rápida.
Sua opinião é muito importante para nós! ❤
Muito obrigado!

---

Hello! 👋 We hope your stay was wonderful! 🌟
To help us keep improving, we kindly ask for just 1 minute:
Click here 👉 https://guiaairbnbpesquisa.streamlit.app/ and answer our quick survey.
Your opinion is very important to us! ❤
Thank you very much!

---

¡Hola! 👋 ¡Esperamos que tu estadía haya sido maravillosa! 🌟
Para ayudarnos a mejorar siempre, te pedimos solo 1 minutito:
Haz clic aquí 👉 https://guiaairbnbpesquisa.streamlit.app/ y responde nuestra encuesta rápida.
¡Tu opinión es muy importante para nosotros! ❤
¡Muchas gracias!""")
    
    # Mensagem multilíngue em st.warning (Envio de mensagem Whatsapp de pesquisa)
    st.warning("""Mesagem para enviar ao hóspede na saída para responder ao questionário!

---
               
Olá! 👋 Esperamos que sua estadia tenha sido maravilhosa! 🌟
Para nos ajudar a sempre melhorar, pedimos apenas 1 minutinho:
Clique aqui 👉 https://guiaairbnbpesquisa.streamlit.app/ e responda nossa pesquisa rápida.
Sua opinião é muito importante para nós! ❤
Muito obrigado!

---

Hello! 👋 We hope your stay was wonderful! 🌟
To help us keep improving, we kindly ask for just 1 minute:
Click here 👉 https://guiaairbnbpesquisa.streamlit.app/ and answer our quick survey.
Your opinion is very important to us! ❤
Thank you very much!

---

¡Hola! 👋 ¡Esperamos que tu estadía haya sido maravillosa! 🌟
Para ayudarnos a mejorar siempre, te pedimos solo 1 minutito:
Haz clic aquí 👉 https://guiaairbnbpesquisa.streamlit.app/ y responde nuestra encuesta rápida.
¡Tu opinión es muy importante para nosotros! ❤
¡Muchas gracias!""")

    # Link direto para o segundo app de pesquisa
    link_pesquisa = "https://guiaairbnbpesquisa.streamlit.app/"

    # Gerar e exibir o QR Code com o novo link
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf, format="PNG")
    buf.seek(0)  # necessário para leitura correta do buffer
    st.image(buf, caption="📱 Escaneie com a câmera do celular", use_container_width=False)

    # Exibir o link logo abaixo do QR Code
    st.markdown(f"""
        <div style="margin-top:20px; padding:10px; background-color:#f5f5f5; border-radius:8px; text-align:center;">
            <strong>Ou acesse diretamente:</strong><br>
            <a href="{link_pesquisa}" target="_blank">{link_pesquisa}</a>
        </div>
    """, unsafe_allow_html=True)
