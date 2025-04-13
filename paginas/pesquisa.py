import streamlit as st
from paginas.servico_sheets import aba

def exibir():
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
            <div class="pesquisa-titulo">📝 Pesquisa</div>
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
            aplicativo = st.selectbox("Qual o aplicativo de hospedagem?", ["Airbnb", "Booking", "Direto com o anfitrião", "Outros"])
        with col2:
            destaque = st.text_input("O que mais gostou (no condomínio e/ou no apartamento)?")
            melhoria = st.text_input("Algo que poderíamos melhorar?")
            perfil_ou_nome = st.text_input("Insira o link do seu perfil ou seu nome:")
        
        mensagem = st.text_area("Mensagem ou sugestão final:")

        enviar = st.form_submit_button("Enviar resposta")

        if enviar:
            try:
                dados = [gostou, destaque, melhoria, recomendaria, aplicativo, perfil_ou_nome, mensagem]
                aba.append_row(dados)
                st.success("✅ Obrigado! Sua resposta foi registrada com sucesso.")
            except Exception as e:
                st.error(f"❌ Erro ao salvar resposta: {e}")
