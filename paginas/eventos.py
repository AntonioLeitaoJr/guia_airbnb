import streamlit as st
import os

# 1️⃣ Obter idioma atual da sessão (padrão: pt)
idioma = st.session_state.get("idioma", "pt")

# 2️⃣ Montar caminho correto do arquivo
CAMINHO_ARQUIVO = os.path.join("paginas", "textos_idiomas", f"eventos_{idioma}.txt")

# 3️⃣ Conteúdo padrão caso o arquivo ainda não exista
def conteudo_padrao():
    return {
        "pt": """
🎉 Eventos

Confira os eventos e atrações culturais que estão acontecendo na cidade durante o período da sua estadia!

- 2 de maio: Festa "Emo Vive | Especial Paramore + Avril Lavigne" - Studio Pub
- 3 de maio: Show da banda Vanguart - Teatro Estação Gasômetro
- 4 de maio: Evento "nocapz. - Okka" - Casa Namata
- 8 de maio: Stand-up "Comedy Norte" - Bosque Sport Bar & Bowling
- 9 de maio: Show de Geraldo Azevedo - Assembleia Paraense
- 10 de maio: Show "Mulher" - Teatro do Sesi
- 10 de maio: Show de Henry Freitas - Estádio Olímpico do Pará (Mangueirão)
- 11 de maio: Show "Meu Canto Amazônico" com Nilson Chaves - Parque Cultural Vila Maguary
- 15 de maio: Espetáculo "Zona Desconforto" - Teatro Maria Sylvia Nunes
- 16 e 17 de maio: Espetáculo "Pérolas Musicais - Tributo à Jovem Guarda" - Teatro do Sesi
- 17 de maio: Show da banda Capital Inicial - Assembleia Paraense
- 17 de maio: Evento "Mixtape: dominATE" - Ice Bode
- 29 de abril: Show "Tecendo Mel" com Rafael Du Vale - Teatro Experimental Waldemar Henrique
- 30 de maio a 1º de junho: 4º Encontro Cidades da Amazônia e do Brasil - Teatro Estação Gasômetro
- 27 a 28 de maio: 1º Congresso de Enfermagem - Hospital Adventista de Belém
- 10 a 11 de junho: XVIII Congresso Notarial e Registral do Pará - Estação das Docas
- 5 a 7 de junho: 1º Congresso Norte de Cirurgia Bariátrica e Metabólica - Hotel Princesa Louçã
- 6 de junho: Show "Tiê canta Cartas de Amor" - Belém
- 8 de junho: Palestra "Como viver um dia perfeito" com Lúcia Helena Galvão - Centro de Convenções Princesa Louçã
- 7 de junho: DevOpsDays Belém 2025 - Shopping Pátio Belém
- 8 de novembro: Global Citizen Festival: Amazônia 2025 com Alok - Estádio Olímpico do Pará (Mangueirão)
- 12 a 14 de dezembro: Psica Festival 2025 com Gaby Amarantos - Estádio Olímpico do Pará (Mangueirão)

🌿 COP 30 - Conferência das Nações Unidas sobre Mudanças Climáticas

- 19 a 23 de maio: Semana do Clima UNFCCC - Belém
- Outubro (data a definir): Pré-COP - Brasil
- 10 a 21 de novembro: COP 30 - Belém, Pará

🙏 Círio de Nazaré 2025

- 12 de outubro: Procissão principal do Círio de Nazaré - Belém
- 2 a 24 de outubro: Programação cultural e religiosa do Círio - Belém

🏆 Eventos Esportivos em Belém com Relevância Nacional e Internacional

- 12 de janeiro: Super Copa Grão-Pará 2025 - Estádio Mangueirão
- 2 de fevereiro: Supercopa Rei 2025 - Estádio Mangueirão
- 6 de abril: Corrida e Caminhada da Cooperação Belém 2025 - Belém
- 18 de maio: LIVE! RUN XP Belém 2025 - Portal da Amazônia
- 24 de maio: Belém Night Run Red Sky - Belém
- 4 de maio: Corrida ALEPA 2025 - Belém
- 13 de abril: Corrida da Amazônia - Belém
- 30 de março: Corrida do Fogo 2025 – Etapa Ananindeua
- 9 de março: Corrida Mulheres em Movimento - Belém
- 16 de fevereiro: 2ª Corrida Rei da Amazônia - Belém
- 9 de fevereiro: Corrida 10 Anos La Carrera - Belém
- 2 de fevereiro: 7ª Corrida Lobos da Amazônia - Belém
- 12 de janeiro: Corrida de Belém 2025 - Belém

""",
        "en": """
🎉 Events

Check out the cultural events and attractions happening in the city during your stay!

- May 2: "Emo Vive | Paramore + Avril Lavigne Special" party - Studio Pub
- May 3: Vanguart band concert - Teatro Estação Gasômetro
- May 4: "nocapz. - Okka" event - Casa Namata
- May 8: "Comedy Norte" stand-up show - Bosque Sport Bar & Bowling
- May 9: Geraldo Azevedo concert - Assembleia Paraense
- May 10: "Mulher" show - Teatro do Sesi
- May 10: Henry Freitas concert - Estádio Mangueirão
- May 11: "Meu Canto Amazônico" with Nilson Chaves - Parque Cultural Vila Maguary
- May 15: "Zona Desconforto" performance - Teatro Maria Sylvia Nunes
- May 16–17: "Pérolas Musicais - Tribute to Jovem Guarda" show - Teatro do Sesi
- May 17: Capital Inicial band concert - Assembleia Paraense
- May 17: "Mixtape: dominATE" event - Ice Bode
- April 29: "Tecendo Mel" show with Rafael Du Vale - Teatro Experimental Waldemar Henrique
- May 30 to June 1: 4th Meeting of Amazonian and Brazilian Cities - Teatro Estação Gasômetro
- May 27–28: 1st Nursing Congress - Adventist Hospital of Belém
- June 10–11: 18th Notarial and Registry Congress of Pará - Estação das Docas
- June 5–7: 1st Northern Congress of Bariatric and Metabolic Surgery - Hotel Princesa Louçã
- June 6: "Tiê sings Love Letters" show - Belém
- June 8: "How to Live a Perfect Day" lecture with Lúcia Helena Galvão - Princesa Louçã Convention Center
- June 7: DevOpsDays Belém 2025 - Pátio Belém Shopping
- November 8: Global Citizen Festival: Amazon 2025 with Alok - Estádio Mangueirão
- December 12–14: Psica Festival 2025 with Gaby Amarantos - Estádio Mangueirão

🌿 COP 30 - United Nations Climate Change Conference

- May 19–23: UNFCCC Climate Week - Belém
- October (date to be defined): Pre-COP - Brazil
- November 10–21: COP 30 - Belém, Pará

🙏 Círio de Nazaré 2025

- October 12: Main procession of Círio de Nazaré - Belém
- October 2–24: Cultural and religious programming of Círio - Belém

🏆 Sports Events in Belém with National and International Relevance

- January 12: Super Copa Grão-Pará 2025 - Mangueirão Stadium
- February 2: Supercopa Rei 2025 - Mangueirão Stadium
- April 6: Cooperation Run and Walk Belém 2025 - Belém
- May 18: LIVE! RUN XP Belém 2025 - Portal da Amazônia
- May 24: Belém Night Run Red Sky - Belém
- May 4: ALEPA Run 2025 - Belém
- April 13: Amazon Run - Belém
- March 30: Fire Run 2025 – Ananindeua Stage
- March 9: Women in Movement Run - Belém
- February 16: 2nd Amazon King Run - Belém
- February 9: 10 Years La Carrera Run - Belém
- February 2: 7th Amazon Wolves Run - Belém
- January 12: Belém Run 2025 - Belém

""",
        "es": """
🎉 Eventos

¡Consulta los eventos y atracciones culturales que están ocurriendo en la ciudad durante tu estadía!

- 2 de mayo: Fiesta "Emo Vive | Especial Paramore + Avril Lavigne" - Studio Pub
- 3 de mayo: Concierto de la banda Vanguart - Teatro Estação Gasômetro
- 4 de mayo: Evento "nocapz. - Okka" - Casa Namata
- 8 de mayo: Stand-up "Comedy Norte" - Bosque Sport Bar & Bowling
- 9 de mayo: Concierto de Geraldo Azevedo - Assembleia Paraense
- 10 de mayo: Espectáculo "Mulher" - Teatro do Sesi
- 10 de mayo: Concierto de Henry Freitas - Estadio Olímpico do Pará (Mangueirão)
- 11 de mayo: Show "Meu Canto Amazônico" con Nilson Chaves - Parque Cultural Vila Maguary
- 15 de mayo: Espectáculo "Zona Desconforto" - Teatro Maria Sylvia Nunes
- 16 y 17 de mayo: Espectáculo "Pérolas Musicais - Tributo a la Jovem Guarda" - Teatro do Sesi
- 17 de mayo: Concierto de la banda Capital Inicial - Assembleia Paraense
- 17 de mayo: Evento "Mixtape: dominATE" - Ice Bode
- 29 de abril: Show "Tecendo Mel" con Rafael Du Vale - Teatro Experimental Waldemar Henrique
- 30 de mayo al 1º de junio: 4º Encuentro Ciudades de la Amazonía y de Brasil - Teatro Estação Gasômetro
- 27 al 28 de mayo: 1º Congreso de Enfermería - Hospital Adventista de Belém
- 10 al 11 de junio: XVIII Congreso Notarial y Registral de Pará - Estação das Docas
- 5 al 7 de junio: 1º Congreso del Norte de Cirugía Bariátrica y Metabólica - Hotel Princesa Louçã
- 6 de junio: Concierto "Tiê canta Cartas de Amor" - Belém
- 8 de junio: Conferencia "Cómo vivir un día perfecto" con Lúcia Helena Galvão - Centro de Convenciones Princesa Louçã
- 7 de junio: DevOpsDays Belém 2025 - Shopping Pátio Belém
- 8 de noviembre: Global Citizen Festival: Amazonía 2025 con Alok - Estadio Olímpico do Pará (Mangueirão)
- 12 al 14 de diciembre: Psica Festival 2025 con Gaby Amarantos - Estadio Olímpico do Pará (Mangueirão)

🌿 COP 30 - Conferencia de las Naciones Unidas sobre el Cambio Climático

- 19 al 23 de mayo: Semana del Clima UNFCCC - Belém
- Octubre (fecha por definir): Pre-COP - Brasil
- 10 al 21 de noviembre: COP 30 - Belém, Pará

🙏 Círio de Nazaré 2025

- 12 de octubre: Procesión principal del Círio de Nazaré - Belém
- 2 al 24 de octubre: Programación cultural y religiosa del Círio - Belém

🏆 Eventos Deportivos en Belém con Relevancia Nacional e Internacional

- 12 de enero: Supercopa Grão-Pará 2025 - Estadio Mangueirão
- 2 de febrero: Supercopa Rey 2025 - Estadio Mangueirão
- 6 de abril: Carrera y Caminata de la Cooperación Belém 2025 - Belém
- 18 de mayo: LIVE! RUN XP Belém 2025 - Portal da Amazônia
- 24 de mayo: Belém Night Run Red Sky - Belém
- 4 de mayo: Carrera ALEPA 2025 - Belém
- 13 de abril: Carrera de la Amazonía - Belém
- 30 de marzo: Carrera del Fuego 2025 – Etapa Ananindeua
- 9 de marzo: Carrera Mujeres en Movimiento - Belém
- 16 de febrero: 2ª Carrera Rey de la Amazonía - Belém
- 9 de febrero: Carrera 10 Años La Carrera - Belém
- 2 de febrero: 7ª Carrera Lobos de la Amazonía - Belém
- 12 de enero: Carrera de Belém 2025 - Belém
"""
    }.get(idioma, "Conteúdo ainda não cadastrado.")

# 4️⃣ Exibir conteúdo
def exibir():
    st.markdown("""
        <div style="background-color:#262626;padding:30px;border-radius:15px;box-shadow:2px 2px 12px rgba(0,0,0,0.3);margin-bottom:20px;">
            <h2 style="color:#ff914d;text-align:center;">🎉 Eventos</h2>
    """, unsafe_allow_html=True)

    # Criar o arquivo com conteúdo padrão se não existir
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            f.write(conteudo_padrao())

    # Carregar e exibir conteúdo
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        conteudo = f.read()

    st.markdown(conteudo, unsafe_allow_html=True)

    st.markdown("""</div>""", unsafe_allow_html=True)

    # 5️⃣ Modo admin: permite editar o texto
    if st.session_state.get("modo_admin"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("✏️ Editar lista de eventos")
        novo_conteudo = st.text_area("", conteudo, height=400)
        if st.button("💾 Salvar alterações"):
            with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            st.success("Eventos atualizados com sucesso! ✅")
