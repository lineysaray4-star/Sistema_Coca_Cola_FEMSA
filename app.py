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
logo_base64 = ""
try:
  logo_str = get_base64_of_bin_file("logo_coca.png")
  logo_base64 = logo_str
  logo_html = f'<img src="data:image/png;base64,{logo_str}" style="height: 1.3em; vertical-align: middle; margin: 0 4px; display: inline-block;">'
except:
  pass

# Estilos CSS robustos para el modo oscuro fijo y diseño corporativo
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
        width: 220px !important;
        display: block !important;
        margin: 1.5rem auto 0 auto !important;
        border: none !important;
    }}
    
    [data-testid="stFormSubmitButton"] button:hover {{
        background-color: #c50007 !important;
        box-shadow: 0 4px 12px rgba(244, 0, 9, 0.4);
    }}

    /* Tarjetas contenedoras para el panel principal */
    .dashboard-card {{
        background: rgba(20, 20, 20, 0.90);
        padding: 2rem;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        border-left: 6px solid #F40009;
        margin-bottom: 1.5rem;
    }}

    /* Estilo tipo Post-it / Nota para el Mural */
    .mural-card {{
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        border-top: 5px solid #F40009;
        color: #111111 !important;
        margin-bottom: 1.2rem;
        height: 100%;
    }}
    .mural-card * {{
        color: #222222 !important;
    }}
    .mural-title {{
        font-weight: 800;
        font-size: 1.1rem;
        color: #F40009 !important;
        margin-bottom: 0.5rem;
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

if "lista_proyectos" not in st.session_state:
  st.session_state.lista_proyectos = []

if "menu_actual" not in st.session_state:
  st.session_state.menu_actual = "🏠 Inicio / Resumen"

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
    # 1. Imagen arriba del todo en la barra lateral
    if st.session_state.menu_actual == "🏠 Inicio / Resumen":
      st.image(
          "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=300&auto=format&fit=crop&q=80",
          use_container_width=True,
      )
    else:
      if logo_base64:
        st.markdown(
            f"""
                <div style="text-align: center; padding: 0.2rem 0 0.8rem 0;">
                    <img src="data:image/png;base64,{logo_base64}" style="width: 90%; max-width: 190px;">
                </div>
                """,
            unsafe_allow_html=True,
        )
      else:
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
            "📌 Mural de Proyectos",
            "⚙️ Optimización Multiperiodo",
            "📊 Reportes & Brief",
        ],
        key="menu_actual",
    )

    st.markdown("---")
    if st.button("🚪 Cerrar Sesión"):
      st.session_state.autenticado = False
      st.rerun()

  # ------------------------------------------
  # INICIO / RESUMEN
  # ------------------------------------------
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

    total_proyectos = len(st.session_state.lista_proyectos)
    presupuesto_total = sum(
        p.get("capex", 0) for p in st.session_state.lista_proyectos
    )

    col1, col2, col3 = st.columns(3)
    with col1:
      st.metric(label="Proyectos Registrados", value=str(total_proyectos))
    with col2:
      st.metric(
          label="Presupuesto Asignado ($ USD)",
          value=f"${presupuesto_total:,.0f}".replace(",", "."),
      )
    with col3:
      st.metric(label="Estado del Sistema", value="Activo")

  # ------------------------------------------
  # REGISTRO DE PROYECTOS (BRIEF MGIP + AHP 0-10 ENTEROS)
  # ------------------------------------------
  elif menu == "📋 Registro de Proyectos":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>Registro y Gestión de Proyectos CAPEX</h2>
            <p style="margin-top: 0.5rem; color: #CCCCCC;">
                Complete el formulario de Brief MGIP corporativo y evalúe los criterios AHP de la iniciativa.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Formulario completo Brief MGIP
    with st.form("form_brief_mgip"):
      st.markdown("### 📝 Captura de Brief (Estándar ServiceNow MGIP)")

      col_a, col_b = st.columns(2)
      with col_a:
        fecha_sol = st.date_input("Fecha de Solicitud")
        nombre_sol = st.text_input(
            "Nombre del Solicitante", value=st.session_state.usuario_actual
        )
        tipo_iniciativa = st.selectbox(
            "Tipo de Iniciativa",
            [
                "Renovación por Obsolescencia",
                "Upgrade / Actualización Electrónica",
                "Seguridad, Calidad & Ambiental",
                "Infraestructura / Facilities",
                "ESG / Sostenibilidad",
                "Productividad / Incremento de Capacidad",
            ],
        )
        pais_sol = st.text_input("País Solicitante", value="Colombia")
        area_sol = st.selectbox(
            "Área / Ubicación (Modelo 3D Planta)",
            [
                "Línea 1 (L1)",
                "Línea 2 (L2)",
                "Línea 3 (L3)",
                "Línea 4 (L4)",
                "Soplado",
                "Embotellado / Llenadora",
                "Paletizado / Empacadora",
                "Jarabe / Preparación",
                "Almacén / Bodega",
                "Servicios Industriales (SCI)",
                "Tratamiento de Agua",
            ],
        )

      with col_b:
        anio_ejec = st.selectbox("Año de Ejecución", [2026, 2027, 2028])
        prioridad_est = st.selectbox(
            "Prioridades Estratégicas (Pilar)",
            [
                "Continuidad Operativa",
                "Eficiencia y Rentabilidad",
                "Seguridad y Sostenibilidad KORE",
            ],
        )
        incluida_bp = st.checkbox("¿Incluida en BP Nueva Iniciativa?")
        capex_usd = st.number_input(
            "Inversión Inicial Aproximada CAPEX (USD)",
            min_value=0.0,
            step=5000.0,
            value=0.0,
        )
        opex_usd = st.number_input(
            "Inversión Inicial Aproximada OPEX (USD)",
            min_value=0.0,
            step=1000.0,
            value=0.0,
        )

      st.markdown("---")
      st.markdown("#### ⚙️ Generación de Nomenclatura del Requerimiento")
      st.markdown(
          "*Normativa (Máx. 40 caracteres): Acción + Equipo/Zona + Línea + BQA"
          " (Ej: Reemplazo Compresor L2 BQA)*"
      )

      col_n1, col_n2, col_n3 = st.columns(3)
      with col_n1:
        accion_nom = st.selectbox(
            "Acción",
            [
                "Reemplazo",
                "Adecuación",
                "Ampliación",
                "Adquisición",
                "Instalación",
                "Reingeniería",
            ],
        )
      with col_n2:
        equipo_nom = st.text_input(
            "Equipo / Zona / Detalle", placeholder="Ej. Compresor Amoniaco"
        )
      with col_n3:
        linea_nom = st.selectbox(
            "Línea", ["L1", "L2", "L3", "L4", "General"]
        )

      nomenclatura_generada = (
          f"{accion_nom} {equipo_nom} {linea_nom} BQA"[:40]
          if equipo_nom.strip()
          else "Pendiente de definir"
      )

      st.markdown(
          f"""
            <div style="background: rgba(30, 30, 30, 0.95); padding: 0.8rem 1rem; border-radius: 8px; border-left: 4px solid #F40009; margin: 0.5rem 0 1rem 0;">
                <span style="color: #FFFFFF !important; font-size: 0.95rem;">📌 <b>Nombre del Requerimiento Resultante:</b> {nomenclatura_generada}</span>
            </div>
            """,
          unsafe_allow_html=True,
      )

      st.markdown("---")
      st.markdown(
          "#### 🎯 Evaluación Multicriterio AHP (Puntuación de 0 a 10"
          " enteros)"
      )
      st.markdown(
          "Califique el impacto de la iniciativa en cada uno de los 7"
          " criterios corporativos ponderados:"
      )

      c1 = st.slider(
          "1. Seguridad y cumplimiento normativo (Peso: 31.97%)", 0, 10, 5, 1
      )
      c2 = st.slider(
          "2. Rentabilidad y optimización de recursos (Peso: 20.53%)",
          0,
          10,
          5,
          1,
      )
      c3 = st.slider(
          "3. Continuidad operativa y salud de activos (Peso: 18.94%)",
          0,
          10,
          5,
          1,
      )
      c4 = st.slider(
          "4. Alineación estratégica y LRP (Peso: 13.99%)", 0, 10, 5, 1
      )
      c5 = st.slider(
          "5. Gestión de riesgos técnicos y operacionales (Peso: 8.72%)",
          0,
          10,
          5,
          1,
      )
      c6 = st.slider(
          "6. Complejidad y desafíos de ejecución técnica (Peso: 3.83%)",
          0,
          10,
          5,
          1,
      )
      c7 = st.slider(
          "7. Impacto en el servicio y desarrollo humano (Peso: 2.02%)",
          0,
          10,
          5,
          1,
      )

      ahp_score_calculado = (
          (c1 * 0.3197)
          + (c2 * 0.2053)
          + (c3 * 0.1894)
          + (c4 * 0.1399)
          + (c5 * 0.0872)
          + (c6 * 0.0383)
          + (c7 * 0.0202)
      )
      score_entero = int(round(ahp_score_calculado))

      st.markdown(
          f"""
            <div style="background: rgba(30, 30, 30, 0.95); padding: 0.8rem 1rem; border-radius: 8px; border-left: 4px solid #F40009; margin: 0.5rem 0 1rem 0;">
                <span style="color: #FFFFFF !important; font-size: 0.95rem;">📊 <b>Puntaje Ponderado AHP Calculado:</b> {score_entero} / 10</span>
            </div>
            """,
          unsafe_allow_html=True,
      )

      st.markdown("---")
      st.markdown("#### 📄 Secciones Descriptivas del Brief")
      antecedentes = st.text_area(
          "Antecedentes",
          placeholder=(
              "Describir situación actual, causa del problema, afectación"
              " al negocio y por qué..."
          ),
      )
      objetivo = st.text_area(
          "Objetivo",
          placeholder=(
              "Indicar propósito a alcanzar y relación con el corredor"
              " estratégico..."
          ),
      )
      descripcion_req = st.text_area(
          "Descripción del Requerimiento",
          placeholder="Qué voy a cambiar y cómo lo quiero resolver...",
      )
      expectativas = st.text_area(
          "Expectativas / Criterios de Aceptación / Calidad / Beneficio Esperado",
          placeholder=(
              "Criterios que definen el éxito del proyecto, impacto en KPIs,"
              " puesta en marcha..."
          ),
      )
      riesgos = st.text_area(
          "Riesgos",
          placeholder=(
              "Riesgos detectados (cuantitativos/cualitativos) y qué pasa"
              " si no se ejecuta el cambio..."
          ),
      )

      btn_submit_brief = st.form_submit_button("🚀 Enviar Registro")

      if btn_submit_brief:
        if not equipo_nom.strip():
          st.error(
              "Por favor indique el equipo o detalle para la nomenclatura."
          )
        elif capex_usd <= 0:
          st.error("El monto CAPEX debe ser mayor a 0.")
        else:
          nuevo_proyecto = {
              "nombre": nomenclatura_generada,
              "fecha": str(fecha_sol),
              "solicitante": nombre_sol,
              "tipo": tipo_iniciativa,
              "area": area_sol,
              "anio": anio_ejec,
              "capex": capex_usd,
              "opex": opex_usd,
              "ahp": score_entero,
              "antecedentes": antecedentes,
              "objetivo": objetivo,
              "descripcion": descripcion_req,
              "expectativas": expectativas,
              "riesgos": riesgos,
          }
          st.session_state.lista_proyectos.append(nuevo_proyecto)
          st.success(
              f"¡Proyecto '{nomenclatura_generada}' registrado exitosamente"
              f" con AHP {score_entero}/10 y subido al mural!"
          )

  # ------------------------------------------
  # MURAL DE PROYECTOS
  # ------------------------------------------
  elif menu == "📌 Mural de Proyectos":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>📌 Mural de Proyectos CAPEX - Planta Barranquilla</h2>
            <p style="margin-top: 0.5rem; color: #CCCCCC;">
                Vista general de iniciativas registradas en formato de notas informativas del equipo.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if len(st.session_state.lista_proyectos) > 0:
      cols = st.columns(3)
      for idx, proj in enumerate(st.session_state.lista_proyectos):
        col_actual = cols[idx % 3]
        with col_actual:
          st.markdown(
              f"""
                    <div class="mural-card">
                        <div class="mural-title">#{idx + 1} | {proj['nombre']}</div>
                        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><b>📅 Fecha:</b> {proj['fecha']} ({proj['anio']})</p>
                        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><b>👤 Solicitante:</b> {proj['solicitante']}</p>
                        <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><b>📍 Área:</b> {proj['area']}</p>
                        <hr style="margin: 0.5rem 0; border-color: #ddd;">
                        <p style="font-size: 0.85rem; margin-bottom: 0.3rem;"><b>💰 CAPEX:</b> ${proj['capex']:,.0f}</p>
                        <p style="font-size: 0.85rem; margin-bottom: 0.3rem;"><b>🔧 OPEX:</b> ${proj['opex']:,.0f}</p>
                        <p style="font-size: 0.85rem; margin-bottom: 0.5rem;"><b>🎯 AHP Score:</b> {proj['ahp']} / 10</p>
                        <details style="font-size: 0.8rem; color: #444;">
                            <summary style="cursor: pointer; font-weight: bold; color: #F40009;">Ver resumen de Brief</summary>
                            <p style="margin-top: 0.4rem;"><b>Objetivo:</b> {proj['objetivo'][:120]}...</p>
                            <p><b>Riesgos:</b> {proj['riesgos'][:120]}...</p>
                        </details>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

      st.markdown("<br>", unsafe_allow_html=True)
      if st.button("🗑️ Limpiar Todos los Proyectos del Mural"):
        st.session_state.lista_proyectos = []
        st.rerun()
    else:
      st.info(
          "📭 El mural está vacío actualmente. Ve a la sección '📋 Registro de"
          " Proyectos' para capturar el primer brief."
      )

  # ------------------------------------------
  # OPTIMIZACIÓN MULTIPERIODO
  # ------------------------------------------
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

  # ------------------------------------------
  # REPORTES & BRIEF
  # ------------------------------------------
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
