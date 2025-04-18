import streamlit as st
st.set_page_config(page_title="Dashboard Dirección KelceTS", layout="wide")

# 📦 Librerías
import os
import pandas as pd
from langdetect import detect
from dotenv import load_dotenv
import plotly.express as px

# 🔐 Carga de claves API
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 📁 Carga de datos
@st.cache_data
def cargar_datos():
    ruta = "data/BD Comentarios KelceTS.txt"
    with open(ruta, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

comentarios = cargar_datos()

# 🧠 Análisis de comentarios
comentarios_procesados = []
for c in comentarios:
    try:
        idioma = detect(c)
    except:
        idioma = "desconocido"
    valor = "negativa" if any(p in c.lower() for p in ["roto", "desgaste", "plasticosa", "hundido"]) else "positiva"
    comunicacion = "📦 Notificación interna (logística/calidad)" if valor == "negativa" else "✅ Respuesta al cliente"
    comentarios_procesados.append({"comentario": c, "idioma": idioma, "valoracion_global": valor, "comunicacion_recomendada": comunicacion})

df = pd.DataFrame(comentarios_procesados)

# 🎨 Colores definidos
colores_valoraciones = {"negativa": "#E31837", "parcial": "#FFB612", "positiva": "#28A745"}

# ====================
# 🎯 ENCABEZADO CEO CON LOGO Y LEMA
# ====================
st.markdown("""
    <div style='background-color:#CE1126; padding:10px 20px; display:flex; flex-direction:column; align-items:center;'>
        <img src='https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/main/data/Kelce%20TS%20LOGO.png' style='height:80px; margin-bottom:10px;'>
        <h2 style='color:white; text-align:center;'>Dashboard Dirección KelceTS</h2>
        <h4 style='color:white;'>Decisiones estratégicas basadas en comentarios reales de clientes 👟</h4>
    </div>
""", unsafe_allow_html=True)

# 🧮 KPIs
st.title("📊 Dashboard Dirección KelceTS")
col1, col2, col3 = st.columns(3)
col1.metric("Comentarios analizados", len(df))
negativos = df[df["valoracion_global"] == "negativa"]
col2.metric("% Negativos", f"{len(negativos)/len(df)*100:.2f}%")
coste_estimado = (
    df["comunicacion_recomendada"].str.contains("cliente").sum()*3 +
    df["comunicacion_recomendada"].str.contains("interna").sum()*5 +
    df["comunicacion_recomendada"].str.contains("proveedor").sum()*7
)
col3.metric("Ahorro estimado", f"{coste_estimado:.2f} €")

# 📈 Visualización
st.markdown("## 📈 Análisis visual")
opciones = ["📈 Valoraciones", "🌍 Idiomas", "📬 Tipo de comunicaciones"]
eleccion = st.sidebar.radio("Tipo de visualización:", opciones)

if eleccion == "📈 Valoraciones":
    df_plot = df["valoracion_global"].value_counts().reset_index()
    df_plot.columns = ["Valoración", "Cantidad"]
    df_plot["Color"] = df_plot["Valoración"].map(colores_valoraciones).fillna("#999999")
    fig = px.bar(
        df_plot,
        x="Valoración",
        y="Cantidad",
        color="Valoración",
        color_discrete_map=colores_valoraciones
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
elif eleccion == "🌍 Idiomas":
    df_agrupado = df.groupby("idioma")["valoracion_global"].value_counts().unstack().fillna(0)
    df_agrupado["total"] = df_agrupado.sum(axis=1)
    df_agrupado["predominante"] = df_agrupado[["positiva", "negativa"]].idxmax(axis=1)
    df_agrupado["color"] = df_agrupado["predominante"].map(colores_valoraciones)

    emoji_flags = {
        "es": "🇪🇸", "de": "🇩🇪", "fr": "🇫🇷", "it": "🇮🇹", "pt": "🇵🇹", "nl": "🇳🇱",
        "pl": "🇵🇱", "fi": "🇫🇮", "sv": "🇸🇪", "da": "🇩🇰", "el": "🇬🇷", "hu": "🇭🇺",
        "cs": "🇨🇿", "ro": "🇷🇴", "bg": "🇧🇬", "hr": "🇭🇷", "et": "🇪🇪", "sk": "🇸🇰",
        "sl": "🇸🇮", "lv": "🇱🇻", "lt": "🇱🇹", "mt": "🇲🇹", "ga": "🇮🇪", "en": "🇬🇧"
    }
    df_agrupado = df_agrupado.reset_index()
    df_agrupado["label"] = df_agrupado["idioma"].apply(lambda x: f"{emoji_flags.get(x, '')} {x}")

    fig = px.bar(
        df_agrupado,
        x="label",
        y="total",
        text="total",
        color="predominante",
        color_discrete_map=colores_valoraciones,
        title="Distribución por idioma con valoración dominante",
        hover_data={
            "positiva": True,
            "negativa": True,
            "total": False,
            "label": False,
            "predominante": False
        }
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig)

elif eleccion == "📬 Tipo de comunicaciones":
    df_plot = df["comunicacion_recomendada"].value_counts().reset_index()
    df_plot.columns = ["Tipo de comunicación", "Cantidad"]
    fig = px.bar(df_plot, x="Tipo de comunicación", y="Cantidad", color="Tipo de comunicación", color_discrete_sequence=["#FFB612", "#28A745", "#E31837"])
    st.plotly_chart(fig)

# ✅ Mensaje final
st.markdown("<p style='text-align:center; color:green; font-weight:bold;'>✅ Datos reales cargados desde /data</p>", unsafe_allow_html=True)

# 👣 Footer
st.markdown("""
<hr style='margin-top:50px;'>
<div style='text-align:center; font-size:small; color:gray;'>
    Asistente de IA para un call center desarrollado por Araceli Fradejas Muñoz, Abril 2025<br>
    Curso Desarrollador10X realizado en el <a href='https://iia.es/' target='_blank' style='color:gray; text-decoration:underline;'>Instituto de Inteligencia Artificial</a><br>
    KelceTS S.L. – Proyecto académico ficticio como Capstone Project de IA generativa
</div>
""", unsafe_allow_html=True)
