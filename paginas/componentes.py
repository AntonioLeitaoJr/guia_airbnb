import io

import qrcode
import streamlit as st


def aplicar_estilo_global() -> None:
    """Aplica uma identidade visual mais moderna e responsiva ao app."""
    st.set_page_config(
        page_title="Guia Torre Evidence",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

        :root {
            --brand: #ff5a5f;
            --brand-2: #ff914d;
            --ink: #17202a;
            --muted: #667085;
            --card: rgba(255, 255, 255, 0.92);
            --line: rgba(23, 32, 42, 0.10);
            --shadow: 0 18px 45px rgba(16, 24, 40, 0.12);
        }

        html, body, [class*="css"] {
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 90, 95, 0.16), transparent 32rem),
                radial-gradient(circle at top right, rgba(255, 145, 77, 0.18), transparent 30rem),
                linear-gradient(180deg, #fff8f5 0%, #f7f9fc 52%, #ffffff 100%);
            color: var(--ink);
        }

        .main .block-container {
            max-width: 1180px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1f2937 0%, #111827 100%);
            color: #f9fafb;
        }

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {
            color: #f9fafb !important;
        }

        .stButton > button,
        .stDownloadButton > button,
        div[data-testid="stFormSubmitButton"] button {
            border: 0;
            border-radius: 999px;
            background: linear-gradient(135deg, var(--brand), var(--brand-2));
            color: white;
            font-weight: 700;
            box-shadow: 0 10px 24px rgba(255, 90, 95, 0.22);
            transition: transform .15s ease, box-shadow .15s ease, filter .15s ease;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        div[data-testid="stFormSubmitButton"] button:hover {
            color: white;
            filter: brightness(1.04);
            transform: translateY(-1px);
            box-shadow: 0 14px 30px rgba(255, 90, 95, 0.28);
        }

        .hero-card, .modern-card, .content-card, .metric-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 28px;
            box-shadow: var(--shadow);
            backdrop-filter: blur(12px);
        }

        .hero-card {
            overflow: hidden;
            margin-bottom: 1.25rem;
        }

        .hero-image {
            min-height: 340px;
            background-size: cover;
            background-position: center;
            position: relative;
        }

        .hero-image::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(90deg, rgba(15, 23, 42, 0.70), rgba(15, 23, 42, 0.18));
        }

        .hero-content {
            position: absolute;
            inset: auto 24px 24px 24px;
            z-index: 2;
            color: white;
            max-width: 760px;
        }

        .eyebrow {
            display: inline-flex;
            gap: 8px;
            align-items: center;
            padding: 7px 12px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.28);
            font-size: 0.86rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: clamp(2rem, 5vw, 4rem);
            font-weight: 800;
            line-height: 1.02;
            margin: 0;
            letter-spacing: -0.05em;
        }

        .hero-subtitle {
            color: rgba(255, 255, 255, 0.9);
            font-size: clamp(1rem, 2vw, 1.2rem);
            margin-top: 14px;
        }

        .modern-card {
            padding: 28px;
            margin-bottom: 20px;
        }

        .modern-card h2 {
            color: var(--ink);
            text-align: center;
            font-size: clamp(1.6rem, 3vw, 2.4rem);
            letter-spacing: -0.04em;
            margin: 0 0 8px;
        }

        .modern-card p, .content-card p {
            color: var(--muted);
            text-align: center;
            font-size: 1rem;
            margin: 0;
        }

        .content-card {
            padding: 28px;
            margin: 18px 0;
        }

        .quick-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
            margin: 18px 0 8px;
        }

        .metric-card {
            padding: 20px;
        }

        .metric-card strong {
            display: block;
            font-size: 1rem;
            color: var(--ink);
            margin-bottom: 6px;
        }

        .metric-card span {
            color: var(--muted);
            font-size: 0.94rem;
        }

        .map-frame iframe {
            border: 0;
            border-radius: 24px;
            box-shadow: var(--shadow);
        }

        @media (max-width: 760px) {
            .quick-grid { grid-template-columns: 1fr; }
            .hero-image { min-height: 430px; }
            .hero-content { inset: auto 18px 18px 18px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def cabecalho_card(titulo: str, descricao: str | None = None) -> None:
    descricao_html = f"<p>{descricao}</p>" if descricao else ""
    st.markdown(
        f"""
        <div class="modern-card">
            <h2>{titulo}</h2>
            {descricao_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def mostrar_qr_code(link: str, caption: str = "📱 Escaneie com a câmera do celular") -> None:
    img_qr = qrcode.make(link)
    buf = io.BytesIO()
    img_qr.save(buf, format="PNG")
    buf.seek(0)
    col1, col2, col3 = st.columns([1, 1.1, 1])
    with col2:
        st.image(buf, caption=caption, use_container_width=True)
