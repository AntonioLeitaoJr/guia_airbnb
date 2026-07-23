import streamlit as st

from paginas.componentes import cabecalho_card
from password_admin import (
    senha_admin_configurada_localmente,
    atualizar_senha_admin,
    verificar_senha_admin,
)

TAMANHO_MINIMO_SENHA = 6


def exibir():
    cabecalho_card(
        "👤 Perfil do Admin",
        "Atualize sua senha de administrador com segurança, sem sair da área restrita.",
    )

    if senha_admin_configurada_localmente():
        st.info("A senha atual está salva no armazenamento local seguro do app.")
    else:
        st.info("A senha atual ainda é a senha configurada nos secrets do Streamlit.")

    with st.form("form_alterar_senha_admin"):
        senha_atual = st.text_input("Senha atual", type="password")
        nova_senha = st.text_input("Nova senha", type="password")
        confirmar_senha = st.text_input("Confirmar nova senha", type="password")
        enviar = st.form_submit_button("Salvar nova senha")

    if not enviar:
        return

    if not senha_atual or not nova_senha or not confirmar_senha:
        st.error("Preencha todos os campos para alterar a senha.")
        return

    if not verificar_senha_admin(senha_atual):
        st.error("A senha atual informada está incorreta.")
        return

    if len(nova_senha) < TAMANHO_MINIMO_SENHA:
        st.error(f"A nova senha deve ter pelo menos {TAMANHO_MINIMO_SENHA} caracteres.")
        return

    if nova_senha != confirmar_senha:
        st.error("A confirmação não confere com a nova senha.")
        return

    if verificar_senha_admin(nova_senha):
        st.error("A nova senha deve ser diferente da senha atual.")
        return

    atualizar_senha_admin(nova_senha)
    st.session_state["tentativas_login"] = 0
    st.success("Senha do administrador alterada com sucesso!")
