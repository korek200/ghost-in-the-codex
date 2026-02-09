import streamlit as st
import os
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA (Identidad Codex) ---
st.set_page_config(
    page_title="GHOST IN THE CODEX",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTÉTICA DE LUJO SILENCIOSO (Obsidiana & Oro) ---
st.markdown("""
    <style>
    /* Fondo General - Negro Obsidiana */
    .stApp {
        background-color: #0e0e0e;
        color: #e0e0e0;
    }
    /* Tipografía y Títulos */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #d4af37; /* Dorado Mate */
        font-weight: 300;
        letter-spacing: 2px;
    }
    /* Inputs y Áreas de Texto */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #333;
        border-radius: 0px;
    }
    /* Botones - Sutileza Jade */
    .stButton > button {
        background-color: #1a1a1a;
        color: #d4af37;
        border: 1px solid #d4af37;
        border-radius: 0px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #d4af37;
        color: #000000;
        border-color: #d4af37;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111111;
        border-right: 1px solid #222;
    }
    /* Separadores */
    hr {
        border-color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE SEGURIDAD ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def init_codex():
    if not GOOGLE_API_KEY:
        st.warning("⚠️ LLAVE MAESTRA NO DETECTADA. El Códice está en modo pasivo.")
        return False
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        return True
    except Exception as e:
        st.error(f"Error de conexión con el Oráculo: {e}")
        return False

codex_active = init_codex()

# --- INTERFAZ PRINCIPAL ---
st.title("G H O S T  IN  THE  C O D E X")
st.markdown("### LÁMINA I: INGESTA Y REFINACIÓN")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### 📂 DEPÓSITO DE ACTIVOS")
    uploaded_file = st.file_uploader("Cargar Documento (CSV/TXT)", label_visibility="collapsed")
    
    if uploaded_file:
        st.success(f"Archivo '{uploaded_file.name}' asimilado correctamente.")
        # Aquí iría la lógica de lectura de datos futura

with col2:
    st.markdown("#### 👁️ EL ORÁCULO (GEMINI)")
    query = st.text_area("Consulta estratégica:", height=100, placeholder="Escribe tu instrucción para el análisis de datos...")
    
    if st.button("EJECUTAR INTERPRETACIÓN"):
        if not codex_active:
            st.error("Protocolo detenido: Falta credencial.")
        elif not query:
            st.info("El silencio no genera respuestas.")
        else:
            with st.spinner("El Tlacuilo Digital está procesando..."):
                try:
                    # Forzamos la versión estable de la API para evitar el error 404
genai.configure(api_key=os.environ["GOOGLE_API_KEY"], transport='rest')
model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(query)
                    st.markdown("#### RESULTADO:")
                    st.markdown(f"> {response.text}")
                except Exception as e:
                    st.error(f"Fallo en la interpretación: {e}")

st.markdown("---")
st.caption("🔒 SOVEREIGN INFRASTRUCTURE | CDMX | 2025")
