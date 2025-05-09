import streamlit as st
from paginas.servico_sheets import aba

def exibir():
    idioma = st.session_state.get("idioma", "pt")

    textos = {
        "pt": {
            "titulo": "Pesquisa",
            "sub": "Agradecemos por sua estadia! Por favor, responda às perguntas abaixo. Sua opinião é muito importante.",
            "gostou": "Você gostou da hospedagem?",
            "recomendaria": "Você recomendaria este imóvel a outras pessoas?",
            "aplicativo": "Qual o aplicativo de hospedagem?",
            "destaque": "O que mais gostou (no condomínio e/ou no apartamento)?",
            "melhoria": "Algo que poderíamos melhorar?",
            "perfil": "Insira o link do seu perfil ou seu nome:",
            "mensagem": "Mensagem ou sugestão final:",
            "enviar": "Enviar resposta"
        },
        "en": {
            "titulo": "Survey",
            "sub": "Thank you for your stay! Please answer the questions below. Your opinion is very important.",
            "gostou": "Did you enjoy your stay?",
            "recomendaria": "Would you recommend this place to others?",
            "aplicativo": "Which app did you use to book?",
            "destaque": "What did you like most (in the condo and/or apartment)?",
            "melhoria": "Anything we could improve?",
            "perfil": "Insert your profile link or your name:",
            "mensagem": "Final message or suggestion:",
            "enviar": "Submit response"
        },
        "es": {
            "titulo": "Encuesta",
            "sub": "¡Gracias por su estadía! Por favor, responda las siguientes preguntas. Su opinión es muy importante.",
            "gostou": "¿Le gustó la estadía?",
            "recomendaria": "¿Recomendaría este lugar a otras personas?",
            "aplicativo": "¿Qué aplicación utilizó para reservar?",
            "destaque": "¿Qué fue lo que más le gustó (en el condominio y/o en el apartamento)?",
            "melhoria": "¿Hay algo que podríamos mejorar?",
            "perfil": "Coloque el enlace de su perfil o su nombre:",
            "mensagem": "Mensaje o sugerencia final:",
            "enviar": "Enviar respuesta"
        }
    }

    t = textos[idioma]

    st.markdown(f"""
        <style>
        .pesquisa-box {{
            background-color: #262626;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }}
        .pesquisa-titulo {{
            color: #ff914d;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .pesquisa-sub {{
            color: #eaeaea;
            text-align: center;
            font-size: 16px;
            margin-bottom: 25px;
        }}
        </style>

        <div class="pesquisa-box">
            <div class="pesquisa-titulo">📝 {t["titulo"]}</div>
            <div class="pesquisa-sub">{t["sub"]}</div>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="pesquisa_form"):
        col1, col2 = st.columns(2)
        with col1:
        # Opções de "Sim" e "Não"
            opcoes_sim_nao = {"pt": ["Sim", "Não"], "en": ["Yes", "No"], "es": ["Sí", "No"]}[idioma]
            reverso_sim_nao = {"Sim": "Sim", "Não": "Não", "Yes": "Sim", "No": "Não", "Sí": "Sim"}

            gostou_visual = st.radio(t["gostou"], opcoes_sim_nao)
            recomendaria_visual = st.radio(t["recomendaria"], opcoes_sim_nao)

            gostou = reverso_sim_nao[gostou_visual]
            recomendaria = reverso_sim_nao[recomendaria_visual]

        # Opções do aplicativo de hospedagem
            opcoes_apps = {
                "pt": ["Airbnb", "Booking", "Direto com o anfitrião", "Outros"],
                "en": ["Airbnb", "Booking", "Direct with the host", "Others"],
                "es": ["Airbnb", "Booking", "Directo con el anfitrión", "Otros"]
            }
            reverso_apps = {
                "Airbnb": "Airbnb",
                "Booking": "Booking",
                "Direto com o anfitrião": "Direto com o anfitrião",
                "Outros": "Outros",
                "Direct with the host": "Direto com o anfitrião",
                "Others": "Outros",
                "Directo con el anfitrión": "Direto com o anfitrião",
                "Otros": "Outros"
            }

            aplicativo_visual = st.selectbox(t["aplicativo"], opcoes_apps[idioma])
            aplicativo = reverso_apps[aplicativo_visual]
        
        with col2:
            destaque = st.text_input(t["destaque"])
            melhoria = st.text_input(t["melhoria"])
            perfil_ou_nome = st.text_input(t["perfil"])
        
        mensagem = st.text_area(t["mensagem"])

        enviar = st.form_submit_button(t["enviar"])

        if enviar:
            try:
                dados = [gostou, destaque, melhoria, recomendaria, aplicativo, perfil_ou_nome, mensagem]
                aba.append_row(dados)
                st.success("✅ Obrigado! Sua resposta foi registrada com sucesso.")
            except Exception as e:
                st.error(f"❌ Erro ao salvar resposta: {e}")
