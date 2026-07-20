import streamlit as st

APP_URL_PADRAO = "https://guiaairbnbleitao.streamlit.app/"
PESQUISA_URL_PADRAO = "https://guiaairbnbpesquisa.streamlit.app/"
PLANILHA_ID_PADRAO = "1WNAVAuX0OykxQWScj7s5I7gWGBaWlyn8uceYy8wpuak"


def get_config(nome: str, padrao: str | None = None) -> str | None:
    try:
        return st.secrets.get(nome, padrao)
    except Exception:
        return padrao


def get_app_url() -> str:
    return get_config("APP_URL", APP_URL_PADRAO) or APP_URL_PADRAO


def get_pesquisa_url() -> str:
    return get_config("PESQUISA_URL", PESQUISA_URL_PADRAO) or PESQUISA_URL_PADRAO


def get_planilha_id() -> str:
    return get_config("GOOGLE_SHEETS_SPREADSHEET_ID", PLANILHA_ID_PADRAO) or PLANILHA_ID_PADRAO
