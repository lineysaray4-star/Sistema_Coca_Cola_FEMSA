import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos con máxima legibilidad
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo con imagen de fábrica real de Coca-Cola y tono oscuro suave */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)), 
                    url('https://images.unsplash.com/photo-1629967341764-055d7f4d1002?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
    }
    
    /* Tarjeta de login limpia */
    .login-card {
        background: rgba(255, 255, 255, 0.97);
        padding: 2.8rem;
        border-radius: 16px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
        margin-top: 3rem;
    }
    
    .badge-femsa {
        background-color: #F40009;
        color: white;
        padding: 8px 20px;
        border-radius: 8px;
        font-weight: 900;
        font-size: 1.1rem;
        letter-spacing: 1.5px;
        display: inline-block;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Títulos en color BLANCO para máxima visibilidad sobre el fondo oscuro */
    .login-title {
        font-weight: 800;
        color: #FFFFFF !important;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.7); /* Sombra para que resalten */
    }
    
    .login-subtitle {
        color: #FFFFFF !important;
        font-size: 1.0rem;
        margin-bottom: 2rem;
        font-weight: 600;
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.7); /* Sombra para que resalten */
    }
    
    .stTextInput > div > div > input {
        color: #333;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #F40009;
        color: white;
        font-weight: 800;
        border: none;
        border-radius: 8px;
        padding: 0.8rem;
        transition: all 0.3s ease;
        font-size: 1.0rem;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        background-color: #c50007;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
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
    col1, col2, col3 = st.columns([1, 2.4, 1])
    
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Cabecera visual
        st.markdown('<div style="text-align: center;"><span class="badge-femsa">COCA-COLA FEMSA</span></div>', unsafe_allow_html=True)
        
        # Títulos en blanco con sombra, ahora sí se ven
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
