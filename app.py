import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import io

# Configuración de la página
st.set_page_config(
    page_title="KelceTS - Dashboard de Comunicaciones",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título del dashboard
st.title("📊 Dashboard de Análisis de Comunicaciones - KelceTS")
st.markdown("---")

@st.cache_data(ttl=10)  # Reducimos el tiempo de caché a 10 segundos
def cargar_datos():
    try:
        # Rutas de posibles ubicaciones de los archivos
        rutas_posibles = [
            "analisis_comentarios_kelcets.xlsx",  # Directorio actual
            "./analisis_comentarios_kelcets.xlsx",
            "../analisis_comentarios_kelcets.xlsx",
            "/workspaces/codespaces-blank/analisis_comentarios_kelcets.xlsx",  # Ruta específica de Codespaces
            # Agrega cualquier otra ruta que pueda ser relevante
        ]
        
        # Intentar cargar desde cada ruta posible
        df = None
        df_comunicaciones = None
        df_estadisticas = None
        archivo_cargado = None
        
        for ruta in rutas_posibles:
            try:
                st.sidebar.text(f"Intentando cargar: {ruta}")
                if os.path.exists(ruta):
                    # Cargar los datos desde el archivo Excel
                    df = pd.read_excel(ruta, sheet_name='Resumen')
                    df_comunicaciones = pd.read_excel(ruta, sheet_name='Comunicaciones')
                    df_estadisticas = pd.read_excel(ruta, sheet_name='Estadísticas')
                    archivo_cargado = ruta
                    st.sidebar.success(f"Datos cargados desde: {ruta}")
                    break
            except Exception as e:
                st.sidebar.error(f"Error al cargar {ruta}: {e}")
        
        if df is None:
            # Si no se pudo cargar el archivo, mostrar los archivos disponibles en el directorio
            st.sidebar.warning("No se pudo cargar el archivo. Archivos disponibles:")
            try:
                archivos = os.listdir(".")
                for archivo in archivos:
                    st.sidebar.text(f" - {archivo}")
            except:
                st.sidebar.error("No se pudo listar los archivos")
            
            # Usar datos simulados como respaldo
            st.warning("⚠️ Usando datos simulados como respaldo")
            data_resumen = {
                'ID': list(range(1, 11)),
                'Comentario_Original': ['Ejemplo de comentario 1', 'Ejemplo de comentario 2'] * 5,
                'Idioma': ['español', 'alemán', 'español', 'finés', 'portugués'] * 2,
                'Valoracion': ['positiva', 'negativa', 'positiva', 'negativa', 'neutra'] * 2,
                'Envio_96h': ['sí', 'no', 'sí', 'no', 'no mencionado'] * 2,
                'Embalaje_Danado': ['no', 'sí', 'no', 'no', 'no mencionado'] * 2,
                'Talla_Correcta': ['sí', 'no', 'sí', 'no', 'no mencionado'] * 2,
                'Materiales_Calidad': ['sí', 'no', 'parcialmente', 'no', 'no mencionado'] * 2,
                'Tipo_Uso': ['diario', 'ocasional', 'diario', 'ocasional', 'no mencionado'] * 2,
                'Cumple_Expectativas': ['sí', 'no', 'parcialmente', 'no', 'no mencionado'] * 2
            }
            
            data_estadisticas = {
                'Métrica': [
                    'Total Comentarios',
                    'Valoraciones Positivas',
                    'Valoraciones Negativas',
                    'Valoraciones Neutras',
                    'Problemas de Calidad Materiales',
                    'Problemas de Talla',
                    'Problemas de Envío',
                    'Problemas de Embalaje',
                    'Satisfacción General (%)'
                ],
                'Valor': [10, 4, 4, 2, 4, 4, 4, 2, 60]
            }
            
            df = pd.DataFrame(data_resumen)
            df_comunicaciones = pd.DataFrame(data_resumen)
            df_estadisticas = pd.DataFrame(data_estadisticas)
            
        return df, df_comunicaciones, df_estadisticas, (archivo_cargado is not None)
        
    except Exception as e:
        st.error(f"Error en la función cargar_datos: {e}")
        return None, None, None, False
    
    # Crear DataFrames
    df = pd.DataFrame(data_resumen)
    df_comunicaciones = pd.DataFrame(data_resumen)  # Usando los mismos datos como ejemplo
    df_estadisticas = pd.DataFrame(data_estadisticas)
    
    return df, df_comunicaciones, df_estadisticas, True

# Barra lateral para navegación
st.sidebar.title("Navegación")

# Botón de refrescar en la barra lateral
with st.sidebar:
    st.sidebar.write("Última actualización de datos:")
    st.sidebar.write(pd.Timestamp.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    if st.button('🔄 Refrescar datos'):
        # Limpiar todas las cachés
        st.cache_data.clear()
        st.cache_resource.clear()
        st.success("Caché limpiada. Recargando datos...")
        st.rerun()
        
# Cargar datos - Movido después del botón de refrescar para asegurar que se carguen datos frescos
df, df_comunicaciones, df_estadisticas, datos_cargados = cargar_datos()

if datos_cargados:
    # Sección 1: Resumen General
    if seccion == "Resumen General":
        st.header("📈 Resumen General")
        
        # Mostrar KPIs en columnas
        col1, col2, col3, col4 = st.columns(4)
        
        # Extraer valores de estadísticas
        total_comentarios = df_estadisticas[df_estadisticas["Métrica"] == "Total Comentarios"]["Valor"].values[0]
        valoraciones_positivas = df_estadisticas[df_estadisticas["Métrica"] == "Valoraciones Positivas"]["Valor"].values[0]
        valoraciones_negativas = df_estadisticas[df_estadisticas["Métrica"] == "Valoraciones Negativas"]["Valor"].values[0]
        satisfaccion_general = df_estadisticas[df_estadisticas["Métrica"] == "Satisfacción General (%)"]["Valor"].values[0]
        
        with col1:
            st.metric("Total Comentarios", f"{total_comentarios}")
        
        with col2:
            st.metric("Valoraciones Positivas", f"{valoraciones_positivas}")
        
        with col3:
            st.metric("Valoraciones Negativas", f"{valoraciones_negativas}")
        
        with col4:
            st.metric("Satisfacción General", f"{satisfaccion_general}%")
        
        st.markdown("---")
        
        # Gráfico de distribución de valoraciones
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribución de Valoraciones")
            fig_valoraciones = px.pie(
                names=df["Valoracion"].value_counts().index, 
                values=df["Valoracion"].value_counts().values,
                color=df["Valoracion"].value_counts().index,
                color_discrete_map={"positiva":"green", "negativa":"red", "neutra":"blue"},
                hole=0.4
            )
            st.plotly_chart(fig_valoraciones, use_container_width=True)
        
        with col2:
            st.subheader("Cumplimiento de Expectativas")
            fig_expectativas = px.pie(
                names=df["Cumple_Expectativas"].value_counts().index,
                values=df["Cumple_Expectativas"].value_counts().values,
                color=df["Cumple_Expectativas"].value_counts().index,
                color_discrete_map={"sí":"green", "no":"red", "parcialmente":"orange", "no mencionado":"gray"},
                hole=0.4
            )
            st.plotly_chart(fig_expectativas, use_container_width=True)
        
        # Problemas detectados
        st.subheader("Principales Problemas Detectados")
        
        problemas_df = pd.DataFrame({
            "Problema": ["Materiales", "Talla", "Envío", "Embalaje"],
            "Cantidad": [
                df_estadisticas[df_estadisticas["Métrica"] == "Problemas de Calidad Materiales"]["Valor"].values[0],
                df_estadisticas[df_estadisticas["Métrica"] == "Problemas de Talla"]["Valor"].values[0],
                df_estadisticas[df_estadisticas["Métrica"] == "Problemas de Envío"]["Valor"].values[0],
                df_estadisticas[df_estadisticas["Métrica"] == "Problemas de Embalaje"]["Valor"].values[0]
            ]
        })
        
        fig_problemas = px.bar(
            problemas_df, 
            x="Problema", 
            y="Cantidad",
            color="Problema"
        )
        st.plotly_chart(fig_problemas, use_container_width=True)
    
    # Sección 2: Análisis por Idioma
    elif seccion == "Análisis por Idioma":
        st.header("🌍 Análisis por Idioma")
        
        # Distribución de idiomas
        st.subheader("Distribución de Comentarios por Idioma")
        fig_idiomas = px.pie(
            names=df["Idioma"].value_counts().index,
            values=df["Idioma"].value_counts().values
        )
        st.plotly_chart(fig_idiomas, use_container_width=True)
    
    # Sección 3: Análisis de Satisfacción
    elif seccion == "Análisis de Satisfacción":
        st.header("😊 Análisis de Satisfacción")
        
        # Ejemplo simple para demostración
        st.subheader("Satisfacción por tipo de problema")
        st.bar_chart(df["Materiales_Calidad"].value_counts())
    
    # Sección 4: Problemas Detectados
    elif seccion == "Problemas Detectados":
        st.header("⚠️ Problemas Detectados")
        
        # Filtro por tipo de problema
        tipo_problema = st.radio(
            "Selecciona el tipo de problema:",
            ["Materiales", "Talla", "Envío", "Embalaje"]
        )
        
        st.write(f"Datos filtrados para problema de {tipo_problema}")
        st.dataframe(df.head(3))
    
    # Sección 5: Datos en Bruto
    else:  # Datos en Bruto
        st.header("📋 Datos en Bruto")
        st.dataframe(df)

else:
    st.error("No se pudieron cargar los datos.")

# Pie de página
st.markdown("---")
st.markdown("Desarrollado para KelceTS S.L. | Dashboard de Análisis de Comentarios de Clientes")
