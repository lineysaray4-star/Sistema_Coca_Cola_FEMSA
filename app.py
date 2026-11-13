import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos para la pantalla de login
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), 
                    url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
    }
    
    .login-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        border-top: 5px solid #F40009;
        margin-top: 5rem;
    }
    
    .login-title {
        font-weight: 800;
        color: #1F1F1F;
        font-size: 1.4rem;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    
    .login-subtitle {
        color: #666;
        text-align: center;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F40009;
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        padding: 0.6rem;
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

# Inicializar el estado de autenticación en la sesión
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Pantalla de Login
if not st.session_state.autenticado:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Logo o marca visual corporativa
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="background-color: #F40009; color: white; padding: 6px 14px; border-radius: 4px; font-weight: 800; font-size: 1.1rem; letter-spacing: 1px;">COCA-COLA FEMSA</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown('<p class="login-title">SISTEMA DE SOPORTE A DECISIONES</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-subtitle">Planta Barranquilla | Módulo CAPEX</p>', unsafe_allow_html=True)
        
        # Formulario de acceso
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
    # Pantalla temporal post-login para verificar que funciona perfectamente
    st.success(f"¡Bienvenido, {st.session_state.usuario_actual}! Acceso concedido correctamente al sistema de la planta Barranquilla.")
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
