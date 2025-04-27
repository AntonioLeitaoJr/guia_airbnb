import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# Escopos para acessar o Google Sheets
ESCOPO = ["https://www.googleapis.com/auth/spreadsheets"]

# Pega direto o dicionário do secret
info = st.secrets["GOOGLE_SHEETS_CREDENTIALS"]

# Cria as credenciais
credenciais = Credentials.from_service_account_info(info, scopes=ESCOPO)

# Autenticação com gspread
cliente = gspread.authorize(credenciais)

# Abertura da planilha
PLANILHA_ID = "1WNAVAuX0OykxQWScj7s5I7gWGBaWlyn8uceYy8wpuak"
planilha = cliente.open_by_key(PLANILHA_ID)

# Seleciona a aba principal
aba = planilha.sheet1

