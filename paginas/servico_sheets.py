import gspread
from google.oauth2.service_account import Credentials

# Caminho da sua chave JSON
CAMINHO_CHAVE = "paginas/GOOGLESHEETS/guiaairbnbrespostas-fdad952e267a.json"

# Escopos necessários para edição do Google Sheets
ESCOPO = ["https://www.googleapis.com/auth/spreadsheets"]

# Criação das credenciais
credenciais = Credentials.from_service_account_file(CAMINHO_CHAVE, scopes=ESCOPO)

# Autenticação com gspread
cliente = gspread.authorize(credenciais)

# Abra a planilha pelo ID (copiado da URL do Google Sheets)
PLANILHA_ID = "1WNAVAuX0OykxQWScj7s5I7gWGBaWlyn8uceYy8wpuak"
planilha = cliente.open_by_key(PLANILHA_ID)

# Seleciona a primeira aba da planilha
aba = planilha.sheet1
