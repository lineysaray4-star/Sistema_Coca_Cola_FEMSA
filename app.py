import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilos CSS corporativos con fondo de fábrica y textos blancos
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Fondo con imagen de línea de envasado industrial de Coca-Cola y tono oscuro suave */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1595889835846-6d472ac3f665?q=80&w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Tarjeta de login limpia */
    .login-card {
        background: rgba(255, 255, 255, 0.98);
        padding: 3rem;
        border-radius: 18px;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.5);
        margin-top: 4rem;
        border: 1px solid #e0e0e0;
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
        margin-bottom: 1.8rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    }
    
    /* Títulos en color BLANCO para máxima visibilidad sobre el fondo industrial */
    .login-title {
        font-weight: 800;
        color: #FFFFFF !important;
        font-size: 1.6rem;
        margin-bottom: 0.6rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9); /* Sombra fuerte para destacar */
    }
    
    .login-subtitle {
        color: #FFFFFF !important;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-weight: 600;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9); /* Sombra fuerte para destacar */
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
        box-shadow: 0 6px 15px rgba(0,0,0,0.4);
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
    # Usamos columnas para centrar la tarjeta
    col1, col2, col3 = st.columns([1, 2.6, 1])
    
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Cabecera visual
        st.markdown('<div style="text-align: center;"><span class="badge-femsa">COCA-COLA FEMSA</span></div>', unsafe_allow_html=True)
        
        # Títulos en blanco con sombra fuerte, ahora sí se ven sobre la fábrica
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
    # Pantalla temporal post-login para verificar
    st.success(f"¡Bienvenido, {st.session_state.usuario_actual}! Acceso concedido correctamente al sistema de la planta Barranquilla.")
    
    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
