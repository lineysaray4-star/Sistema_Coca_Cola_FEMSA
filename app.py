import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos con diseño industrial y máxima visibilidad
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo industrial moderno con textura y gradiente corporativo */
    .stApp {
        background: radial-gradient(circle at center, #1e1e1e 0%, #0d0d0d 100%);
        background-size: cover;
        background-position: center;
    }
    
    /* Tarjeta de login impecable y flotante */
    .login-card {
        background: #FFFFFF;
        padding: 3rem;
        border-radius: 18px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        margin-top: 3.5rem;
        border-top: 6px solid #F40009;
    }
    
    .badge-femsa {
        background-color: #F40009;
        color: white;
        padding: 8px 22px;
        border-radius: 10px;
        font-weight: 900;
        font-size: 1.2rem;
        letter-spacing: 1.8px;
        display: inline-block;
        margin-bottom: 1.5rem;
    }
    
    /* Títulos en blanco brillante para destacar sobre el fondo oscuro */
    .login-title {
        font-weight: 800;
        color: #FFFFFF !important;
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
        text-align: center;
        letter-spacing: 0.5px;
    }
    
    .login-subtitle {
        color: #E0E0E0 !important;
        font-size: 1.05rem;
        margin-bottom: 2.2rem;
        font-weight: 600;
        text-align: center;
    }
    
    .stTextInput > div > div > input {
        color: #333;
        font-size: 1.0rem;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F40009;
        color: white;
        font-weight: 800;
        border: none;
        border-radius: 10px;
        padding: 0.9rem;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        letter-spacing: 0.8px;
    }
    
    .stButton>button:hover {
        background-color: #c50007;
        color: white;
        box-shadow: 0 6px 15px rgba(244, 0, 9, 0.4);
        transform: translateY(-1px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inicializar estado de sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Pantalla de Login
if not st.session_state.autenticado:
    col1, col2, col3 = st.columns([1, 2.6, 1])
    
    with col2:
        # Cabecera de títulos fuera de la tarjeta blanca para que se lean perfecto en blanco
        st.markdown('<p class="login-title">SISTEMA DE SOPORTE A DECISIONES</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Planta Barranquilla | Módulo CAPEX</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Logo o insignia visual
        st.markdown('<div style="text-align: center;"><span class="badge-femsa">COCA-COLA FEMSA</span></div>', unsafe_allow_html=True)
        
        # Campos del formulario
        usuario = st.text_input("Usuario", placeholder="Ingrese su usuario")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("INICIAR SESIÓN"):
            if usuario.strip() != "" and password == "CocaCola2026":
                st.session_state.autenticado = True
                st.session_state.usuario_actual = usuario
                st.rerun()
            else:
                st.error("Credenciales incorrectas. Verifique usuario y contraseña.")
                
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # Pantalla temporal post-login para verificar
    st.success(f"¡Bienvenido, {st.session_state.usuario_actual}! Acceso concedido correctamente al sistema de la planta Barranquilla.")
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
