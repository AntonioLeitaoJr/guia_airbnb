# Torre Evidence Digital Guide

## Introduction

Welcome to the official repository of **Torre Evidence Digital Guide** — a smart and multilingual hospitality assistant built with Streamlit. This web application improves the guest experience in short-term rentals by offering an interactive digital guide.

- Main app: https://guiaairbnbleitao.streamlit.app/
- Survey-only version: https://guiaairbnbpesquisa.streamlit.app/?pesquisa=sim

## Features

- Digital guest manual
- Interactive map with tourist spots
- Updated list of local events
- Cleaning and check-in instructions
- Multilingual interface: Portuguese, English and Spanish
- Admin area for content editing and survey links
- Guest feedback survey integration
- Export responses from Google Sheets
- QR Code generation for survey sharing

## Technologies Used

- Python 3.10+
- Streamlit
- Pandas
- Google Sheets API
- QRCode (PIL + qrcode)
- GitHub + Streamlit Cloud for deployment

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/AntonioLeitaoJr/guia_airbnb.git
cd guia_airbnb
```

Create a virtual environment, if desired:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows, activate it with:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the main app:

```bash
streamlit run app.py
```

Run the survey redirect app:

```bash
streamlit run app_pesquisa.py
```

## Configuration

Configure these values in Streamlit secrets when deploying:

```toml
ADMIN_PASSWORD = "change-me"
APP_URL = "https://guiaairbnbleitao.streamlit.app/"
PESQUISA_URL = "https://guiaairbnbpesquisa.streamlit.app/"
GOOGLE_SHEETS_SPREADSHEET_ID = "spreadsheet-id"

[GOOGLE_SHEETS_CREDENTIALS]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "..."
client_email = "..."
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "..."
```

## Project Structure

```text
guia_airbnb/
├── app.py
├── app_pesquisa.py
├── config.py
├── idiomas.py
├── requirements.txt
├── paginas/
│   ├── admin_config.py
│   ├── admin_enviar.py
│   ├── admin_respostas.py
│   ├── boas_vindas.py
│   ├── componentes.py
│   ├── eventos.py
│   ├── guia_imovel.py
│   ├── mapa.py
│   ├── pesquisa.py
│   ├── servico_sheets.py
│   └── textos_idiomas/
│       ├── eventos_en.txt
│       ├── eventos_es.txt
│       ├── eventos_pt.txt
│       ├── guia_imovel_en.txt
│       ├── guia_imovel_es.txt
│       └── guia_imovel_pt.txt
├── simbolo_airbnb.jpg
└── torre_evidence.jpg
```

## Notes

The editable guide and events content is stored in local text files. On Streamlit Cloud, changes made through the admin interface may not persist after redeploys or restarts. For long-term content management, use an external storage service such as Google Sheets, a database or another persistent backend.

## Contact

- GitHub: @AntonioLeitaoJr
- Email: leitaoprogrammer@gmail.com

## License

This project is currently private and under development. License will be defined upon public release.
