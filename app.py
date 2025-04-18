import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
import urllib.request
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors

st.set_page_config(page_title="Dashboard Dirección KelceTS", layout="wide")

# Función para crear un DataFrame de ejemplo
def crear_df_ejemplo():
    """Crea un DataFrame de ejemplo con la estructura necesaria"""
    data = {
        'comentario_original': ['Comentario positivo ejemplo', 'Comentario negativo ejemplo', 'Otro comentario'] * 10,
        'idioma': ['español', 'alemán', 'francés'] * 10,
        'valoracion': ['positiva', 'negativa', 'neutra'] * 10,
        'envio_96h': ['sí', 'no', 'no mencionado'] * 10,
        'embalaje_danado': ['no', 'sí', 'no mencionado'] * 10,
        'talla_correcta': ['sí', 'no', 'no mencionado'] * 10,
        'materiales_calidad': ['sí', 'no', 'parcialmente'] * 10,
        'cumple_expectativas': ['sí', 'no', 'parcialmente'] * 10
    }
    return pd.DataFrame(data)

# Carga del Excel de GitHub
@st.cache_data
def cargar_excel():
    try:
        # URL correcta al archivo raw en GitHub
        url = "https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/Informe_Final_KelceTS.xlsx"
        
        # Descargar el archivo
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            urllib.request.urlretrieve(url, tmp.name)
            # Cargar el Excel desde el archivo temporal
            return pd.read_excel(tmp.name)
    except Exception as e:
        st.error(f"⚠️ Error al cargar el Excel desde GitHub: {e}")
        st.info("Intentando cargar archivo local...")
        
        # Intento alternativo con archivo local
        try:
            if os.path.exists("Informe_Final_KelceTS.xlsx"):
                return pd.read_excel("Informe_Final_KelceTS.xlsx")
            else:
                raise FileNotFoundError("No se encontró el archivo local")
        except Exception as e2:
            st.error(f"⚠️ También falló la carga local: {e2}")
            st.warning("Se usarán datos de ejemplo para mostrar la funcionalidad.")
            return crear_df_ejemplo()

# Función para generar gráfico de variables de calidad
def generar_grafico_calidad(df):
    """Genera el gráfico de variables clave de calidad"""
    
    # Variables clave para analizar
    variables_calidad = ["envio_96h", "embalaje_danado", "talla_correcta", "materiales_calidad", "cumple_expectativas"]
    
    # Preparar DataFrame para visualización
    datos_calidad = []
    for var in variables_calidad:
        if var in df.columns:
            counts = df[var].value_counts().to_dict()
            for valor, cantidad in counts.items():
                datos_calidad.append({"Categoría": var, "Valor": valor, "Cantidad": cantidad})
    
    df_calidad = pd.DataFrame(datos_calidad)
    
    # Color mapping para consistencia visual
    colores_valores = {
        "sí": "#28A745",  # Verde para valores positivos
        "no": "#E31837",  # Rojo para valores negativos
        "parcialmente": "#FFB612",  # Amarillo para valores parciales
        "no mencionado": "#6c757d"  # Gris para valores no mencionados
    }
    
    # Crear gráfico con Plotly
    fig = px.bar(
        df_calidad,
        x="Categoría",
        y="Cantidad", 
        color="Valor",
        barmode="group",
        title="📊 Análisis de variables clave de calidad",
        color_discrete_map=colores_valores
    )
    
    fig.update_layout(
        xaxis_title="Variable de calidad",
        yaxis_title="Número de comentarios",
        legend_title="Valoración",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

# Función para generar PDF mejorado
def generar_pdf_mejorado(df, metricas):
    """Genera un PDF ejecutivo mejorado con cabecera personalizada"""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    # Colores corporativos KelceTS
    color_rojo = colors.Color(0xCE/255, 0x11/255, 0x26/255)
    color_negro = colors.black
    
    # -------- CABECERA PERSONALIZADA --------
    # Fondo rojo en la cabecera
    c.setFillColor(color_rojo)
    c.rect(0, height-4*cm, width, 4*cm, fill=True)
    
    # Logo KelceTS
    try:
        logo_url = "https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png"
        local_logo_path = "/tmp/KelceTS_logo.png"
        urllib.request.urlretrieve(logo_url, local_logo_path)
        c.drawImage(local_logo_path, x=2*cm, y=height-3.5*cm, width=2.5*cm, height=2.5*cm, mask='auto')
    except Exception as e:
        # Si falla la carga del logo, dejamos un espacio
        st.error(f"Error al cargar logo: {e}")
    
    # Título en la cabecera
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.white)
    c.drawString(5*cm, height-2*cm, "INFORME EJECUTIVO KELCETS")
    
    # -------- CONTENIDO --------
    # Fecha actual
    import datetime
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(color_negro)
    c.drawRightString(width-1*cm, height-5*cm, f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y')}")
    
    # Métricas clave
    y_pos = height - 6*cm
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2*cm, y_pos, "Métricas clave")
    y_pos -= 1*cm
    
    # Contenido de métricas
    c.setFont("Helvetica", 12)
    c.drawString(2*cm, y_pos, f"Comentarios analizados: {metricas['total_comentarios']}")
    y_pos -= 0.8*cm
    c.drawString(2*cm, y_pos, f"Porcentaje negativos: {metricas['porc_negativos']:.2f}%")
    y_pos -= 0.8*cm
    c.drawString(2*cm, y_pos, f"Coste total estimado: {metricas['coste_total']}")
    
    # Footer institucional
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(A4[0] / 2, 1.5*cm, "KelceTS S.L. – Proyecto académico ficticio | Curso Desarrollador10X – Instituto de Inteligencia Artificial")
    
    c.save()
    buffer.seek(0)
    return buffer

# CARGA DE DATOS Y PROCESAMIENTO
try:
    # Cargar datos
    df = cargar_excel()
    
    # Procesamiento de datos
    if "tipo_comunicacion" not in df.columns:
        df["tipo_comunicacion"] = df["valoracion"].apply(lambda v: (
            "📦 Notificación interna (logística/calidad)" if v == "negativa" else
            "✅ Respuesta al cliente" if v == "positiva" else
            "📧 Comunicación pendiente de revisión"
        ))

    coste_unitario = {
        "📦 Notificación interna (logística/calidad)": 5,
        "✅ Respuesta al cliente": 3,
        "📧 Comunicación pendiente de revisión": 4
    }
    df["coste_base"] = df["tipo_comunicacion"].map(coste_unitario)

    penalizaciones = []
    medidas = []
    for _, row in df.iterrows():
        penal = 0
        medida = []
        if str(row.get("materiales_calidad", "")).strip().lower() == "no":
            penal += 40
            medida.append("25% descuento + recogida gratuita")
        if str(row.get("envio_96h", "")).strip().lower() == "no":
            penal += 50
            medida.append("5% descuento por retraso de envío")
        if str(row.get("talla_correcta", "")).strip().lower() == "no":
            penal += 10
            medida.append("Cambio de talla sin coste en 72h")
        if str(row.get("embalaje_danado", "")).strip().lower() == "sí":
            penal += 5
            medida.append("5% descuento por embalaje dañado")
        penalizaciones.append(penal)
        medidas.append(" + ".join(medida) if medida else "Sin medida compensatoria")

    df["coste_penalizacion"] = penalizaciones
    df["medida_aplicada"] = medidas
    df["coste_total"] = df["coste_base"] + df["coste_penalizacion"]

    # 🎯 ENCABEZADO CEO CON LOGO Y LEMA
    st.markdown("""
        <div style='background-color:#CE1126; padding:10px 20px; display:flex; flex-direction:column; align-items:center;'>
            <img src='https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png' style='max-height:80px; width:auto; margin-bottom:10px;'>
            <h2 style='color:white; text-align:center;'>Dashboard Dirección KelceTS</h2>
            <h4 style='color:white;'>Decisiones estratégicas basadas en comentarios reales de clientes 👟</h4>
        </div>
    """, unsafe_allow_html=True)

    # 📊 Indicadores clave
    st.title("📊 Dashboard Dirección KelceTS")
    col1, col2, col3 = st.columns(3)
    
    # Cálculo de métricas
    total_comentarios = len(df)
    porc_positivos = len(df[df['valoracion'] == 'positiva']) / total_comentarios * 100 if total_comentarios > 0 else 0
    porc_negativos = len(df[df['valoracion'] == 'negativa']) / total_comentarios * 100 if total_comentarios > 0 else 0
    coste_total = f"{df['coste_total'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # Mostrar métricas
    col1.metric("Comentarios analizados", total_comentarios)
    col2.metric("% Negativos", f"{porc_negativos:.2f}%")
    col3.metric("Coste estimado", f"{coste_total} €")

    # Selector
    opciones = {
        "📈 Valoraciones": "📈 Distribución por valoración",
        "🌍 Idiomas": "🌍 Distribución por idioma con valoración dominante",
        "📬 Tipo de comunicaciones": "📬 Distribución por tipo de comunicación",
        "🔍 Variables de calidad": "🔍 Análisis de variables clave de calidad"
    }
    eleccion = st.sidebar.radio("Tipo de visualización:", list(opciones.keys()))
    st.markdown(f"## {opciones[eleccion]}")

    # Colores Chiefs
    colores_valoraciones = {"negativa": "#E31837", "parcial": "#FFB612", "positiva": "#28A745", "neutra": "#7f7f7f"}

    if eleccion == "📈 Valoraciones":
        df_plot = df["valoracion"].value_counts().reset_index()
        df_plot.columns = ["Valoración", "Cantidad"]
        fig = px.bar(df_plot, x="Valoración", y="Cantidad", color="Valoración", color_discrete_map=colores_valoraciones)
        st.plotly_chart(fig, use_container_width=True)

    elif eleccion == "🌍 Idiomas":
        # Manejo seguro de errores en agrupación
        try:
            df_agrupado = df.groupby("idioma")["valoracion"].value_counts().unstack().fillna(0)
            for col in ["positiva", "negativa"]:
                if col not in df_agrupado.columns:
                    df_agrupado[col] = 0
            df_agrupado["total"] = df_agrupado.sum(axis=1)
            df_agrupado["predominante"] = df_agrupado[["positiva", "negativa"]].idxmax(axis=1)
            df_agrupado = df_agrupado.reset_index()
            
            # Banderas para idiomas
            flags = {
                "español": "🇪🇸", "alemán": "🇩🇪", "francés": "🇫🇷", "italiano": "🇮🇹", 
                "portugués": "🇵🇹", "neerlandés": "🇳🇱", "polaco": "🇵🇱", "finlandés": "🇫🇮",
                "sueco": "🇸🇪", "danés": "🇩🇰", "griego": "🇬🇷", "húngaro": "🇭🇺",
                "checo": "🇨🇿", "rumano": "🇷🇴"
            }
            
            df_agrupado["label"] = df_agrupado["idioma"].apply(lambda x: f"{flags.get(x, '')} {x}")
            fig = px.bar(df_agrupado, x="label", y="total", text="total", color="predominante", color_discrete_map=colores_valoraciones)
            fig.update_traces(textposition="outside")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error en gráfico de idiomas: {e}")
            st.write(df[["idioma", "valoracion"]].head())

    elif eleccion == "📬 Tipo de comunicaciones":
        df_plot = df["tipo_comunicacion"].value_counts().reset_index()
        df_plot.columns = ["Tipo de comunicación", "Cantidad"]
        fig = px.bar(df_plot, x="Tipo de comunicación", y="Cantidad", color="Tipo de comunicación", color_discrete_sequence=["#FFB612", "#28A745", "#E31837"])
        st.plotly_chart(fig, use_container_width=True)
        
    elif eleccion == "🔍 Variables de calidad":
        # Generamos el nuevo gráfico de variables de calidad
        fig_calidad = generar_grafico_calidad(df)
        st.plotly_chart(fig_calidad, use_container_width=True)

    # ✅ Carga de datos
    st.markdown("<p style='text-align:center; color:green; font-weight:bold;'>✅ Datos reales cargados desde GitHub</p>", unsafe_allow_html=True)

    # 📥 Descargar PDF
    metricas = {
        "total_comentarios": total_comentarios,
        "porc_positivos": porc_positivos,
        "porc_negativos": porc_negativos,
        "coste_total": coste_total
    }
    
    # Generar PDF mejorado
    pdf_buffer = generar_pdf_mejorado(df, metricas)
    
    # Botón de descarga (explícitamente mostrado)
    descargar = st.download_button(
        label="📄 Descargar informe ejecutivo en PDF",
        data=pdf_buffer,
        file_name="Informe_Ejecutivo_KelceTS.pdf",
        mime="application/pdf",
        use_container_width=True,
        type="primary"
    )
    
    if not descargar:
        st.info("👆 Haz clic en el botón para descargar el informe ejecutivo en PDF")

except Exception as e:
    st.error(f"⚠️ Error en la aplicación: {e}")
    st.info("Para resolver este problema, verifica:")
    st.markdown("""
    1. Que existe el archivo en GitHub
    2. Que tienes conexión a Internet
    3. Si el problema persiste, descarga el archivo manualmente
    """)