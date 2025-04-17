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
# 🌍 4strea. Análisis de idiomas de los comentarios
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

