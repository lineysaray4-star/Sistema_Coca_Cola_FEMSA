import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos limpios y de alta legibilidad
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo con imagen limpia de botellas/bebidas y tono oscuro suave */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), 
                    url('https://images.unsplash.com/photo-1554866585-cd94860890b7?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
    }
    
    /* Tarjeta de login impecable, totalmente blanca y opaca */
    .login-card {
        background: #FFFFFF;
        padding: 2.5rem;
        border-radius: 14px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
        border-top: 6px solid #F40009;
        margin-top: 2rem;
    }
    
    .badge-femsa {
        background-color: #F40009;
        color: white;
        padding: 8px 18px;
        border-radius: 6px;
        font-weight: 800;
        font-size: 1.05rem;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 1.2rem;
    }
    
    .login-title {
        font-weight: 800;
        color: #111111 !important;
        font-size: 1.35rem;
        margin-bottom: 0.4rem;
        text-align: center;
    }
    
    .login-subtitle {
        color: #555555 !important;
        font-size: 0.95rem;
        margin-bottom: 1.8rem;
        font-weight: 600;
        text-align: center;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F40009;
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        padding: 0.75rem;
        transition: background 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #c50007;
        color: white;
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
    col1, col2, col3 = st.columns([1, 2.2, 1])
    
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Cabecera corporativa limpia
        st.markdown('<div style="text-align: center;"><span class="badge-femsa">COCA-COLA FEMSA</span></div>', unsafe_allow_html=True)
        st.markdown('<p class="login-title">SISTEMA DE SOPORTE A DECISIONES</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Planta Barranquilla | Módulo CAPEX</p>', unsafe_allow_html=True)
        
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
    st.success(f"¡Bienvenido, {st.session_state.usuario_actual}! Acceso concedido correctamente al sistema de la planta Barranquilla.")
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
