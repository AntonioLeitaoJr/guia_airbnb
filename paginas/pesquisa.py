import streamlit as st
from paginas.servico_sheets import aba

def exibir():
    idioma = st.session_state.get("idioma", "pt")

    textos = {
        "pt": {
            "titulo": "Pesquisa",
            "subtitulo": "Agradecemos por sua estadia! Por favor, responda às perguntas abaixo. Sua opinião é muito importante.",
            "gostou": "Você gostou da hospedagem?",
            "recomendaria": "Você recomendaria este imóvel a outras pessoas?",
            "destaque": "O que mais gostou (no condomínio e/ou no apartamento)?",
            "melhoria": "Algo que poderíamos melhorar?",
            "aplicativo": "Qual o aplicativo de hospedagem?",
            "perfil": "Insira o link do seu perfil ou seu nome:",
            "mensagem": "Mensagem ou sugestão final:",
            "enviar": "Enviar resposta",
            "sucesso": "✅ Obrigado! Sua resposta foi registrada com sucesso.",
            "erro": "❌ Erro ao salvar resposta:"
        },
        "en": {
            "titulo": "Survey",
            "subtitulo": "Thank you for your stay! Please answer the questions below. Your opinion is very important.",
            "gostou": "Did you enjoy your stay?",
            "recomendaria": "Would you recommend this place to others?",
            "destaque": "What did you like most (in the condo and/or apartment)?",
            "melhoria": "Anything we could improve?",
            "aplicativo": "Which app did you use to book?",
            "perfil": "Insert your profile link or your name:",
            "mensagem": "Final message or suggestion:",
            "enviar": "Submit response",
            "sucesso": "✅ Thank you! Your response has been recorded successfully.",
            "erro": "❌ Error saving response:"
        },
        "es": {
            "titulo": "Encuesta",
            "subtitulo": "¡Gracias por su estadía! Por favor, responda las preguntas a continuación. Su opinión es muy importante.",
            "gostou": "¿Le gustó la estadía?",
            "recomendaria": "¿Recomendaría esta propiedad a otras personas?",
            "destaque": "¿Qué fue lo que más le gustó (del condominio y/o del apartamento)?",
            "melhoria": "¿Algo que podríamos mejorar?",
            "aplicativo": "¿Qué aplicación utilizó para reservar?",
            "perfil": "Ingrese el enlace de su perfil o su nombre:",
            "mensagem": "Mensaje o sugerencia final:",
            "enviar": "Enviar respuesta",
            "sucesso": "✅ ¡Gracias! Su respuesta ha sido registrada con éxito.",
            "erro": "❌ Error al guardar la respuesta:"
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
            <div class="pesquisa-titulo">📝 {t['titulo']}</div>
            <div class="pesquisa-sub">{t['subtitulo']}</div>
        </div>
    """, unsafe_allow_html=True)

    with st.form(key="pesquisa_form"):
        col1, col2 = st.columns(2)
        with col1:
            gostou = st.radio(t["gostou"], ["Sim", "Não"])
            recomendaria = st.radio(t["recomendaria"], ["Sim", "Não"])
            aplicativo = st.selectbox(t["aplicativo"], ["Airbnb", "Booking", "Direto com o anfitrião", "Outros"])
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
                st.success(t["sucesso"])
            except Exception as e:
                st.error(f"{t['erro']} {e}")
