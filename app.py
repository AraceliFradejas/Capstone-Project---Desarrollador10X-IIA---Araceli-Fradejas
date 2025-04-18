import streamlit as st
st.set_page_config(page_title="Dashboard Dirección KelceTS", layout="wide")

# 📦 Librerías
import os
import pandas as pd
from langdetect import detect
from dotenv import load_dotenv
import plotly.express as px
import urllib.request
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader

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

def generar_pdf(resumen):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # Logo personalizado
    logo_url = "https://raw.githubusercontent.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---AraceliFradejas/main/data/KelceTS_logo.png"
    logo = ImageReader(logo_url)
    c.drawImage(logo, x=2*cm, y=26*cm, width=4*cm, height=4*cm, mask='auto')

    # Título principal
    c.setFont("Helvetica-Bold", 16)
    c.drawString(7*cm, 28*cm, "Informe ejecutivo KelceTS")

    # Cabecera resumen
    c.setFont("Helvetica", 10)
    y = 26*cm
    for linea in resumen:
        c.drawString(2*cm, y, linea)
        y -= 0.7*cm

    # Footer institucional
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(A4[0] / 2, 1.5*cm, "KelceTS S.L. – Proyecto académico ficticio | Curso Desarrollador10X – Instituto de Inteligencia Artificial")

    c.save()
    buffer.seek(0)
    return buffer

try:
    df = cargar_excel()

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

    # Descarga personalizada del PDF profesional
    resumen = [
        f"Comentarios analizados: {len(df)}",
        f"% Negativos: {len(df[df['valoracion'] == 'negativa']) / len(df) * 100:.2f}%",
        f"Coste operativo total estimado: {df['coste_total'].sum():,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."),
    ]

    st.download_button(
        label="📄 Descargar informe ejecutivo en PDF",
        data=generar_pdf(resumen),
        file_name="Resumen_KelceTS.pdf",
        mime="application/pdf",
        help="Haz clic para descargar el resumen ejecutivo generado con IA",
        use_container_width=True,
        type="primary"
    )

except Exception as e:
    st.warning(f"⚠️ No se pudo cargar el Excel de comparación: {e}")
