import streamlit as st

def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">📘 Guia do Imóvel</h2>
            <p style="color:#eaeaea;font-size:16px;">
                <strong>Wi-Fi:</strong> Rede: <code>BelémGuest</code> | Senha: <code>senhaboa2025</code><br><br>
                <p>
                <ul style="color:#eaeaea;font-size:16px;">
                <strong>Regras do condomínio:</strong><br>
                • Horário da piscina: 8h às 21h<br>
                • Sala de reuniões: agendar na portaria<br>
                • Silêncio entre 22h e 7h<br><br>
                <p>
                <strong>Outros detalhes:</strong><br>
                • Ar-condicionado: desligue ao sair<br>
                • Check-out: até às 11h<br>
                • Emergência: (91) 99999-9999
            </p>
        </div>
    """, unsafe_allow_html=True)
