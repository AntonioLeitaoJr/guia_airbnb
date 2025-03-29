import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io
import os

# ⬇️ Detectar parâmetros da URL
query_params = st.experimental_get_query_params()
mostrar_pesquisa = query_params.get("pesquisa", ["nao"])[0].lower() == "sim"
mostrar_admin = query_params.get("admin", ["nao"])[0].lower() == "sim"

# ⬇️ Definir menu dinâmico
opcoes_menu = ["🏠 Boas-vindas", "📘 Guia do Imóvel", "🗺️ Mapa", "🎉 Eventos"]
if mostrar_pesquisa:
    opcoes_menu.append("📝 Pesquisa")
if mostrar_admin:
    opcoes_menu += ["📲 Enviar Pesquisa", "📊 Ver Respostas", "⚙️ Configurações"]

# ⬇️ Menu lateral com imagem
st.sidebar.image("simbolo_airbnb.jpg", width=100)
st.sidebar.title("Guia do Hóspede")
menu = st.sidebar.radio("Navegar para:", opcoes_menu)

# ------------------------------------------------------------------------------
# 📲 ABA: ENVIAR PESQUISA (ADMIN)
if menu == "📲 Enviar Pesquisa":
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📲 Enviar Pesquisa de Satisfação</h2>
            <p style="color:#eaeaea;text-align:center;">Copie o link abaixo e envie para o hóspede após o check-out.<br>Ou imprima o QR Code para deixar no apartamento.</p>
        </div>
    """, unsafe_allow_html=True)

    link_pesquisa = "https://guiaairbnbleitao.streamlit.app/?pesquisa=sim"
    st.code(link_pesquisa, language="text")

    st.code(link_pesquisa, language="text")

copiado = st.button("📋 Copiar Link da Pesquisa")
if copiado:
    st.toast("Link copiado! Agora é só colar.", icon="📎")
    st.write("")  # Apenas para manter o layout


    st.markdown("---")

    st.subheader("📱 QR Code para Avaliação")
    img_qr = qrcode.make(link_pesquisa)
    buf = io.BytesIO()
    img_qr.save(buf)
    st.image(buf, caption="Escaneie com a câmera do celular", use_container_width=False)

# ------------------------------------------------------------------------------
# 📊 ABA: VER RESPOSTAS (ADMIN)
elif menu == "📊 Ver Respostas":
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📊 Respostas Coletadas</h2>
            <p style="color:#eaeaea;text-align:center;">Visualize abaixo as respostas da pesquisa de satisfação.</p>
        </div>
    """, unsafe_allow_html=True)

    # Se o arquivo não existir ainda:
    if not os.path.exists("respostas.csv"):
        st.info("Ainda não há respostas registradas.")
    else:
        df = pd.read_csv("respostas.csv")
        st.dataframe(df, use_container_width=True)
        st.download_button("📂 Baixar Excel", data=df.to_csv(index=False), file_name="respostas.csv", mime="text/csv")

# ------------------------------------------------------------------------------
# ⚙️ ABA: CONFIGURAÇÕES (ADMIN)
elif menu == "⚙️ Configurações":
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">⚙️ Configurações do Sistema</h2>
            <p style="color:#eaeaea;text-align:center;">Aqui você poderá configurar o link público, QR Code, exportação e envio de dados futuramente.</p>
        </div>
    """, unsafe_allow_html=True)

    st.warning("Em breve: envio automático de respostas por e-mail, edição visual do QR e muito mais! ✨")


if menu == "🏠 Boas-vindas":
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





# Guia do Imóvel
elif menu == "📘 Guia do Imóvel":
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📘 Informações sobre o Imóvel</h2>
            <p style="color:#eaeaea;font-size:16px;">
                <strong>Wi-Fi:</strong> Rede: <code>BelémGuest</code> | Senha: <code>senhaboa2025</code><br><br>
                <p>
                <ul style="color:#eaeaea;font-size:16px;">
                <strong>Regras do condomínio:</strong><br>
                • Horário da piscina: 8h às 21h<br>
                • Sala de reuniões: agendar na portaria<br>
                • Silêncio entre 22h e 7h<br><br>
                <p>
                <strong>Outros detalhes:</strong><br>
                • Ar-condicionado: desligue ao sair<br>
                • Check-out: até às 11h<br>
                • Emergência: (91) 99999-9999
            </p>
        </div>
    """, unsafe_allow_html=True)



# Mapa
elif menu == "🗺️ Mapa":
    st.markdown("""
    <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
        <h2 style="color:#ff914d;text-align:center;">🗺️ Locais Úteis Próximos</h2>
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





# Eventos
elif menu == "🎉 Eventos":
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">🎉 Eventos em Belém</h2>
            <p style="color:#eaeaea;text-align:center;">
                Confira os eventos e atrações culturais que estão acontecendo na cidade durante o período da sua estadia!
            </p>
            <ul style="color:#eaeaea;font-size:16px;">
                <li>26 a 30 de março: Feira da Amazônia - Hangar</li>
                <li>27 de março: Show de MPB no Theatro da Paz</li>
                <li>28 de março: Feira Gastronômica na Estação das Docas</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)



# Pesquisa
elif menu == "📝 Pesquisa":
    st.markdown("""
        <style>
        .pesquisa-box {
            background-color: #262626;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .pesquisa-titulo {
            color: #ff914d;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .pesquisa-sub {
            color: #eaeaea;
            text-align: center;
            font-size: 16px;
            margin-bottom: 25px;
        }
        </style>

        <div class="pesquisa-box">
            <div class="pesquisa-titulo">📝 Pesquisa de Satisfação</div>
            <div class="pesquisa-sub">
                Agradecemos por sua estadia! Por favor, responda às perguntas abaixo. Sua opinião é muito importante.
            </div>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="pesquisa_form"):
        col1, col2 = st.columns(2)
        with col1:
            gostou = st.radio("Você gostou da hospedagem?", ["Sim", "Não"])
            recomendaria = st.radio("Você recomendaria este imóvel a outras pessoas?", ["Sim", "Não"])
            condominio = st.text_input("O que mais gostou no condomínio?")
        with col2:
            destaque = st.text_input("O que mais gostou?")
            melhoria = st.text_input("Algo que poderíamos melhorar?")
            mensagem = st.text_area("Mensagem ou sugestão final:")

        enviar = st.form_submit_button("Enviar resposta")

        if enviar:
            nova_resposta = pd.DataFrame([{
                "Gostou": gostou,
                "Destaque": destaque,
                "Melhoria": melhoria,
                "Recomendaria": recomendaria,
                "Condomínio": condominio,
                "Mensagem": mensagem
            }])
            try:
                nova_resposta.to_csv("respostas.csv", mode='a', header=False, index=False)
                st.success("✅ Obrigado! Sua resposta foi registrada com sucesso.")
            except Exception as e:
                st.error(f"❌ Erro ao salvar resposta: {e}")

