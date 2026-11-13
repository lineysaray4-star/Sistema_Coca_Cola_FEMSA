import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos corregidos y optimizados
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo con imagen de planta industrial / producción */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
    }
    
    /* Contenedor principal del Login */
    .login-container {
        background: #FFFFFF;
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        border-top: 6px solid #F40009;
        margin-top: 3rem;
    }
    
    .badge-femsa {
        background-color: #F40009;
        color: white;
        padding: 6px 16px;
        border-radius: 4px;
        font-weight: 800;
        font-size: 1rem;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .login-title {
        font-weight: 800;
        color: #111111 !important;
        font-size: 1.3rem;
        margin-bottom: 0.3rem;
    }
    
    .login-subtitle {
        color: #555555 !important;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F40009;
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        padding: 0.7rem;
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
        # Usamos un contenedor nativo de Streamlit para evitar problemas con los bloques HTML
        with st.container():
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            
            # Cabecera visual
            st.markdown('<div style="text-align: center;"><span class="badge-femsa">COCA-COLA FEMSA</span></div>', unsafe_allow_html=True)
            st.markdown('<p class="login-title" style="text-align: center;">SISTEMA DE SOPORTE A DECISIONES</p>', unsafe_allow_html=True)
            st.markdown('<p class="login-subtitle" style="text-align: center;">Planta Barranquilla | Módulo CAPEX</p>', unsafe_allow_html=True)
            
            # Formulario limpio
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
