import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

from config import get_planilha_id

ESCOPO = ["https://www.googleapis.com/auth/spreadsheets"]


@st.cache_resource(show_spinner=False)
def get_aba():
    if "GOOGLE_SHEETS_CREDENTIALS" not in st.secrets:
        raise RuntimeError("Credenciais do Google Sheets não configuradas.")

    info = st.secrets["GOOGLE_SHEETS_CREDENTIALS"]
    credenciais = Credentials.from_service_account_info(info, scopes=ESCOPO)
    cliente = gspread.authorize(credenciais)
    planilha = cliente.open_by_key(get_planilha_id())
    return planilha.sheet1


def append_resposta(dados: list[str]) -> None:
    get_aba().append_row(dados)


def listar_respostas() -> list[list[str]]:
    return get_aba().get_all_values()
