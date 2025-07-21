Torre Evidence Digital Guide - README
Introduction
Welcome to the official repository of 'Torre Evidence Digital Guide' - a smart and multilingual hospitality
assistant built with Streamlit. This web application was designed to improve the guest experience in
short-term rentals by offering a complete, interactive, and real-time updated digital guide.
Access the app: https://guiaairbnbleitao.streamlit.app/
Survey-only version: https://guiaairbnbpesquisa.streamlit.app/?pesquisa=sim
Features
- Digital Guest Manual
- Interactive Map with Tourist Spots
- Updated List of Local Events
- Cleaning and Check-in Instructions
- Multilingual Interface (Portuguese, English, Spanish)
- Admin Area for Content Editing
- Guest Feedback Survey Integration
- Export responses to Google Sheets (automatically)
- QR Code generation for survey sharing
Technologies Used
- Python 3.10+
- Streamlit
- Pandas
- Google Sheets API
- QRCode (PIL + qrcode)
- GitHub + Streamlit Cloud for deployment
How to Run Locally
Clone the repository:
git clone https://github.com/AntonioLeitaoJr/guia_airbnb.git
cd guia_airbnb
(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py
Don't forget to add your credentials.json (Google service account key) and configure necessary access to
Google Sheets.
Live Version
- Main App: https://guiaairbnbleitao.streamlit.app/
- Survey Only Mode: https://guiaairbnbpesquisa.streamlit.app/?pesquisa=sim
Project Structure
guia_airbnb/
 app.py
 eventos.txt
 guia.txt
 imagens/
 idiomas/
 pt.py
 en.py
 es.py
 paginas/
 guia_imovel.py
 eventos.py
 pesquisa.py
 servico_sheets/
 auth.py
 integracao.py
Contact
If you'd like to contribute, give feedback, or report an issue, feel free to reach out:
- GitHub: @AntonioLeitaoJr
- Email: leitaoprogrammer@gmail.com
License
This project is currently private and under development. License will be defined upon public release.
