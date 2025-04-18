import streamlit as st
st.set_page_config(page_title="Dashboard Dirección KelceTS", layout="wide")

# 📦 Librerías
import os
import pandas as pd
from langdetect import detect
from dotenv import load_dotenv
import plotly.express as px
import urllib.request

# 🔐 Carga de claves API
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 📁 Carga de Excel
@st.cache_data
def cargar_excel():
    excel_url = "https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---AraceliFradejas/main/data/Informe_Final_KelceTS.xlsx"
    excel_path = "data/Informe_Final_KelceTS.xlsx"
    if not os.path.exists(excel_path):
        urllib.request.urlretrieve(excel_url, excel_path)
    return pd.read_excel(excel_path)

try:
    df = cargar_excel()

    if "tipo_comunicacion" not in df.columns:
        df["tipo_comunicacion"] = df["valoracion"].apply(lambda v: (
            "📦 Notificación interna (logística/calidad)" if v == "negativa" else
            "✅ Respuesta al cliente" if v == "positiva" else
            "📧 Comunicación pendiente de revisión"
        ))

    # Costes base por tipo de comunicación
    coste_unitario = {
        "📦 Notificación interna (logística/calidad)": 5,
        "✅ Respuesta al cliente": 3,
        "📧 Comunicación pendiente de revisión": 4
    }
    df["coste_base"] = df["tipo_comunicacion"].map(coste_unitario)

    # Penalizaciones adicionales por medidas de calidad
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

    # ====================
    # 🎯 ENCABEZADO CEO CON LOGO Y LEMA
    # ====================
    st.markdown("""
        <div style='background-color:#CE1126; padding:10px 20px; display:flex; flex-direction:column; align-items:center;'>
            <img src='https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---AraceliFradejas/main/data/Kelce%20TS%20LOGO.png' style='height:80px; margin-bottom:10px;'>
            <h2 style='color:white; text-align:center;'>Dashboard Dirección KelceTS</h2>
            <h4 style='color:white;'>Decisiones estratégicas basadas en comentarios reales de clientes 👟</h4>
        </div>
    """, unsafe_allow_html=True)

    # 🎮 Selector de visualización
    opciones = {
        "📈 Valoraciones": "📈 Distribución por valoración",
        "🌍 Idiomas": "🌍 Distribución por idioma con valoración dominante",
        "📬 Tipo de comunicaciones": "📬 Distribución por tipo de comunicación"
    }
    eleccion = st.sidebar.radio("Tipo de visualización:", list(opciones.keys()))

    # 🎯 KPIs desde Excel
    st.title("📊 Dashboard Dirección KelceTS")
    col1, col2, col3 = st.columns(3)
    col1.metric("Comentarios analizados", len(df))
    col2.metric("% Negativos", f"{len(df[df['valoracion'] == 'negativa']) / len(df) * 100:.2f}%")
    coste_formateado = f"{df['coste_total'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    col3.metric("Coste estimado", f"{coste_formateado} €")

    # 🎨 Colores definidos
    colores_valoraciones = {"negativa": "#E31837", "parcial": "#FFB612", "positiva": "#28A745"}

    # 📈 Visualización
    st.markdown(f"## {opciones[eleccion]}")

    if eleccion == "📈 Valoraciones":
        df_plot = df["valoracion"].value_counts().reset_index()
        df_plot.columns = ["Valoración", "Cantidad"]
        fig = px.bar(
            df_plot,
            x="Valoración",
            y="Cantidad",
            color="Valoración",
            color_discrete_map=colores_valoraciones
        )
        st.plotly_chart(fig, use_container_width=True)

    elif eleccion == "🌍 Idiomas":
        if "idioma" in df.columns and "valoracion" in df.columns:
            df_agrupado = df.groupby("idioma")["valoracion"].value_counts().unstack().fillna(0)
            if "positiva" not in df_agrupado.columns:
                df_agrupado["positiva"] = 0
            if "negativa" not in df_agrupado.columns:
                df_agrupado["negativa"] = 0
            df_agrupado["total"] = df_agrupado.sum(axis=1)
            df_agrupado["predominante"] = df_agrupado[["positiva", "negativa"]].idxmax(axis=1)
            df_agrupado["color"] = df_agrupado["predominante"].map(colores_valoraciones)
            df_agrupado = df_agrupado.reset_index()

            emoji_flags = {
                "es": "🇪🇸", "de": "🇩🇪", "fr": "🇫🇷", "it": "🇮🇹", "pt": "🇵🇹", "nl": "🇳🇱",
                "pl": "🇵🇱", "fi": "🇫🇮", "sv": "🇸🇪", "da": "🇩🇰", "el": "🇬🇷", "hu": "🇭🇺",
                "cs": "🇨🇿", "ro": "🇷🇴", "bg": "🇧🇬", "hr": "🇭🇷", "et": "🇪🇪", "sk": "🇸🇰",
                "sl": "🇸🇮", "lv": "🇱🇻", "lt": "🇱🇹", "mt": "🇲🇹", "ga": "🇮🇪", "en": "🇬🇧"
            }
            df_agrupado["label"] = df_agrupado["idioma"].apply(lambda x: f"{emoji_flags.get(x, '')} {x}")

            fig = px.bar(
                df_agrupado,
                x="label",
                y="total",
                text="total",
                color="predominante",
                color_discrete_map=colores_valoraciones
            )
            fig.update_traces(textposition="outside")
            st.plotly_chart(fig)

    elif eleccion == "📬 Tipo de comunicaciones":
        df_plot = df["tipo_comunicacion"].value_counts().reset_index()
        df_plot.columns = ["Tipo de comunicación", "Cantidad"]
        fig = px.bar(
            df_plot,
            x="Tipo de comunicación",
            y="Cantidad",
            color="Tipo de comunicación",
            color_discrete_sequence=["#FFB612", "#28A745", "#E31837"]
        )
        st.plotly_chart(fig)

    # ✅ Datos reales cargados
    st.markdown("<p style='text-align:center; color:green; font-weight:bold;'>✅ Datos reales cargados desde /data</p>", unsafe_allow_html=True)

except Exception as e:
    st.warning(f"⚠️ No se pudo cargar el Excel de comparación: {e}")

# 👣 Footer
st.markdown("""
<hr style='margin-top:50px;'>
<div style='text-align:center; font-size:small; color:gray;'>
    Asistente de IA para un call center desarrollado por Araceli Fradejas Muñoz, Abril 2025<br>
    Curso Desarrollador10X realizado en el <a href='https://iia.es/' target='_blank' style='color:gray; text-decoration:underline;'>Instituto de Inteligencia Artificial</a><br>
    KelceTS S.L. – Proyecto académico ficticio como Capstone Project de IA generativa
</div>
""", unsafe_allow_html=True)
