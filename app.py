import base64
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Función para cargar la imagen local de fondo de forma segura
def get_base64_of_bin_file(bin_file):
  with open(bin_file, "rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()


# Intentar cargar la imagen local 'fabrica.jpg'
background_css = ""
try:
  bin_str = get_base64_of_bin_file("fabrica.jpg")
  background_css = f"""
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
except:
  background_css = """
    .stApp {{
        background: radial-gradient(circle at center, #1e1e1e 0%, #0d0d0d 100%);
    }}
    """

# Estilos CSS corporativos
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    {background_css}
    
    /* Tarjeta de login */
    .login-card {{
        background: rgba(255, 255, 255, 0.98);
        padding: 3rem;
        border-radius: 18px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        margin-top: 2rem;
        border-top: 6px solid #F40009;
    }}
    
    .badge-femsa {{
        background-color: #F40009;
        color: white;
        padding: 8px 22px;
        border-radius: 10px;
        font-weight: 900;
        font-size: 1.2rem;
        letter-spacing: 1.8px;
        display: inline-block;
        margin-bottom: 1.5rem;
    }}
    
    .login-title {{
        font-weight: 800;
        color: #FFFFFF !important;
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }}
    
    .login-subtitle {{
        color: #FFFFFF !important;
        font-size: 1.05rem;
        margin-bottom: 2rem;
        font-weight: 600;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }}
    
    .stTextInput > div > div > input {{
        color: #333;
        font-size: 1.0rem;
    }}
    
    /* Centrar y estilizar el botón de inicio de sesión */
    .stButton {{
        display: flex;
        justify-content: center;
    }}
    
    .stButton>button {{
        width: 70%;
        background-color: #F40009;
        color: white;
        font-weight: 800;
        border: none;
        border-radius: 10px;
        padding: 0.8rem;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        letter-spacing: 0.8px;
        margin: 0 auto;
        display: block;
    }}
    
    .stButton>button:hover {{
        background-color: #c50007;
        color: white;
        box-shadow: 0 6px 15px rgba(244, 0, 9, 0.4);
        transform: translateY(-1px);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicializar estado de sesión
if "autenticado" not in st.session_state:
  st.session_state.autenticado = False

# ==========================================
# 1. PANTALLA DE LOGIN
# ==========================================
if not st.session_state.autenticado:
  col1, col2, col3 = st.columns([1, 2.6, 1])

  with col2:
    st.markdown(
        '<p class="login-title">SISTEMA DE SOPORTE A DECISIONES</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="login-subtitle">Planta Barranquilla | Módulo CAPEX</p>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align: center;"><span class="badge-femsa">COCA-COLA'
        " FEMSA</span></div>",
        unsafe_allow_html=True,
    )

    usuario = st.text_input("Usuario", placeholder="Ej. Ing. Alejandra")
    password = st.text_input(
        "Contraseña", type="password", placeholder="••••••••"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("INICIAR SESIÓN"):
      # Contraseña general: CocaCola2026 / Usuario cualquiera no vacío
      if usuario.strip() != "" and password == "CocaCola2026":
        st.session_state.autenticado = True
        st.session_state.usuario_actual = usuario
        st.rerun()
      else:
        st.error(
            "Credenciales incorrectas. Verifique que la contraseña sea"
            " CocaCola2026."
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 2. APLICACIÓN PRINCIPAL (POST-LOGIN)
# ==========================================
else:
  # Menú lateral de navegación
  with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300&auto=format&fit=crop&q=80",
        use_container_width=True,
    )
    st.markdown(f"### 👤 Usuario: **{st.session_state.usuario_actual}**")
    st.markdown("---")

    menu = st.radio(
        "Navegación del Sistema",
        [
            "🏠 Inicio / Resumen",
            "📋 Registro de Proyectos",
            "⚙️ Optimización Multiperiodo",
            "📊 Reportes & Brief",
        ],
    )

    st.markdown("---")
    if st.button("🚪 Cerrar Sesión"):
      st.session_state.autenticado = False
      st.rerun()

  # Contenido según la opción del menú seleccionado
  if menu == "🏠 Inicio / Resumen":
    st.title("🏭 Planta Coca-Cola FEMSA - Barranquilla")
    st.subheader("Sistema de Soporte a Decisiones (DSS) para Portafolio CAPEX")

    st.markdown(
        """
        Bienvenido al sistema gerencial de optimización y priorización de proyectos de inversión. 
        Utilice el menú lateral para navegar entre el registro de iniciativas, la ejecución del motor de optimización y la generación de reportes para el brief corporativo.
        """
    )

    # Métricas rápidas de ejemplo
    col1, col2, col3 = st.columns(3)
    with col1:
      st.metric(
          label="Proyectos Registrados", value="0", delta="Pendiente de carga"
      )
    with col2:
      st.metric(label="Presupuesto Asignado ($)", value="$0", delta="Estable")
    with col3:
      st.metric(
          label="Estado del Sistema", value="Activo", delta="Conectado a Planta"
      )

  elif menu == "📋 Registro de Proyectos":
    st.title("📋 Registro y Gestión de Proyectos CAPEX")
    st.info(
        "Aquí es donde crearemos el formulario para registrar los proyectos con"
        " sus costos, puntajes AHP y restricciones."
    )

  elif menu == "⚙️ Optimización Multiperiodo":
    st.title("⚙️ Motor de Optimización Multiperiodo (MILP)")
    st.info(
        "Aquí implementaremos el motor matemático de selección de portafolio y"
        " visualización de cronogramas."
    )

  elif menu == "📊 Reportes & Brief":
    st.title("📊 Generación de Reportes y Brief en Excel")
    st.info(
        "Aquí colocaremos el botón de descarga en formato Excel para el brief"
        " corporativo."
    )
