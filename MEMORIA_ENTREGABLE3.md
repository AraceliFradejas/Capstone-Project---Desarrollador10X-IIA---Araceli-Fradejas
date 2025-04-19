# MEMORIA TÉCNICA: DASHBOARD ESTRATÉGICO KELCETS S.L.

![Logo KelceTS](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png)

## 📊 PROYECTO CAPSTONE: DESARROLLADOR 10X - INSTITUTO DE INTELIGENCIA ARTIFICIAL

**Autora:** Araceli Fradejas Muñoz  
**Fecha de entrega:** 21 de abril de 2025  
**Versión:** 3.0

---

## 📝 1. INTRODUCCIÓN

### 1.1. Descripción general

Este documento presenta la memoria técnica del proyecto capstone desarrollado para el curso Desarrollador 10X del Instituto de Inteligencia Artificial. El proyecto consiste en un **dashboard estratégico para la startup ficticia KelceTS S.L.**, especializada en la venta de zapatillas online en Europa.

El objetivo principal ha sido crear una herramienta analítica que permita a la dirección y al CEO de KelceTS visualizar, analizar y tomar decisiones estratégicas basadas en los comentarios que los clientes dejan en diferentes canales e idiomas.

### 1.2. Problema abordado

KelceTS, como empresa de e-commerce en crecimiento, necesita:

- Procesar y analizar grandes volúmenes de comentarios de clientes en múltiples idiomas
- Detectar patrones y tendencias en las valoraciones de sus productos
- Determinar áreas críticas que requieren mejora (calidad, logística, atención)
- Estimar costes asociados a la gestión de incidencias
- Tomar decisiones estratégicas basadas en datos reales

La solución desarrollada supera el reto de convertir datos textuales no estructurados en información analítica de valor para la toma de decisiones ejecutivas.

---

## 🎯 2. OBJETIVOS DEL PROYECTO

### 2.1. Objetivo general

Desarrollar un dashboard interactivo que permita visualizar y analizar estratégicamente los comentarios de clientes de KelceTS S.L., facilitando la toma de decisiones basadas en datos para mejorar la experiencia del cliente y optimizar procesos internos.

### 2.2. Objetivos específicos

1. **Visualización de datos:** Crear representaciones gráficas intuitivas que muestren la distribución y tendencias de los comentarios.
2. **Análisis multilingüe:** Permitir el análisis de comentarios en diferentes idiomas europeos.
3. **Segmentación por variables críticas:** Analizar métricas clave como tiempos de entrega, calidad de materiales, tallas y embalaje.
4. **Estimación de costes:** Calcular los costes asociados a las diferentes acciones derivadas de los comentarios.
5. **Automatización de informes:** Generar informes ejecutivos en PDF con los principales hallazgos y recomendaciones.
6. **Interfaz intuitiva:** Desarrollar una interfaz de usuario limpia y profesional con la identidad corporativa de KelceTS.

---

## 💻 3. METODOLOGÍA Y DESARROLLO

### 3.1. Metodología de trabajo

El proyecto se ha desarrollado siguiendo una metodología ágil adaptada, con entregables incrementales:

1. **Entregable 1:** Análisis exploratorio inicial y definición de requisitos.
2. **Entregable 2:** Desarrollo de funcionalidades core y primeras visualizaciones.
3. **Entregable 3 (actual):** Dashboard completo con todas las funcionalidades integradas.

### 3.2. Tecnologías utilizadas

#### 3.2.1. Lenguajes y frameworks

- **Python 3.10:** Lenguaje principal de desarrollo
- **Streamlit 1.32:** Framework para la creación del dashboard interactivo
- **Pandas 2.0:** Manipulación y análisis de datos
- **NumPy 1.24:** Operaciones matemáticas y análisis numérico
- **Plotly 5.18:** Creación de visualizaciones interactivas

#### 3.2.2. Bibliotecas adicionales

- **ReportLab 4.0:** Generación de informes PDF profesionales
- **python-dotenv 1.0:** Gestión segura de variables de entorno
- **urllib:** Acceso a recursos remotos (logo, datos)

#### 3.2.3. APIs y servicios externos

- **OpenAI API:** Procesamiento avanzado de lenguaje natural (fallback principal)
- **Google Gemini API:** Alternativa para procesamiento de lenguaje natural (fallback secundario)
- **GitHub:** Alojamiento del código fuente y archivos de datos

### 3.3. Estructura del código

El proyecto mantiene una estructura modular con las siguientes funciones principales:

- **Configuración inicial:** Parámetros de página y estilos CSS personalizados
- **Carga y procesamiento de datos:** Obtención de datos desde GitHub o localmente
- **Generación de visualizaciones:** Funciones específicas para cada tipo de gráfico
- **Creación de PDF:** Función para generar informes ejecutivos descargables
- **Interfaz de usuario:** Componentes Streamlit para la visualización y interacción

### 3.4. Fuentes de datos

Los datos utilizados provienen de diversas fuentes internas de KelceTS:

- **BD Comentarios KelceTS.txt:** Base principal de comentarios de clientes
- **Informe_Final_KelceTS.xlsx:** Dataset procesado con valoraciones categorizadas
- **Reglas de calidad clientes KelceTS SL.xlsx:** Criterios para evaluación de calidad
- **Reglas de comunicaciones equipos calidad y logística KelceTS SL.xlsx:** Protocolos de comunicación interna
- **Reglas de como valorar un comentario KelceTS SL.xlsx:** Guía de análisis de comentarios
- **Reglas de medidas de calidad KelceTS SL.xlsx:** Estándares de calidad y medidas correctivas

---

## ⚙️ 4. FUNCIONALIDADES IMPLEMENTADAS

### 4.1. Dashboard interactivo

- **Indicadores clave (KPIs):** Métricas principales como total de comentarios, porcentaje de valoraciones negativas y coste estimado total.
- **Selector de visualizaciones:** Menú lateral para alternar entre diferentes tipos de análisis.
- **Responsividad:** Adaptación a diferentes dispositivos y tamaños de pantalla.
- **Estilos personalizados:** Implementación de la identidad visual de KelceTS con colores corporativos.

### 4.2. Análisis de datos

- **Distribución de valoraciones:** Visualización de comentarios positivos, negativos y neutros.
- **Análisis por idioma:** Distribución geográfica de comentarios con indicadores de valoración predominante.
- **Tipo de comunicaciones:** Categorización de las comunicaciones generadas (internas, cliente, pendientes).
- **Variables de calidad:** Análisis detallado de factores críticos como envíos en 96h, embalaje, tallas y materiales.

### 4.3. Generación de informes

- **Informes PDF automáticos:** Creación de informes ejecutivos de 3 páginas con los principales hallazgos.
- **Visualizaciones en alta resolución:** Gráficos optimizados para impresión.
- **Recomendaciones automáticas:** Generación de conclusiones basadas en los datos analizados.
- **Información corporativa:** Inclusión de logo y datos de la empresa en cada página.

### 4.4. Cálculo de costes

- **Estimación de costes base:** Cálculo de costes por tipo de comunicación.
- **Penalizaciones:** Aplicación automática de costes adicionales según las incidencias detectadas.
- **Medidas correctivas:** Identificación de acciones necesarias para cada tipo de problema.
- **Coste total:** Agregación de todos los costes para estimación global.

---

## 📈 5. RESULTADOS Y ANÁLISIS

### 5.1. Dashboard resultante

El dashboard final permite un análisis exhaustivo de los comentarios de clientes, con las siguientes características:

- **Interfaz clara y profesional** con la identidad visual de KelceTS
- **Visualizaciones interactivas** que permiten explorar los datos desde diferentes perspectivas
- **Métricas actualizadas** en tiempo real con la carga de nuevos datos
- **Filtrado y segmentación** de datos según diferentes variables

### 5.2. Hallazgos principales

Del análisis de datos realizado se pueden extraer las siguientes conclusiones:

1. **Distribución de valoraciones:** Se observa un balance entre comentarios positivos y negativos, con áreas específicas de mejora.
2. **Distribución lingüística:** Los comentarios en español, alemán y francés son predominantes, lo que refleja los mercados principales de KelceTS.
3. **Variables críticas:** Los problemas relacionados con tiempos de entrega y calidad de materiales son los que generan mayor número de valoraciones negativas.
4. **Impacto económico:** Las incidencias de calidad y logística suponen un impacto económico significativo a través de compensaciones y gestión de incidencias.

### 5.3. Limitaciones y oportunidades de mejora

El proyecto actual presenta algunas limitaciones que podrían abordarse en futuras iteraciones:

- **Análisis temporal:** Incorporar análisis de tendencias y evolución a lo largo del tiempo
- **Integración con APIs en tiempo real:** Conexión directa con sistemas de comentarios y redes sociales
- **Predicción:** Implementar modelos predictivos para anticipar problemas de calidad
- **Personalización avanzada:** Añadir más opciones de filtrado y personalización de visualizaciones

---

## 🔄 6. FLUJO DE TRABAJO Y PROCESOS

### 6.1. Carga y preprocesamiento de datos

1. **Obtención de datos:** Carga desde GitHub o fuentes locales
2. **Limpieza y transformación:** Procesamiento para estructurar la información
3. **Enriquecimiento:** Cálculo de métricas adicionales y categorización
4. **Validación:** Verificación de integridad y consistencia de los datos

### 6.2. Análisis y generación de visualizaciones

1. **Definición de KPIs:** Identificación de métricas relevantes
2. **Segmentación:** Agrupación de datos según variables clave
3. **Visualización:** Creación de gráficos interactivos con Plotly
4. **Interpretación:** Extracción de conclusiones basadas en patrones observados

### 6.3. Generación de informes PDF

1. **Diseño de plantilla:** Estructura visual de los informes ejecutivos
2. **Generación de gráficos:** Creación de visualizaciones optimizadas para PDF
3. **Cálculo de recomendaciones:** Análisis automático para generar conclusiones
4. **Compilación:** Integración de todos los elementos en un documento cohesionado

---

## 💡 7. IMPACTO Y VALOR AÑADIDO

### 7.1. Impacto en la empresa

La solución desarrollada aporta valor a KelceTS en múltiples dimensiones:

- **Toma de decisiones basada en datos:** Facilita decisiones estratégicas fundamentadas en información real.
- **Optimización de procesos:** Identifica áreas críticas de mejora en logística y calidad.
- **Reducción de costes:** Permite anticipar y mitigar problemas recurrentes.
- **Mejora de la experiencia del cliente:** Facilita la detección y solución de problemas frecuentes.

### 7.2. Innovación tecnológica

El proyecto integra diversas tecnologías innovadoras:

- **Análisis multilingüe automatizado:** Procesamiento de comentarios en diferentes idiomas.
- **Visualización interactiva:** Gráficos dinámicos que permiten exploración profunda.
- **Generación automatizada de informes:** Creación de documentos ejecutivos sin intervención manual.
- **Integración con APIs de IA:** Uso de modelos avanzados de procesamiento de lenguaje natural.

---

## 🔧 8. INSTALACIÓN Y DESPLIEGUE

### 8.1. Requisitos previos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)
- Acceso a Internet (para cargar datos desde GitHub)
- Opcionalmente: Claves de API para OpenAI y Google Gemini

### 8.2. Instrucciones de instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/AraceliFradejas/kelcets-dashboard.git
   cd kelcets-dashboard
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno (opcional):**
   Crear un archivo `.env` con las siguientes variables:
   ```
   OPENAI_API_KEY=su_clave_api_openai
   GOOGLE_API_KEY=su_clave_api_google
   ```

4. **Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```

### 8.3. Configuración adicional

La aplicación está diseñada para funcionar sin configuración adicional, pero se pueden ajustar los siguientes parámetros:

- **Fuente de datos:** Modificar URLs en `cargar_excel()` para usar otros datasets
- **Estilos visuales:** Personalizar colores y estilos en la sección de configuración CSS
- **Variables de análisis:** Ajustar las variables específicas en las funciones de generación de gráficos

---

## 📚 9. LECCIONES APRENDIDAS Y CONCLUSIONES

### 9.1. Desafíos enfrentados

Durante el desarrollo del proyecto se enfrentaron varios desafíos:

1. **Procesamiento multilingüe:** Gestión de comentarios en diferentes idiomas con estructuras gramaticales diversas.
2. **Integración de múltiples fuentes de datos:** Combinación coherente de datos de diversas fuentes y formatos.
3. **Generación automática de informes PDF:** Creación de documentos profesionales con visualizaciones de alta calidad.
4. **Usabilidad del dashboard:** Diseño de una interfaz intuitiva sin comprometer la profundidad analítica.

### 9.2. Soluciones implementadas

Para superar estos desafíos se aplicaron las siguientes soluciones:

1. **Fallback entre servicios de IA:** Sistema de respaldo entre OpenAI y Google Gemini para procesamiento lingüístico.
2. **Estructura de datos unificada:** Diseño de un modelo de datos coherente para facilitar el análisis integrado.
3. **Optimización de visualizaciones:** Ajuste de parámetros gráficos para garantizar legibilidad en diferentes formatos.
4. **Diseño centrado en el usuario:** Interfaz simplificada con elementos visuales claros y consistentes.

### 9.3. Conclusiones finales

Este proyecto demuestra el potencial del análisis de datos y las visualizaciones interactivas para transformar información no estructurada en conocimiento accionable. La combinación de tecnologías como Python, Streamlit, Plotly y ReportLab ha permitido crear una solución completa que aporta valor real en un contexto empresarial.

El dashboard desarrollado no solo cumple con los objetivos establecidos inicialmente, sino que establece una base sólida para futuras iteraciones y mejoras, demostrando la aplicación práctica de los conocimientos adquiridos durante el curso Desarrollador 10X.

---

## 📝 10. ANEXOS

### 10.1. Referencias bibliográficas

- Documentación oficial de Streamlit: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- Documentación de Plotly: [https://plotly.com/python/](https://plotly.com/python/)
- Documentación de ReportLab: [https://www.reportlab.com/docs/reportlab-userguide.pdf](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- Python Data Science Handbook, Jake VanderPlas (2016)

### 10.2. Agradecimientos

- A los instructores y mentores del curso Desarrollador 10X del Instituto de Inteligencia Artificial por su guía y apoyo continuo.
- Al equipo ficticio de KelceTS S.L. por proporcionar el contexto de negocio y los requisitos para este proyecto.

---

Memoria elaborada por **Araceli Fradejas Muñoz**  
Curso Desarrollador 10X - Instituto de Inteligencia Artificial  
Abril 2025