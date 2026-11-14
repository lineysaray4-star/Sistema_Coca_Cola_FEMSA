import base64
import plotly.express as px
import pandas as pd
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

# Estilos CSS robustos para el modo oscuro fijo y visibilidad total de textos
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    {background_css}
    
    /* Forzar colores de texto generales en blanco para máxima visibilidad */
    .stMarkdown, p, span, label, h1, h2, h3, h4, 
    .stRadio label, .stCheckbox label, .stSelectbox label, 
    .stNumberInput label, .stTextInput label, .stDateInput label, .stSlider label {{
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

# Inicializar estados de sesión
if "autenticado" not in st.session_state:
  st.session_state.autenticado = False

if "lista_proyectos" not in st.session_state:
  st.session_state.lista_proyectos = []

if "menu_actual" not in st.session_state:
  st.session_state.menu_actual = "🏠 Inicio / Resumen"

# Valores predeterminados (escala 0-100 basados en los pesos originales de Excel)
VALORES_EXCEL_DEFAULT = {
    "Seguridad y cumplimiento normativo": 31.97,
    "Rentabilidad y optimización de recursos": 20.53,
    "Continuidad operativa y salud de activos": 18.94,
    "Alineación estratégica y LRP": 13.99,
    "Gestión de riesgos técnicos y operacionales": 8.72,
    "Complejidad y desafíos de ejecución técnica": 3.83,
    "Impacto en el servicio y desarrollo humano": 2.02,
}

# Inicializar los valores de los sliders en session_state si no existen
for key, default_val in VALORES_EXCEL_DEFAULT.items():
  session_key = f"slider_{key}"
  if session_key not in st.session_state:
    st.session_state[session_key] = default_val

# Lista oficial de los 20 lugares de la planta
LUGARES_PLANTA = [
    "Nave L6",
    "Ed. Administrativo",
    "Preparación Jarabes",
    "Nave L5",
    "PTAP",
    "Maquinaria Auxiliar",
    "Almacén Materia Prima",
    "Taller de Mantenimiento",
    "Almacén PT en planta",
    "Almacén central",
    "Almacén Seco y Refrigerado",
    "CIP 2",
    "Laboratorios",
    "Bodega de Almacenamiento",
    "Almacén PT",
    "Planta de Aguas Residuales",
    "Línea San Martín",
    "Línea Krones",
    "Línea Simonazzi",
    "Línea Caraballo",
]

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
            "⚙️ Configuración AHP",
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
  # CONFIGURACIÓN AHP (BARRAS 0-100 + PALETA DE COLORES VARIADA + DONUT CHART)
  # ------------------------------------------
  elif menu == "⚙️ Configuración AHP":
    st.markdown(
        """
        <div class="dashboard-card">
            <h2>⚙️ Configuración y Ponderación de Criterios AHP</h2>
            <p style="margin-top: 0.8rem; color: #CCCCCC; line-height: 1.6;">
                <b>Instrucciones:</b> Deslice las barras corporativas en una escala de 0 a 100 para definir el nivel de importancia que considera para cada criterio. Con base en estos valores, el sistema calculará automáticamente el peso ponderado real (normalizado al 100%) que se aplicará en las evaluaciones de los proyectos. <br><br>
                Si desea volver a los parámetros originales, haga clic en el botón inferior para restaurar instantáneamente los valores predeterminados de Excel.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Botón para cargar los valores predeterminados de Excel y actualizar todo automáticamente
    if st.button("🔄 Cargar Valores Predeterminados (Excel)"):
      for key, default_val in VALORES_EXCEL_DEFAULT.items():
        st.session_state[f"slider_{key}"] = default_val
      st.success(
          "¡Valores predeterminados de Excel restaurados con éxito en las"
          " barras y el gráfico circular!"
      )
      st.rerun()

    st.markdown("### 🎚️ Nivel de Importancia por Criterio (0 a 100)")

    # Capturar los valores actuales de las barras desde st.session_state
    raw_scores = {}
    for crit in VALORES_EXCEL_DEFAULT.keys():
      session_key = f"slider_{crit}"
      raw_scores[crit] = st.slider(
          f"{crit}", 0.0, 100.0, float(st.session_state[session_key]), 1.0, key=session_key
      )

    # Cálculo automático de los pesos normalizados (verdadero peso ponderado AHP que suma 100%)
    suma_total = sum(raw_scores.values())
    if suma_total > 0:
      pesos_normalizados = {k: v / suma_total for k, v in raw_scores.items()}
    else:
      pesos_normalizados = {
          k: 1.0 / len(VALORES_EXCEL_DEFAULT) for k in raw_scores.keys()
      }

    # Guardar en st.session_state para que la app lo use en las evaluaciones
    st.session_state.pesos_ahp = pesos_normalizados

    st.markdown("---")
    st.markdown("### 📊 Gráfico Circular: Verdadero Peso Ponderado (Suma 100%)")
    st.markdown(
        "El siguiente diagrama refleja en tiempo real la distribución"
        " porcentual calculada a partir de sus ajustes con colores"
        " altamente distinguibles:"
    )

    # Generar gráfico circular (Dona) con Plotly utilizando una paleta variada y corporativa (Rojo, Azul, Verde, Morado, Naranja, Cian, Rosa)
    df_chart = pd.DataFrame({
        "Criterio": list(pesos_normalizados.keys()),
        "Porcentaje Real (%)": [v * 100 for v in pesos_normalizados.values()],
    })

    paleta_colores = [
        "#E61C24",  # Rojo Coca-Cola
        "#0072B2",  # Azul corporativo
        "#009E73",  # Verde esmeralda
        "#CC79A7",  # Morado / Magenta
        "#D55E00",  # Naranja intenso
        "#56B4E9",  # Azul cian claro
        "#F0E442",  # Amarillo brillante
    ]

    fig = px.pie(
        df_chart,
        names="Criterio",
        values="Porcentaje Real (%)",
        hole=0.4,
        color_discrete_sequence=paleta_colores,
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.7,
            xanchor="center",
            x=0.5,
        ),
    )
    st.plotly_chart(fig, use_container_width=True)

  # ------------------------------------------
  # REGISTRO DE PROYECTOS
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

        # Área / Ubicación con los 20 lugares oficiales de la planta
        area_sol = st.selectbox(
            "Área / Ubicación (Planta)", options=LUGARES_PLANTA
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
          "Califique el impacto de la iniciativa en cada criterio corporativo"
          " (se aplicarán automáticamente los pesos vigentes configurados en"
          " la sección AHP):"
      )

      # Asegurar que existan los pesos AHP en session_state
      if "pesos_ahp" not in st.session_state:
        suma_def = sum(VALORES_EXCEL_DEFAULT.values())
        st.session_state.pesos_ahp = {
            k: v / suma_def for k, v in VALORES_EXCEL_DEFAULT.items()
        }

      criterios_keys = list(st.session_state.pesos_ahp.keys())

      c1_val = st.slider(f"1. {criterios_keys[0]}", 0, 10, 5, 1)
      c2_val = st.slider(f"2. {criterios_keys[1]}", 0, 10, 5, 1)
      c3_val = st.slider(f"3. {criterios_keys[2]}", 0, 10, 5, 1)
      c4_val = st.slider(f"4. {criterios_keys[3]}", 0, 10, 5, 1)
      c5_val = st.slider(f"5. {criterios_keys[4]}", 0, 10, 5, 1)
      c6_val = st.slider(f"6. {criterios_keys[5]}", 0, 10, 5, 1)
      c7_val = st.slider(f"7. {criterios_keys[6]}", 0, 10, 5, 1)

      pesos_lista = list(st.session_state.pesos_ahp.values())
      ahp_score_calculado = (
          (c1_val * pesos_lista[0])
          + (c2_val * pesos_lista[1])
          + (c3_val * pesos_lista[2])
          + (c4_val * pesos_lista[3])
          + (c5_val * pesos_lista[4])
          + (c6_val * pesos_lista[5])
          + (c7_val * pesos_lista[6])
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
