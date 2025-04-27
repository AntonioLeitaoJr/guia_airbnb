import gspread
import json
import streamlit as st
from google.oauth2.service_account import Credentials

ESCOPO = ["https://www.googleapis.com/auth/spreadsheets"]

info = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
credenciais = Credentials.from_service_account_info(info, scopes=ESCOPO)

cliente = gspread.authorize(credenciais)

PLANILHA_ID = "1WNAVAuX0OykxQWScj7s5I7gWGBaWlyn8uceYy8wpuak"
planilha = cliente.open_by_key(PLANILHA_ID)

aba = planilha.sheet1
