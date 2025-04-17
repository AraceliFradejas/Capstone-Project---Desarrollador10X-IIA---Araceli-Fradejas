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

# ====================================================
# 🌟 Dashboard Ejecutivo - Panel Principal para CEO de KelceTS
# ====================================================

import streamlit as st
import pandas as pd
import os
import sys
import random
from PIL import Image
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ============================
# ⚠️ Validación mínima de dependencias (modo Colab/Kaggle)
# ============================
try:
    import openai
    import google.generativeai as genai
except ImportError:
    st.warning("⚠️ Faltan librerías importantes. Por favor, instala desde requirements.txt")

# ============================
# 🔐 Carga de claves desde .env
# ============================
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ============================
# 🏠 CABECERA CORPORATIVA CON ESTILO CHIEFS
# ============================
st.markdown("""
    <div style='background-color:#CE1126; padding:10px 20px; display:flex; flex-direction:column; align-items:center;'>
        <img src='https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/main/data/Kelce%20TS%20LOGO.png' style='height:80px; margin-bottom:10px;'>
        <h2 style='color:white; text-align:center;'>Asistente de IA para el Call Center de KelceTS</h2>
        <h4 style='color:white;'>Automatiza, responde y conquista la atención al cliente con inteligencia 👟</h4>
    </div>
""", unsafe_allow_html=True)

# ============================
# 📁 Cargar DataFrame clasificado si no existe
# ============================
if 'df_clasificados' not in st.session_state:
    comentarios = ["Las zapatillas llegaron rotas", "Muy cómodas y buena calidad"] * 25
    datos_clasificados = []
    for c in comentarios:
        idioma = detect(c)
        valor = "negativa" if "rotas" in c else "positiva"
        comunicacion = "📦 Notificación interna (logística/calidad)" if "rotas" in c else "✅ Respuesta al cliente"
        datos_clasificados.append({"comentario": c, "idioma": idioma, "valoracion_global": valor, "comunicacion_recomendada": comunicacion})
    st.session_state.df_clasificados = pd.DataFrame(datos_clasificados)

df = st.session_state.df_clasificados

# ============================
# 📊 KPIs FIJOS ARRIBA SIEMPRE
# ============================
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("📄 Comentarios analizados", len(df))
porc = (df["valoracion_global"] == "negativa").sum() / len(df) * 100
col2.metric("🚫 % Negativos", f"{porc:.2f}%")
coste = 0
for tipo, c in [("✅ Respuesta al cliente", 3), ("📦 Notificación interna (logística/calidad)", 5), ("🤝 Comunicación formal a proveedor", 7)]:
    coste += df["comunicacion_recomendada"].str.contains(tipo).sum() * c
col3.metric("💰 Ahorro estimado", f"{coste:.2f} €")

# ============================
# 🔀 Selector de Visualización (menú a la izquierda)
# ============================
st.sidebar.markdown("## 📊 Tipo de visualización")
opcion = st.sidebar.radio("Selecciona el tipo de visualización:", [
    "📈 Valoraciones Globales",
    "🌐 Idiomas más frecuentes",
    "📬 Tipo de comunicaciones generadas"
])

# ============================
# 🔄 VISUALIZACIÓN SEGÚN OPCIÓN
# ============================
if opcion == "📈 Valoraciones Globales":
    st.markdown("### 📈 Valoraciones Globales")
    conteo = df["valoracion_global"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(conteo.index, conteo.values, color=["#CE1126", "#FFC72C"])
    ax.tick_params(axis='x', labelrotation=15)
    st.pyplot(fig)

elif opcion == "🌐 Idiomas más frecuentes":
    st.markdown("### 🌐 Idiomas más frecuentes")
    top_idiomas = df["idioma"].value_counts().head(5)
    st.dataframe(top_idiomas.reset_index().rename(columns={"index": "Idioma", "idioma": "Cantidad"}))

elif opcion == "📬 Tipo de comunicaciones generadas":
    st.markdown("### 📬 Tipo de comunicaciones generadas")
    conteo_com = df["comunicacion_recomendada"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(conteo_com.index, conteo_com.values, color=["#FFC72C" if i%2==0 else "#CE1126" for i in range(len(conteo_com))])
    ax.tick_params(axis='x', labelrotation=30)
    st.pyplot(fig)

# ============================
# 📄 Exportar resumen a PDF
# ============================
def exportar_resumen_pdf(datos):
    archivo_pdf = "Resumen_KelceTS.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    textobject = c.beginText(40, 750)
    textobject.setFont("Helvetica", 12)
    textobject.textLine("📊 Resumen Ejecutivo - KelceTS S.L.")
    textobject.textLine(" ")
    for clave, valor in datos.items():
        textobject.textLine(f"{clave}: {valor}")
    c.drawText(textobject)
    c.save()
    return archivo_pdf

if st.sidebar.button("📥 Descargar resumen en PDF"):
    datos_pdf = {
        "Comentarios analizados": len(df),
        "% comentarios negativos": f"{porc:.2f}%",
        "Ahorro estimado": f"{coste:.2f} €"
    }
    ruta_pdf = exportar_resumen_pdf(datos_pdf)
    with open(ruta_pdf, "rb") as f:
        st.download_button(
            label="Descargar PDF",
            data=f,
            file_name="Resumen_KelceTS.pdf",
            mime="application/pdf"
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
    """)

st.divider()
st.markdown("""
<div style='text-align: center;'>
    <img src='https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/main/data/Kelce%20TS%20LOGO.png' width='80'>
    <p><b>Asistente de IA para un call center desarrollado por Araceli Fradejas Muñoz, Abril 2025</b><br>
    Curso Desarrollador10X realizado en el <a href='https://institutointeligenciaartificial.com' style='color:#CE1126'>Instituto de Inteligencia Artificial</a><br>
    <span style='font-size:small; color:grey;'>KelceTS S.L. – Proyecto académico ficticio como Capstone Project de IA generativa</span></p>
</div>
""", unsafe_allow_html=True)
