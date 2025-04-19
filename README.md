# Dashboard Estratégico KelceTS S.L. 👟

![Logo KelceTS](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/raw/main/data/KelceTS_logo.png)

## 🌟 Descripción (Español)

Dashboard analítico desarrollado como proyecto final del curso Desarrollador10X del Instituto de Inteligencia Artificial. Esta aplicación está diseñada para la empresa ficticia KelceTS S.L., una startup especializada en la venta de zapatillas online en Europa.

El dashboard ofrece a la Dirección y al CEO una **visión analítica y estratégica** sobre los comentarios de clientes en diferentes idiomas y canales, permitiendo tomar decisiones basadas en datos reales.

### 🎯 Objetivos de la aplicación

- Visualizar el volumen y evolución de comentarios recibidos
- Analizar temáticas predominantes (logística, calidad, etc.)
- Detectar idiomas más frecuentes y su distribución geográfica
- Medir el número y tipo de comunicaciones generadas (cliente, logística, proveedor)
- Estimar costes de respuesta manual vs automática con IA
- Facilitar decisiones estratégicas basadas en datos en tiempo real

### 📊 Funcionalidades principales

- **Dashboard interactivo** con métricas en tiempo real
- **Visualizaciones dinámicas** de datos por valoración, idioma y tipo de comunicación
- **Análisis de variables clave** de calidad (envíos, embalaje, tallas, etc.)
- **Generación automatizada** de informes PDF ejecutivos
- **Procesamiento multilingüe** de comentarios de clientes
- **Estimación de costes** asociados a cada tipo de comunicación

### 💻 Tecnologías utilizadas

- **Python** como lenguaje principal
- **Streamlit** para el desarrollo del dashboard interactivo
- **Pandas** para manipulación y análisis de datos
- **Plotly** para visualizaciones gráficas dinámicas
- **ReportLab** para generación de informes PDF profesionales
- **GitHub** para versionado y almacenamiento de datos
- Integración con **APIs de IA** (OpenAI y Google Gemini)

### 🚀 Instalación

1. Clone este repositorio:
   ```
   git clone https://github.com/AraceliFradejas/kelcets-dashboard.git
   cd kelcets-dashboard
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configure las variables de entorno para las APIs de IA (opcional):
   - Cree un archivo `.env` con las siguientes variables:
     ```
     OPENAI_API_KEY=su_clave_api_openai
     GOOGLE_API_KEY=su_clave_api_google
     ```

4. Ejecute la aplicación:
   ```
   streamlit run app.py
   ```

### 📁 Estructura del proyecto

- `app.py` - Aplicación principal de Streamlit
- `requirements.txt` - Dependencias del proyecto
- `data/` - Directorio con archivos de datos
  - `BD Comentarios KelceTS.txt` - Base de datos de comentarios
  - `Informe_Final_KelceTS.xlsx` - Dataset principal analizado
  - `KelceTS_logo.png` - Logo corporativo
  - `Reglas de calidad clientes KelceTS SL.xlsx` - Reglas de negocio

### 🧠 Impacto esperado

- Mayor conocimiento de incidencias recurrentes
- Optimización del proceso de atención al cliente
- Visión ejecutiva sobre el uso de IA en análisis multilingüe
- Apoyo a decisiones estratégicas con métricas visuales y automáticas

### 👩‍💻 Autora

**Araceli Fradejas Muñoz**  
Curso Desarrollador10X - Instituto de Inteligencia Artificial  
Abril 2025

---

## 🌟 Description (English)

This analytical dashboard was developed as the final project for the Desarrollador10X course at the Instituto de Inteligencia Artificial. The application is designed for the fictional company KelceTS S.L., a startup specialized in online shoe sales across Europe.

The dashboard provides Management and the CEO with an **analytical and strategic view** of customer comments in different languages and channels, enabling data-driven decision making.

### 🎯 Application Objectives

- Visualize the volume and evolution of received comments
- Analyze predominant topics (logistics, quality, etc.)
- Detect most frequent languages and their geographic distribution
- Measure the number and type of communications generated (customer, logistics, supplier)
- Estimate costs of manual vs. automated AI responses
- Facilitate strategic decisions based on real-time data

### 📊 Key Features

- **Interactive dashboard** with real-time metrics
- **Dynamic data visualizations** by rating, language, and communication type
- **Analysis of key quality variables** (shipping, packaging, sizes, etc.)
- **Automated generation** of executive PDF reports
- **Multilingual processing** of customer comments
- **Cost estimation** associated with each type of communication

### 💻 Technologies Used

- **Python** as the main language
- **Streamlit** for interactive dashboard development
- **Pandas** for data manipulation and analysis
- **Plotly** for dynamic graphical visualizations
- **ReportLab** for professional PDF report generation
- **GitHub** for versioning and data storage
- Integration with **AI APIs** (OpenAI and Google Gemini)

### 🚀 Installation

1. Clone this repository:
   ```
   git clone https://github.com/AraceliFradejas/kelcets-dashboard.git
   cd kelcets-dashboard
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables for AI APIs (optional):
   - Create a `.env` file with the following variables:
     ```
     OPENAI_API_KEY=your_openai_api_key
     GOOGLE_API_KEY=your_google_api_key
     ```

4. Run the application:
   ```
   streamlit run app.py
   ```

### 📁 Project Structure

- `app.py` - Main Streamlit application
- `requirements.txt` - Project dependencies
- `data/` - Directory with data files
  - `BD Comentarios KelceTS.txt` - Comments database
  - `Informe_Final_KelceTS.xlsx` - Main dataset analyzed
  - `KelceTS_logo.png` - Corporate logo
  - `Reglas de calidad clientes KelceTS SL.xlsx` - Business rules

### 🧠 Expected Impact

- Greater knowledge of recurring incidents
- Optimization of the customer service process
- Executive overview of AI use in multilingual analysis
- Support for strategic decisions with visual and automated metrics

### 👩‍💻 Author

**Araceli Fradejas Muñoz**  
Desarrollador10X Course - Instituto de Inteligencia Artificial  
April 2025