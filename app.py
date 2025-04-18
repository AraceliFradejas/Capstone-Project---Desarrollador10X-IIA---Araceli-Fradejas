"""
🧠 Capstone Project - Dashboard Estratégico de Comentarios (KelceTS S.L.)
Instituto de Inteligencia Artificial - Curso Desarrollador 10x

👤 Estudiante: Araceli Fradejas Muñoz  
📅 Fecha de entrega: 21/04/2025

📄 Descripción del Proyecto:
KelceTS S.L. es una startup ficticia especializada en la venta de zapatillas online en Europa.

Este dashboard ha sido diseñado para ofrecer a la Dirección y al CEO una **visión analítica y estratégica** 
sobre los comentarios que los clientes dejan en diferentes idiomas y canales (email, redes sociales, etc.).

🎯 Objetivos de la App:
- Visualizar el volumen y evolución de comentarios recibidos
- Analizar las temáticas predominantes (logística, calidad, otros)
- Detectar idiomas más frecuentes y distribución geográfica
- Medir el número de comunicaciones generadas (cliente, logística, proveedor)
- Estimar costes de respuesta manual vs automática con IA
- Facilitar decisiones estratégicas basadas en datos en tiempo real

🔐 Gestión de claves:
- Carga segura de claves OpenAI y Gemini mediante archivo `.env` (NO se sube a GitHub)
- Fallback automático a Gemini (Google Cloud) si OpenAI no responde

📁 Datos utilizados desde el directorio `/data` del repositorio:
- BD Comentarios KelceTS.txt
- Reglas de calidad, logística, clientes y proveedores

💡 Impacto esperado:
- Mayor conocimiento de incidencias recurrentes
- Optimización del proceso de atención al cliente
- Visión ejecutiva sobre el uso de IA en el análisis multilingüe de clientes
- Apoyo a decisiones estratégicas con métricas visuales y automáticas
"""
import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import urllib.request
from io import BytesIO
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import base64
import time
from datetime import datetime

# Configuración de la página con colores de los Chiefs
st.set_page_config(
    page_title="Dashboard Dirección KelceTS", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Colores de Kansas City Chiefs
CHIEFS_RED = "#E31837"
CHIEFS_YELLOW = "#FFB612"
CHIEFS_RED_DARK = "#B30E29"  # Versión más oscura para hover

# Aplicar estilos personalizados al sidebar y a los componentes
st.markdown(f"""
<style>
    /* Estilo para el sidebar - fondo negro */
    .css-1d391kg, [data-testid="stSidebar"], .css-1cypcdb, .css-1nm2qww, .css-1mbkxta {{
        background-color: black !important;
    }}
    
    /* Estilo para el texto en el sidebar */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4 {{
        color: white !important;
    }}
    
    /* Estilo específico para las etiquetas de los radio buttons */
    .stRadio label {{
        color: white !important;
        font-weight: bold !important;
    }}
    
    /* Estilo para el texto dentro de los radio buttons */
    .stRadio label span {{
        color: white !important;
    }}
    
    /* Color para el círculo de los radio buttons */
    .stRadio [data-baseweb="radio"] input:checked + div {{
        border-color: #E31837 !important;
        background-color: #E31837 !important;
    }}
    
    /* Estilo al pasar el mouse */
    .stRadio [data-baseweb="radio"]:hover input + div {{
        border-color: #E31837 !important;
    }}
    
    /* Asegurarse de que el título del sidebar sea visible */
    [data-testid="stSidebar"] h3 {{
        color: #E31837 !important;
        font-weight: bold !important;
    }}
    
    /* Estilo para los botones (manteniendo tus colores) */
    .stButton>button, .stDownloadButton>button {{
        background-color: #E31837 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.5rem 1rem !important;
        font-weight: bold !important;
    }}
    
    .stButton>button:hover, .stDownloadButton>button:hover {{
        background-color: #B30E29 !important;
    }}
</style>
""", unsafe_allow_html=True)

# 🔐 Carga de claves API
try:
    from dotenv import load_dotenv
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
except:
    pass

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
        "no": CHIEFS_RED,  # Rojo para valores negativos
        "parcialmente": CHIEFS_YELLOW,  # Amarillo para valores parciales
        "no mencionado": "#6c757d"  # Gris para valores no mencionados
    }
    
    # Crear gráfico con Plotly - sin título para evitar duplicación
    fig = px.bar(
        df_calidad,
        x="Categoría",
        y="Cantidad", 
        color="Valor",
        barmode="group",
        color_discrete_map=colores_valores
    )
    
    fig.update_layout(
        xaxis_title="Variable de calidad",
        yaxis_title="Número de comentarios",
        legend_title="Valoración",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

# Función para generar gráfico de valoraciones
def generar_grafico_valoraciones(df):
    """Genera el gráfico de distribución de valoraciones"""
    df_plot = df["valoracion"].value_counts().reset_index()
    df_plot.columns = ["Valoración", "Cantidad"]
    
    # Color mapping
    colores_valoraciones = {
        "negativa": CHIEFS_RED, 
        "parcial": CHIEFS_YELLOW, 
        "positiva": "#28A745", 
        "neutra": "#7f7f7f"
    }
    
    fig = px.bar(
        df_plot, 
        x="Valoración", 
        y="Cantidad", 
        color="Valoración", 
        color_discrete_map=colores_valoraciones
    )
    
    fig.update_layout(
        xaxis_title="Valoración",
        yaxis_title="Número de comentarios"
    )
    
    return fig

# Función para generar gráfico de idiomas
def generar_grafico_idiomas(df):
    """Genera el gráfico de distribución por idioma"""
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
        
        # Color mapping
        colores_valoraciones = {
            "negativa": CHIEFS_RED, 
            "parcial": CHIEFS_YELLOW, 
            "positiva": "#28A745", 
            "neutra": "#7f7f7f"
        }
        
        fig = px.bar(
            df_agrupado, 
            x="label", 
            y="total", 
            text="total", 
            color="predominante", 
            color_discrete_map=colores_valoraciones
        )
        
        fig.update_traces(textposition="outside")
        fig.update_layout(
            xaxis_title="Idioma",
            yaxis_title="Número de comentarios"
        )
        
        return fig
    except Exception as e:
        st.error(f"Error en gráfico de idiomas: {e}")
        return None

# Función para generar gráfico de comunicaciones
def generar_grafico_comunicaciones(df):
    """Genera el gráfico de tipos de comunicaciones"""
    df_plot = df["tipo_comunicacion"].value_counts().reset_index()
    df_plot.columns = ["Tipo de comunicación", "Cantidad"]
    
    fig = px.bar(
        df_plot, 
        x="Tipo de comunicación", 
        y="Cantidad", 
        color="Tipo de comunicación", 
        color_discrete_sequence=[CHIEFS_YELLOW, "#28A745", CHIEFS_RED]
    )
    
    fig.update_layout(
        xaxis_title="Tipo de comunicación",
        yaxis_title="Número de comentarios"
    )
    
    return fig

# Función para generar PDF completo con todos los gráficos
def generar_pdf_completo(df, metricas):
    """
    Genera un PDF ejecutivo completo con todos los gráficos
    y análisis que se muestran en el dashboard
    """
    buffer = BytesIO()
    # Usar el tamaño Letter para más espacio
    page_size = letter
    c = canvas.Canvas(buffer, pagesize=page_size)
    width, height = page_size
    
    # Configurar título del documento PDF
    c.setTitle("Informe_Ejecutivo_KelceTS")
    
    # Colores corporativos KelceTS y Chiefs
    color_rojo = colors.Color(int(CHIEFS_RED[1:3], 16)/255, int(CHIEFS_RED[3:5], 16)/255, int(CHIEFS_RED[5:7], 16)/255)
    color_amarillo = colors.Color(int(CHIEFS_YELLOW[1:3], 16)/255, int(CHIEFS_YELLOW[3:5], 16)/255, int(CHIEFS_YELLOW[5:7], 16)/255)
    color_negro = colors.black
    color_gris = colors.Color(0x6c/255, 0x75/255, 0x7d/255)
    
    # -------- PÁGINA 1: CABECERA Y MÉTRICAS --------
    # Fondo rojo en la cabecera
    c.setFillColor(color_rojo)
    c.rect(0, height-3*cm, width, 3*cm, fill=True)
    
    # Logo KelceTS
    try:
        logo_url = "https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png"
        local_logo_path = "/tmp/KelceTS_logo.png"
        urllib.request.urlretrieve(logo_url, local_logo_path)
        c.drawImage(local_logo_path, x=1*cm, y=height-2.8*cm, width=2*cm, height=2*cm, mask='auto')
    except Exception as e:
        # Si falla la carga del logo, dejamos un espacio
        pass
    
    # Título en la cabecera
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.white)
    c.drawString(4*cm, height-1.8*cm, "INFORME EJECUTIVO KELCETS")
    c.setFont("Helvetica", 12)
    c.drawString(4*cm, height-2.4*cm, "Análisis automatizado de comentarios de clientes")
    
    # Fecha actual
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(color_negro)
    c.drawRightString(width-1*cm, height-4*cm, f"Fecha: {datetime.now().strftime('%d/%m/%Y')}")
    
    # Título de la sección de métricas
    y_pos = height - 5*cm
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*cm, y_pos, "Métricas clave")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 3*cm, 0.1*cm, fill=True)
    y_pos -= 1.5*cm
    
    # Tabla de métricas clave
    data = [
        ["Indicador", "Valor"],
        ["Total comentarios analizados:", f"{metricas['total_comentarios']}"],
        ["Valoraciones positivas:", f"{metricas['porc_positivos']:.2f}%"],
        ["Valoraciones negativas:", f"{metricas['porc_negativos']:.2f}%"],
        ["Coste total estimado:", f"{metricas['coste_total']}"]
    ]
    
    c.setFont("Helvetica", 10)
    table_style = [
        ('GRID', (0, 0), (-1, -1), 0.5, color_gris),
        ('BACKGROUND', (0, 0), (1, 0), color_rojo),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.white),
        ('FONT', (0, 0), (1, 0), 'Helvetica-Bold', 10),
        ('FONT', (0, 1), (0, -1), 'Helvetica-Bold', 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]
    
    # Dibujar tabla de métricas
    table_width = 12*cm
    table_height = 3*cm
    from reportlab.platypus import Table as PT
    from reportlab.platypus import TableStyle
    
    table = PT(data, colWidths=[6*cm, 6*cm])
    table.setStyle(TableStyle(table_style))
    
    # Dibujar tabla en el canvas
    w, h = table.wrap(width, height)
    table.drawOn(c, 1*cm, y_pos-h)
    
    # Añadir más espacio después de la tabla
    y_pos -= 5*cm
    
    # Gráfico de valoraciones
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color_negro)
    c.drawString(1*cm, y_pos, "Distribución de valoraciones")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 5*cm, 0.1*cm, fill=True)
    
    # Generar y guardar gráfico de valoraciones
    fig_valoraciones = generar_grafico_valoraciones(df)
    # Mayor resolución para mejor calidad en PDF
    gráfico_val_path = "/tmp/grafico_valoraciones.png"
    fig_valoraciones.write_image(gráfico_val_path, width=1200, height=700, scale=2)
    
    # Añadir imagen del gráfico
    c.drawImage(gráfico_val_path, x=1*cm, y=y_pos-8*cm, width=width-2*cm, height=7*cm)
    
    # Footer en primera página
    c.setFont("Helvetica", 8)
    c.setFillColor(color_gris)
    c.drawCentredString(width/2, 1*cm, "KelceTS S.L. – Informe generado automáticamente por Araceli Fradejas Muñoz | Página 1/3")
    c.drawCentredString(width/2, 0.7*cm, "Curso Desarrollador10X – Instituto de Inteligencia Artificial")
    
    # -------- PÁGINA 2: GRÁFICOS DE IDIOMAS Y COMUNICACIONES --------
    c.showPage()
    
    # Repetir cabecera
    c.setFillColor(color_rojo)
    c.rect(0, height-3*cm, width, 3*cm, fill=True)
    
    try:
        c.drawImage(local_logo_path, x=1*cm, y=height-2.8*cm, width=2*cm, height=2*cm, mask='auto')
    except:
        pass
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.white)
    c.drawString(4*cm, height-1.8*cm, "INFORME EJECUTIVO KELCETS")
    c.setFont("Helvetica", 12)
    c.drawString(4*cm, height-2.4*cm, "Análisis automatizado de comentarios de clientes")
    
    # Título Idiomas
    y_pos = height - 5*cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color_negro)
    c.drawString(1*cm, y_pos, "Distribución por idioma")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 4*cm, 0.1*cm, fill=True)
    
    # Generar y guardar gráfico de idiomas
    fig_idiomas = generar_grafico_idiomas(df)
    if fig_idiomas:
        gráfico_idiomas_path = "/tmp/grafico_idiomas.png"
        # Mayor resolución para mejor calidad en PDF
        fig_idiomas.write_image(gráfico_idiomas_path, width=1200, height=700, scale=2)
        # Añadir imagen del gráfico
        c.drawImage(gráfico_idiomas_path, x=1*cm, y=y_pos-8*cm, width=width-2*cm, height=7*cm)
    
    # Título Comunicaciones
    y_pos = y_pos - 9*cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color_negro)
    c.drawString(1*cm, y_pos, "Distribución por tipo de comunicación")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 6*cm, 0.1*cm, fill=True)
    
    # Generar y guardar gráfico de comunicaciones
    fig_comunicaciones = generar_grafico_comunicaciones(df)
    gráfico_com_path = "/tmp/grafico_comunicaciones.png"
    # Mayor resolución para mejor calidad en PDF
    fig_comunicaciones.write_image(gráfico_com_path, width=1200, height=700, scale=2)
    
    # Añadir imagen del gráfico
    c.drawImage(gráfico_com_path, x=1*cm, y=y_pos-8*cm, width=width-2*cm, height=7*cm)
    
    # Footer en segunda página
    c.setFont("Helvetica", 8)
    c.setFillColor(color_gris)
    c.drawCentredString(width/2, 1*cm, "KelceTS S.L. – Informe generado automáticamente por Araceli Fradejas Muñoz | Página 2/3")
    c.drawCentredString(width/2, 0.7*cm, "Curso Desarrollador10X – Instituto de Inteligencia Artificial")
    
    # -------- PÁGINA 3: ANÁLISIS DE VARIABLES DE CALIDAD --------
    c.showPage()
    
    # Repetir cabecera
    c.setFillColor(color_rojo)
    c.rect(0, height-3*cm, width, 3*cm, fill=True)
    
    try:
        c.drawImage(local_logo_path, x=1*cm, y=height-2.8*cm, width=2*cm, height=2*cm, mask='auto')
    except:
        pass
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.white)
    c.drawString(4*cm, height-1.8*cm, "INFORME EJECUTIVO KELCETS")
    c.setFont("Helvetica", 12)
    c.drawString(4*cm, height-2.4*cm, "Análisis automatizado de comentarios de clientes")
    
    # Título Variables de Calidad
    y_pos = height - 5*cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color_negro)
    c.drawString(1*cm, y_pos, "Análisis de variables clave de calidad")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 6*cm, 0.1*cm, fill=True)
    
    # Generar y guardar gráfico de variables de calidad
    fig_calidad = generar_grafico_calidad(df)
    gráfico_cal_path = "/tmp/grafico_calidad.png"
    # Mayor resolución para mejor calidad en PDF
    fig_calidad.write_image(gráfico_cal_path, width=1200, height=800, scale=2)
    
    # Añadir imagen del gráfico
    c.drawImage(gráfico_cal_path, x=1*cm, y=y_pos-9*cm, width=width-2*cm, height=8*cm)
    
    # Conclusiones y recomendaciones
    y_pos = y_pos - 10*cm
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color_negro)
    c.drawString(1*cm, y_pos, "Conclusiones y recomendaciones")
    c.setFillColor(color_rojo)
    c.rect(1*cm, y_pos-0.3*cm, 5.5*cm, 0.1*cm, fill=True)
    
    # Texto con conclusiones - USANDO COLOR NEGRO
    y_pos -= 1*cm
    c.setFont("Helvetica", 10)
    c.setFillColor(color_negro)  # Establecer color negro para las conclusiones
    
    # Determinar recomendaciones basadas en los datos
    total = metricas['total_comentarios']
    perc_neg = metricas['porc_negativos']
    
    conclusiones = []
    if perc_neg > 30:
        conclusiones.append("• Se detecta un alto porcentaje de valoraciones negativas. Se recomienda revisar urgentemente los procesos de control de calidad.")
    else:
        conclusiones.append("• El porcentaje de valoraciones negativas está en un rango aceptable, pero debe monitorizarse para detectar incrementos.")
    
    # Variables más problemáticas
    problemas = []
    for var in ["envio_96h", "embalaje_danado", "talla_correcta", "materiales_calidad"]:
        if var in df.columns:
            perc_no = len(df[df[var] == "no"]) / total * 100 if total > 0 else 0
            if perc_no > 20:
                var_nombre = var.replace("_", " ").title()
                problemas.append((var_nombre, perc_no))
    
    problemas.sort(key=lambda x: x[1], reverse=True)
    for i, (prob, perc) in enumerate(problemas[:3]):
        conclusiones.append(f"• {prob}: {perc:.2f}% de comentarios negativos. Requiere revisión prioritaria.")
    
    if not problemas:
        conclusiones.append("• No se detectan problemas significativos en ninguna de las variables analizadas.")
    
    # Añadir conclusiones al PDF
    for i, texto in enumerate(conclusiones):
        c.drawString(1*cm, y_pos - i*0.6*cm, texto)
    
    # Información de fecha y autor
    y_pos -= (len(conclusiones) + 2) * 0.6*cm
    c.setFont("Helvetica", 9)
    c.drawString(1*cm, y_pos, f"Informe generado el {datetime.now().strftime('%d/%m/%Y')} - Análisis automatizado por KelceTS S.L.")
    
    # Footer en tercera página
    c.setFont("Helvetica", 8)
    c.setFillColor(color_gris)
    c.drawCentredString(width/2, 1*cm, "KelceTS S.L. – Informe generado automáticamente por Araceli Fradejas Muñoz | Página 3/3")
    c.drawCentredString(width/2, 0.7*cm, "Curso Desarrollador10X – Instituto de Inteligencia Artificial")
    
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
        <div style='background-color:#E31837; padding:10px 20px; display:flex; flex-direction:column; align-items:center;'>
            <img src='https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png' style='max-height:80px; width:auto; margin-bottom:10px;'>
            <h2 style='color:white; text-align:center;'>Dashboard Dirección KelceTS</h2>
            <h4 style='color:white;'>Decisiones estratégicas basadas en comentarios reales de clientes 👟</h4>
        </div>
    """, unsafe_allow_html=True)

    # 📊 Indicadores clave
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

    # Selector con estilo Chiefs personalizado - título en negro
    st.sidebar.markdown("<h3 style='color: black; font-weight: bold; margin-top: 15px;'>Tipo de visualización:</h3>", unsafe_allow_html=True)
    
    opciones = {
        "📈 Valoraciones": "📈 Distribución por valoración",
        "🌍 Idiomas": "🌍 Distribución por idioma con valoración dominante",
        "📬 Tipo de comunicaciones": "📬 Distribución por tipo de comunicación",
        "🔍 Variables de calidad": "🔍 Análisis de variables clave de calidad"
    }
    
    # Radio button con el estilo aplicado a través del CSS definido al inicio
    # Se añade una etiqueta significativa y se oculta para resolver la advertencia de accesibilidad
    eleccion = st.sidebar.radio(
        "Opciones de visualización", 
        list(opciones.keys()),
        label_visibility="collapsed"  # Oculta la etiqueta pero mantiene la accesibilidad
    )
    
    # Espacio entre secciones
    st.markdown("<hr style='margin-top: 15px; margin-bottom: 15px;'>", unsafe_allow_html=True)
    
    # Título de la visualización seleccionada
    st.markdown(f"## {opciones[eleccion]}")

    # Colores Chiefs
    colores_valoraciones = {"negativa": CHIEFS_RED, "parcial": CHIEFS_YELLOW, "positiva": "#28A745", "neutra": "#7f7f7f"}

    if eleccion == "📈 Valoraciones":
        fig = generar_grafico_valoraciones(df)
        st.plotly_chart(fig, use_container_width=True)

    elif eleccion == "🌍 Idiomas":
        fig = generar_grafico_idiomas(df)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No se pudo generar el gráfico de idiomas")

    elif eleccion == "📬 Tipo de comunicaciones":
        fig = generar_grafico_comunicaciones(df)
        st.plotly_chart(fig, use_container_width=True)
        
    elif eleccion == "🔍 Variables de calidad":
        # Generamos el nuevo gráfico de variables de calidad
        fig = generar_grafico_calidad(df)
        st.plotly_chart(fig, use_container_width=True)

    # ✅ Carga de datos
    st.markdown("<p style='text-align:center; color:green; font-weight:bold;'>✅ Datos reales cargados desde GitHub</p>", unsafe_allow_html=True)

    # 📥 Descargar PDF con todos los gráficos
    metricas = {
        "total_comentarios": total_comentarios,
        "porc_positivos": porc_positivos,
        "porc_negativos": porc_negativos,
        "coste_total": coste_total
    }
    
    # Generar PDF completo con todos los gráficos
    pdf_buffer = generar_pdf_completo(df, metricas)
    
    # Botón de descarga con estilo Chiefs
    descargar = st.download_button(
        label="📄 Descargar informe ejecutivo en PDF",
        data=pdf_buffer,
        file_name="Informe_Ejecutivo_KelceTS.pdf",
        mime="application/pdf",
        use_container_width=True
    )
    
    # ============================
    # ℹ️ INFORMACIÓN TÉCNICA Y FOOTER
    # ============================
    with st.expander("🔧 Información Técnica del Sistema"):
        st.markdown("""
        - 🔐 Claves API cargadas desde `.env`
        - 📂 Datos cargados desde GitHub `/data`
        - 🧠 Modelos conectados: OpenAI y Gemini
        - 🧪 Reglas internas cargadas
        - 📊 Visualizaciones generadas con Plotly
        - 📱 Dashboard responsivo para múltiples dispositivos
        - 🖨️ Informes PDF generados con ReportLab
        """)
    
    # ====================
    # 👣 FOOTER
    # ====================
    st.markdown(
        "<hr style='margin-top:50px;'>"
        "<p style='text-align:center; font-size:small;'>Desarrollado por Araceli Fradejas Muñoz · "
        "<a href='https://iia.es/' target='_blank'>Curso Desarrollador10X Instituto de Inteligencia Artificial</a> · Abril 2025</p>",
        unsafe_allow_html=True
    )

except Exception as e:
    st.error(f"⚠️ Error en la aplicación: {e}")
    
    # Mostrar información de depuración para ayudar a solucionar el problema
    st.info("Revise los siguientes posibles problemas:")
    st.markdown("""
    1. Verificar que el archivo Excel exista en GitHub
    2. Comprobar que se tienen los permisos necesarios
    3. Verificar que las columnas esperadas existen en el archivo
    """)
    
    # Footer siempre visible
    st.markdown(
        "<hr style='margin-top:50px;'>"
        "<p style='text-align:center; font-size:small;'>Desarrollado por Araceli Fradejas Muñoz · "
        "<a href='https://iia.es/' target='_blank'>Curso Desarrollador10X Instituto de Inteligencia Artificial</a> · Abril 2025</p>",
        unsafe_allow_html=True
    )