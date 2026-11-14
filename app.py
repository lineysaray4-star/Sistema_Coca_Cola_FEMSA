import base64
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Coca-Cola FEMSA | DSS CAPEX Barranquilla",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Función para cargar archivos locales en base64 de forma segura
def get_base64_of_bin_file(bin_file):
  with open(bin_file, "rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()


# Cargar la imagen de fondo de la fábrica (fabrica.jpg)
background_css = ""
try:
  bin_str = get_base64_of_bin_file("fabrica.jpg")
  background_css = f"""
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), 
                    url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
except:
  background_css = """
    .stApp {{
        background: #0e1117;
    }}
    """

# Cargar el logo de Coca-Cola (logo_coca.png)
logo_html = '<span class="coca-cola-font">Coca-Cola</span>'
try:
  logo_str = get_base64_of_bin_file("logo_coca.png")
  logo_html = f'<img src="data:image/png;base64,{logo_str}" style="height: 1.3em; vertical-align: middle; margin: 0 4px; display: inline-block;">'
except:
  pass

# Estilos CSS robustos para bloquear el modo oscuro y asegurar contraste
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    {background_css}
    
    /* Forzar colores de texto generales en blanco */
    .stMarkdown, p, span, label, h1, h2, h3, h4 {{
        color: #FFFFFF !important;
    }}
    
    /* Estilizar el formulario nativo de login */
    [data-testid="stForm"] {{
        background: rgba(255, 255, 255, 0.98);
        padding: 2.2rem;
        border-radius: 16px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
        border-top: 6px solid #F40009 !important;
        border-left: none !important;
        border-right: none !important;
        border-bottom: none !important;
        max-width: 420px;
        margin: 0 auto;
    }}
    
    [data-testid="stForm"] label, [data-testid="stForm"] p, [data-testid="stForm"] span {{
        color: #333333 !important;
    }}
    
    .badge-femsa {{
        background-color: #F40009;
        color: white !important;
        padding: 6px 18px;
        border-radius: 8px;
        font-weight: 900;
        font-size: 1.1rem;
        letter-spacing: 1.5px;
        display: inline-block;
        margin-bottom: 1.2rem;
    }}
    
    .login-title {{
        font-weight: 800;
        color: #FFFFFF !important;
        font-size: 1.5rem;
        margin-bottom: 0.4rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }}
    
    .login-subtitle {{
        color: #FFFFFF !important;
        font-size: 1rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
    }}
    
    [data-testid="stFormSubmitButton"] button {{
        background-color: #F40009 !important;
        color: white !important;
        font-weight: 800 !important;
        border-radius: 8px !important;
        padding: 0.65rem !important;
        width: 180px !important;
        display: block !important;
        margin: 1.5rem auto 0 auto !important;
        border: none !important;
    }}
    
    [data-testid="stFormSubmitButton"] button:hover {{
        background-color: #c50007 !important;
        box-shadow: 0 4px 12px rgba(244, 0, 9, 0.4);
    }}

    [data-testid="stTextInput"] button {{
        background-color: transparent !important;
        color: #555555 !important;
        border: none !important;
    }}
    
    [data-testid="stTextInput"] button svg {{
        fill: #555555 !important;
    }}

    /* Tarjetas contenedoras para el panel principal */
    .dashboard-card {{
        background: rgba(20, 20, 20, 0.85);
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        border-left: 6px solid #F40009;
        margin-bottom: 1.5rem;
    }}

    .plant-title {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        font-size: 1.8rem;
    }}

    .barranquilla-text {{
        font-size: 0.85em;
        font-weight: 700 !important;
    }}

    /* Estilo profesional para las métricas */
    [data-testid="stMetric"] {{
        background: rgba(20, 20, 20, 0.85);
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 5px solid #F40009;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
    }}
    [data-testid="stMetricLabel"] {{
        color: #E0E0E0 !important;
        font-weight: 600 !important;
    }}
    [data-testid="stMetricValue"] {{
        color: #F40009 !important;
        font-weight: 800 !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }}
    
    /* Barra lateral fija en modo oscuro */
    [data-testid="stSidebar"] {{
        background-color: #111111 !important;
    }}
    [data-testid="stSidebar"] * {{
        color: #FFFFFF !important;
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
  col1, col2, col3 = st.columns([1, 1.4, 1])

  with col2:
    st.markdown(
        '<p class="login-title">SISTEMA DE SOPORTE A DECISIONES</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="login-subtitle">Planta Barranquilla | Módulo CAPEX</p>',
        unsafe_allow_html=True,
    )

    with st.form("login_form"):
      st.markdown(
          '<div style="text-align: center;"><span'
          ' class="badge-femsa">COCA-COLA FEMSA</span></div>',
          unsafe_allow_html=True,
      )

      usuario = st.text_input("Usuario", placeholder="Ej. Ing. Alejandra")
      password = st.text_input(
          "Contraseña", type="password", placeholder="••••••••"
      )

      submitted = st.form_submit_button("INICIAR SESIÓN")

      if submitted:
        if usuario.strip() != "" and password == "CocaCola2026":
          st.session_state.autenticado = True
          st.session_state.usuario_actual = usuario
          st.rerun()
        else:
          st.error(
              "Credenciales incorrectas. Verifique que la contraseña sea"
              " CocaCola2026."
          )

# ==========================================
# 2. APLICACIÓN PRINCIPAL (POST-LOGIN)
# ==========================================
else:
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

  if menu == "🏠 Inicio / Resumen":
    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="plant-title"><b>Planta {logo_html} FEMSA - <span class="barranquilla-text">Barranquilla</span></b></div>
            <p style="margin-top: 1rem; font-weight: 600; color: #FFFFFF; font-size: 1.1rem;">
                ¡Bienvenido al sistema!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
      st.metric(label="Proyectos Registrados", value="0")
    with col2:
      st.metric(label="Presupuesto Asignado ($)", value="$0")
    with col3:
      st.metric(label="Estado del Sistema", value="Activo")

  elif menu == "📋 Registro de Proyectos":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>📋 Registro y Gestión de Proyectos CAPEX</h2>
            <p style="margin-top: 1rem;">Aquí crearemos el formulario para registrar los proyectos con sus costos, puntajes AHP y restricciones.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  elif menu == "⚙️ Optimización Multiperiodo":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>⚙️ Motor de Optimización Multiperiodo (MILP)</h2>
            <p style="margin-top: 1rem;">Aquí implementaremos el motor matemático de selección de portafolio y visualización de cronogramas.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  elif menu == "📊 Reportes & Brief":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>📊 Generación de Reportes y Brief en Excel</h2>
            <p style="margin-top: 1rem;">Aquí colocaremos el botón de descarga en formato Excel para el brief corporativo.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
