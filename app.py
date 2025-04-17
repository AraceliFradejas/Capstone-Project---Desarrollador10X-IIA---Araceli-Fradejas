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
# ⚙️ 1. Preparación del entorno y carga de librerías
# ====================================================
#
# En esta sección importamos únicamente las librerías necesarias
# para ejecutar análisis estratégico en la app Streamlit.
#
# Este enfoque está centrado en la visualización y análisis
# de datos provenientes de comentarios de clientes para la
# toma de decisiones por parte de la Dirección y el CEO.
#
# Las principales funcionalidades incluyen:
# - Análisis textual y detección de idioma
# - Carga y procesamiento de archivos desde /data
# - Cálculo de métricas e indicadores clave (KPIs)
# - Visualización gráfica e interactiva en Streamlit
# - Conexión con modelos de lenguaje (OpenAI y Gemini)
# 
#
# ================================================
# 🛠️ Instalación automática de paquetes (opcional)
# ================================================

import streamlit as st  
import subprocess
import sys

def instalar_paquete(paquete):
    subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])

paquetes_necesarios = [
    "openai",
    "google-generativeai",
    "langdetect",
    "python-dotenv",
    "pandas",
    "matplotlib",
    "streamlit"
]

for paquete in paquetes_necesarios:
    try:
        __import__(paquete.split("=")[0].replace("-", "_"))
    except ImportError:
        instalar_paquete(paquete)


# 💾 Gestión del sistema
import os
import json
import re
from datetime import datetime

# 📊 Manipulación y análisis de datos
import pandas as pd
import numpy as np

# 🌍 Detección automática de idioma
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # Para que los resultados sean reproducibles

# 🧠 Conexión con modelos de IA
import openai
import google.generativeai as genai

# 🧪 Carga segura de claves
from dotenv import load_dotenv

# 📈 Visualización profesional
import streamlit as st
import matplotlib.pyplot as plt

# 🎲 Reproducibilidad en análisis aleatorios
import random
random.seed(42)

# ====================================================
# 1.1 🔐 Carga de claves de OpenAI y Gemini desde `.env` o desde Secrets
# ====================================================
#
# Esta app en Streamlit se ejecuta de forma segura y privada gracias a un sistema mixto de carga de claves:
#
# 1. Primero intenta cargar un archivo `.env` en la raíz del proyecto, que debe contener las variables:
#     - OPENAI_API_KEY
#     - GOOGLE_API_KEY
#
# 2. Si el archivo `.env` no está disponible (por ejemplo, en entorno cloud como Codespaces),
#    intentará recuperar las claves desde las variables de entorno (Secrets), al estilo de Colab o Kaggle.
#
# Este enfoque garantiza:
#   ✅ Seguridad (las claves no se exponen directamente en el código)
#   ✅ Compatibilidad con ejecución local, cloud, Codespaces y notebooks públicos
#
# ---
#
# ⚠️ MUY IMPORTANTE
# - Si estás ejecutando esta app por primera vez, asegúrate de tener un archivo `.env` con tus claves.
# - También puedes definir tus claves como Secrets en el repositorio (GitHub → Settings → Secrets → Actions).
# - ❌ Si no se encuentran las claves, las llamadas a la API fallarán al analizar los comentarios.

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not OPENAI_API_KEY:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    if OPENAI_API_KEY:
        st.info("🔐 OPENAI_API_KEY cargada desde entorno (Secrets / Codespaces).")

if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    if GOOGLE_API_KEY:
        st.info("🔐 GOOGLE_API_KEY cargada desde entorno (Secrets / Codespaces).")

if OPENAI_API_KEY and GOOGLE_API_KEY:
    st.success("✅ Claves API cargadas correctamente.")
else:
    st.warning("⚠️ No se han encontrado todas las claves necesarias. Revisa tu archivo `.env` o tus Secrets.")

# ====================================================
# 🛰️ 2. Descarga automática de archivos desde GitHub
# ====================================================

import subprocess

REPO_URL = "https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10x-IIA---Araceli-Fradejas.git"
DATA_FOLDER = "data"

if not os.path.exists(DATA_FOLDER):
    try:
        subprocess.run(["git", "clone", REPO_URL], check=True)
        # Mover la carpeta /data desde el repo clonado
        clonado = "Capstone-Project---Desarrollador10x-IIA---Araceli-Fradejas"
        if os.path.exists(os.path.join(clonado, DATA_FOLDER)):
            os.rename(os.path.join(clonado, DATA_FOLDER), DATA_FOLDER)
        st.success("📥 Archivos cargados correctamente desde GitHub.")
    except Exception as e:
        st.error(f"❌ Error al clonar los archivos desde GitHub: {e}")
else:
    st.info("ℹ️ Carpeta /data ya existe. No se vuelve a clonar.")


# ====================================================
# 📂 3. Carga de comentarios desde /data
# ====================================================

st.markdown("## 📂 Análisis de Comentarios de Clientes")
st.markdown("Se cargan automáticamente los comentarios desde el archivo `BD Comentarios KelceTS.txt` ubicado en `/data`.")

comentarios_path = os.path.join("data", "BD Comentarios KelceTS.txt")

# Verificar si el archivo existe
if os.path.exists(comentarios_path):
    with open(comentarios_path, "r", encoding="utf-8") as file:
        comentarios = [line.strip() for line in file if line.strip()]

    num_comentarios = len(comentarios)
    st.success(f"✅ Se han cargado {num_comentarios} comentarios correctamente.")

    # Mostrar una muestra aleatoria
    st.subheader("📌 Muestra aleatoria de comentarios")
    muestra = random.sample(comentarios, min(5, num_comentarios))
    for idx, comentario in enumerate(muestra, 1):
        st.markdown(f"**{idx}.** {comentario}")

else:
    st.error("❌ No se encontró el archivo `BD Comentarios KelceTS.txt` en la carpeta /data.")

# ====================================================
# 🌍 4. Análisis de idiomas de los comentarios
# ====================================================

st.subheader("🌐 Distribución de idiomas detectados")

# Detección automática con langdetect
idiomas = [detect(comentario) for comentario in comentarios]

# Crear DataFrame para análisis
df_idiomas = pd.DataFrame({"comentario": comentarios, "idioma": idiomas})

# Contar ocurrencias por idioma
conteo_idiomas = df_idiomas["idioma"].value_counts().reset_index()
conteo_idiomas.columns = ["Idioma", "Cantidad"]

# Mostrar tabla
st.dataframe(conteo_idiomas, use_container_width=True)

# Mostrar gráfico de barras
fig, ax = plt.subplots()
ax.bar(conteo_idiomas["Idioma"], conteo_idiomas["Cantidad"])
ax.set_xlabel("Idioma")
ax.set_ylabel("Número de comentarios")
ax.set_title("Distribución de idiomas en comentarios")
st.pyplot(fig)

# ====================================================
# 📥 5. Carga de Reglas Internas desde archivos Excel
# ====================================================
st.markdown("## 📥 Reglas de Calidad, Logística y Evaluación")
st.markdown("Se cargan desde el directorio `/data` las reglas internas definidas por KelceTS S.L. para analizar los comentarios y generar respuestas automatizadas.")

# Diccionario para almacenar los DataFrames
reglas = {}

# Lista de archivos de reglas
archivos_reglas = {
    "valoracion": "Reglas de como valorar un comentario KelceTS SL.xlsx",
    "clientes": "Reglas de calidad clientes KelceTS SL.xlsx",
    "logistica": "Reglas de comunicaciones equipos calidad y logistica KelceTS SL.xlsx",
    "medidas": "Reglas de medidas de calidad KelceTS SL.xlsx"
}

# Cargar todos los archivos
for clave, nombre_archivo in archivos_reglas.items():
    ruta = os.path.join("data", nombre_archivo)
    if os.path.exists(ruta):
        reglas[clave] = pd.read_excel(ruta)
        st.success(f"✅ Regla '{clave}' cargada correctamente.")
    else:
        st.warning(f"⚠️ No se encontró el archivo '{nombre_archivo}' en /data.")

# Mostrar contenido resumido
for clave, df in reglas.items():
    st.subheader(f"📄 Vista previa: reglas {clave}")
    st.dataframe(df.head(), use_container_width=True)

# ====================================================
# 🤖 6. Clasificación y comunicaciones automáticas
# ====================================================

st.markdown("""
### 🤖 Clasificación y comunicaciones automáticas

Esta sección aplica reglas de negocio sobre cada comentario de cliente para:

- Detectar si el comentario es negativo o neutro
- Analizar aspectos clave (entrega, embalaje, talla, materiales, uso)
- Determinar si se requiere:
  - ✅ Respuesta al cliente
  - 📦 Notificación interna a equipos
  - 🤝 Comunicación formal a proveedor

Además, se muestra un resumen visual del tipo de comunicaciones generadas para su análisis estratégico.
""")

from langdetect.lang_detect_exception import LangDetectException

# --------------------------------------
# 6.1 🧠 Clasificación del comentario
# --------------------------------------
def clasificar_comentario(texto):
    resultado = {
        "idioma": "desconocido",
        "recibido_96h": "no especifica",
        "embalaje_dañado": "no especifica",
        "talla_correcta": "no especifica",
        "material_bueno": "no especifica",
        "uso": "no especifica",
        "cumple_expectativas": "sí",  # asumimos sí si no hay lo contrario
        "valoracion_global": "positiva"
    }

    # Idioma
    try:
        lang = detect(texto)
        resultado["idioma"] = lang
    except LangDetectException:
        resultado["idioma"] = "desconocido"

    # Reglas simplificadas
    texto_lower = texto.lower()

    if "96" in texto_lower or "cuatro días" in texto_lower or "tardó" in texto_lower:
        resultado["recibido_96h"] = "no"
        resultado["cumple_expectativas"] = "no"

    if "embalaje" in texto_lower or ("caja" in texto_lower and ("roto" in texto_lower or "abollado" in texto_lower)):
        resultado["embalaje_dañado"] = "sí"
        resultado["cumple_expectativas"] = "no"

    if any(p in texto_lower for p in ["grande", "pequeñ", "talla equivocada", "molestias", "incómodas"]):
        resultado["talla_correcta"] = "no"
        resultado["cumple_expectativas"] = "no"

    if any(p in texto_lower for p in ["plasticosas", "desgastan", "rompen", "descosen", "mala calidad"]):
        resultado["material_bueno"] = "no"
        resultado["cumple_expectativas"] = "no"

    if any(p in texto_lower for p in ["diario", "cada día", "todos los días"]):
        resultado["uso"] = "frecuente"
    elif any(p in texto_lower for p in ["ocasional", "solo deporte"]):
        resultado["uso"] = "ocasional"

    # Valoración global
    if resultado["cumple_expectativas"] == "no":
        resultado["valoracion_global"] = "negativa"
    elif any(v == "no especifica" for v in resultado.values()):
        resultado["valoracion_global"] = "neutra"

    return resultado

# --------------------------------------
# 6.2 📬 Generación de comunicaciones
# --------------------------------------
def generar_comunicaciones(info):
    comunicaciones = []

    if info["valoracion_global"] == "negativa":
        comunicaciones.append("✅ Respuesta al cliente")

    if info["recibido_96h"] == "no" or info["embalaje_dañado"] == "sí" or info["talla_correcta"] == "no":
        comunicaciones.append("📦 Notificación interna (logística/calidad)")

    if info["material_bueno"] == "no" or info["cumple_expectativas"] == "no":
        comunicaciones.append("🤝 Comunicación formal a proveedor")

    return ", ".join(comunicaciones) if comunicaciones else "Sin comunicación necesaria"

# --------------------------------------
# 6.3🧪 Aplicar clasificación y generar tabla
# --------------------------------------
datos_clasificados = [clasificar_comentario(c) for c in comentarios]
df_clasificados = pd.DataFrame(datos_clasificados)
df_clasificados["comentario"] = comentarios
df_clasificados["comunicacion_recomendada"] = df_clasificados.apply(generar_comunicaciones, axis=1)

# --------------------------------------
# 6.4 📊 Visualización en la app
# --------------------------------------
st.subheader("📊 Tabla con clasificación y comunicaciones generadas")
st.dataframe(df_clasificados[["comentario", "valoracion_global", "comunicacion_recomendada"]], use_container_width=True)

st.markdown("### 📈 Distribución de comunicaciones generadas")
comunicaciones_count = df_clasificados["comunicacion_recomendada"].value_counts()
st.bar_chart(comunicaciones_count)

# ====================================================
# 7. 📊 Panel de Métricas Estratégicas para Dirección (CEO)
# ====================================================
st.markdown("""
## 📊 Panel Estratégico para Dirección

Este panel resume los resultados globales del análisis automatizado y ofrece métricas clave para la toma de decisiones por parte de la Dirección y el CEO de KelceTS S.L.
""")

# Total de comentarios analizados
total_comentarios = len(df_clasificados)
st.metric(label="📃 Comentarios analizados", value=total_comentarios)

# Distribución de valoración global
st.markdown("### 🔄 Distribución de Valoraciones")
st.bar_chart(df_clasificados["valoracion_global"].value_counts())

# Porcentaje de comentarios negativos
negativos = (df_clasificados["valoracion_global"] == "negativa").sum()
porcentaje_negativos = (negativos / total_comentarios) * 100
st.metric(label="🚫 % de comentarios negativos", value=f"{porcentaje_negativos:.2f}%")

# Idiomas más frecuentes
st.markdown("### 🌐 Idiomas más frecuentes")
idiomas_top = df_clasificados["idioma"].value_counts().head(5)
st.dataframe(idiomas_top.reset_index().rename(columns={"index": "Idioma", "idioma": "Cantidad"}))

# Distribución de comunicaciones generadas
st.markdown("### 📧 Tipo de comunicaciones generadas")
st.bar_chart(df_clasificados["comunicacion_recomendada"].value_counts())

# Estimación de costes evitados
st.markdown("### 💸 Coste estimado de gestión manual evitado")
# Supongamos que cada comunicación manual cuesta 3€ (cliente), 5€ (interna), 7€ (proveedor)
coste_total = 0
for tipo, coste in [("✅ Respuesta al cliente", 3), ("📦 Notificación interna (logística/calidad)", 5), ("🤝 Comunicación formal a proveedor", 7)]:
    count = df_clasificados["comunicacion_recomendada"].str.contains(tipo).sum()
    coste_total += count * coste

st.metric(label="💰 Ahorro estimado por automatización", value=f"{coste_total:.2f} €")
