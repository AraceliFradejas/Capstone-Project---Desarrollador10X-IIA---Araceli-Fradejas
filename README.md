# 🚀 Capstone Project Curso Desarrolador 10x de Instituto de Inteligencia Artificial - Araceli Fradejas Muñoz - Abril 2025

*Análisis Automatizado de Comentarios de Clientes, App para agentes de Call Center y Dashboard Estratégico para CEO y ejecutivos de la startup ficticia "KELCE TS S.L."*  
**Curso:** Desarrollador 10X – Instituto de Inteligencia Artificial  
**Autora:** Araceli Fradejas Muñoz  
**Fecha:** Abril 2025  

---

## 📑 Tabla de Contenidos
- [Descripción General](#descripción-general)
- [Entregables](#entregables)
- [Documentación](#documentación)
- [Flujos de Trabajo](#flujos-de-trabajo)
- [Videos Demostrativos](#videos-demostrativos)
- [Instalación Rápida](#instalación-rápida)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Capturas](#capturas)
- [Roadmap](#roadmap)
- [Créditos](#créditos)
- [ENGLISH VERSION](#english-version)

---

## Descripción General
KelceTS S.L. es una *startup* ficticia que vende zapatillas online en Europa.  
Durante el proyecto se desarrolló una **suite de IA generativa** que automatiza el
análisis de comentarios multilingües y presenta la información tanto a agentes operativos
como a la dirección.

---

## Entregables
| Nº | Producto | Tecnologías | Descripción |
|----|----------|-------------|-------------|
| **1** | ⚙️ *Notebook* de Análisis y Exportación (`Capstone_Project.ipynb`) | Python · OpenAI · Gemini · Pandas · Plotly | Analiza comentarios, aplica reglas de negocio y genera `Informe_Final_KelceTS.xlsx` |
| **2** | 💬 Asistente IA para Call‑Center (`Gradio_CallCenter_KelceTS.ipynb`) | Python · Gradio · LangDetect | Interface web para agentes que detecta idioma, traduce, analiza y genera comunicaciones |
| **3** | 📊 Dashboard Dirección (`app.py`) | Python · Streamlit · Plotly · ReportLab | Visualiza KPIs clave, costes y genera informes PDF ejecutivos |

---

## Documentación
El proyecto cuenta con documentación detallada disponible en el directorio `/memoria/`:

| Documento | Descripción |
|-----------|-------------|
| 📄 [Memoria Completa (ES)](./memoria/Memoria_Completa_CapstoneProject_Desarrollador10x_IIA_AraceliFradejasMuñoz_Abril2025.md) | Memoria técnica completa del proyecto en español |
| 📄 [Full Report (EN)](./memoria/Full_Report_CapstoneProject_Developer10x_IIA_AraceliFradejasMuñoz_April2025_EnglishVersion.md) | Versión en inglés del informe técnico completo |

---

## Flujos de Trabajo
En el directorio `/flujos/` se encuentran los diagramas que representan el funcionamiento de cada componente:

| Diagrama | Descripción |
|----------|-------------|
| 🔄 [Flujo Completo](./flujos/Flujo_Completo0.png) | Visión general del sistema integrado |
| 🔄 [Análisis de Comentarios](./flujos/Flujo_AnalisisComentarios_Entregable1.png) | Procesamiento del módulo 1 para análisis automático |
| 🔄 [App Call Center](./flujos/Flujo__AppGradioCallCenter_Entregable2.png) | Funcionamiento de la interfaz Gradio para agentes |
| 🔄 [Dashboard CEO](./flujos/Flujo_AppStreamlitCEODashboard_Entregable3.png) | Estructura del panel de visualización para dirección |

Para una descripción detallada de cada flujo, consultar el archivo [flujos.md](./flujos/flujos.md).

---

## Videos Demostrativos
El directorio `/videos demos/` contiene grabaciones del proyecto en funcionamiento:

### Entregable 1 - Análisis de Comentarios
📹 [Ver demo del análisis automático](./videos%20demos/Entregable1_crompress.mp4)

### Entregable 2 - App Call Center con Gradio
📹 [Ver demo general](./videos%20demos/Entregable2_crompress.mp4)  
📹 [Ver demo detallada de Gradio](./videos%20demos/Entregable2gradio_crompress.mp4)

### Entregable 3 - Dashboard Ejecutivo
📹 [Ver demo general](./videos%20demos/Entregable3_crompress.mp4)  
📹 [Ver en PC](./videos%20demos/Entregable3streamlitpc_crompress.mp4)  
📹 [Ver en iPad Air 13](./videos%20demos/Entregable3streamlit_IpadAir13_compress.mp4)  
📹 [Ver en iPhone 16 Pro Max](./videos%20demos/Entregable3streamlit_Iphone16promax_compress.mp4)

Para más información sobre los videos, consultar [videos_demos.md](./videos%20demos/videos_demos.md).

---

## Instalación Rápida
```bash
git clone https://github.com/AraceliFradejas/kelcets-dashboard.git
cd kelcets-dashboard
pip install -r requirements.txt
# Configurar claves (opcional)
echo "OPENAI_API_KEY=TU_CLAVE" >> .env
echo "GOOGLE_API_KEY=TU_CLAVE" >> .env
```

---

## Cómo Ejecutar
| Entregable | Comando / Acción |
|------------|------------------|
| **E1** Notebook | Abrir en Colab ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) y seguir celdas |
| **E2** Gradio | Abrir `Gradio_CallCenter_KelceTS.ipynb` en Colab y ejecutar |
| **E3** Dashboard | `streamlit run app.py` |

---

## Capturas
<p align="center">
  <img src="data/gradio_preview.png" width="45%" />
  <img src="data/dashboard_preview.png" width="45%" />
</p>

---

## Roadmap
- [ ] Clasificación emocional y tono  
- [ ] Soporte multimodal (imágenes, vídeos)  
- [ ] API REST para integración con CRM  
- [ ] Despliegue en Streamlit Cloud / Hugging Face  

---

## 👩‍💻 Créditos
Creado por **Araceli Fradejas Muñoz**   
Proyecto desarrollado por **Araceli Fradejas Muñoz** como parte del I Curso Intensivo de Desarrollador 10x con IA – Instituto de Inteligencia Artificial*.  
Contacto: [LinkedIn](https://www.linkedin.com/in/araceli-fradejas-munoz-transformaciondigital/)
Abril 2025

---

# ENGLISH VERSION

## Overview
KelceTS S.L. is a fictional online sneaker company.  
This repository contains a **Generative AI solution** that automates multilingual
feedback analysis and provides both operational and executive interfaces.

## Deliverables
| # | Product | Tech | Description |
|---|---------|------|-------------|
| **1** | ⚙️ Analysis Notebook (`Capstone_Project.ipynb`) | Python · OpenAI · Gemini · Pandas · Plotly | Processes comments, applies business rules and exports `Informe_Final_KelceTS.xlsx` |
| **2** | 💬 AI Assistant for Call Center (`Gradio_CallCenter_KelceTS.ipynb`) | Python · Gradio · LangDetect | Web UI for agents: language detection, translation, analysis and message generation |
| **3** | 📊 Executive Dashboard (`app.py`) | Python · Streamlit · Plotly · ReportLab | Displays key KPIs, cost estimates and generates executive PDF reports |

## Documentation
The project includes detailed documentation available in the `/memoria/` directory:

| Document | Description |
|----------|-------------|
| 📄 [Complete Report (ES)](./memoria/Memoria_Completa_CapstoneProject_Desarrollador10x_IIA_AraceliFradejasMuñoz_Abril2025.md) | Complete technical report in Spanish |
| 📄 [Full Report (EN)](./memoria/Full_Report_CapstoneProject_Developer10x_IIA_AraceliFradejasMuñoz_April2025_EnglishVersion.md) | Full technical report in English |

## Workflow Diagrams
The `/flujos/` directory contains diagrams representing the operation of each component:

| Diagram | Description |
|---------|-------------|
| 🔄 [Complete Workflow](./flujos/Flujo_Completo0.png) | General overview of the integrated system |
| 🔄 [Comments Analysis](./flujos/Flujo_AnalisisComentarios_Entregable1.png) | Processing flow of module 1 for automatic analysis |
| 🔄 [Call Center App](./flujos/Flujo__AppGradioCallCenter_Entregable2.png) | Functioning of the Gradio interface for agents |
| 🔄 [CEO Dashboard](./flujos/Flujo_AppStreamlitCEODashboard_Entregable3.png) | Structure of the visualization panel for management |

For a detailed description of each flow, see the [flujos.md](./flujos/flujos.md) file.

## Demo Videos
The `/videos demos/` directory contains recordings of the project in operation:

### Deliverable 1 - Comment Analysis
📹 [Watch automated analysis demo](./videos%20demos/Entregable1_crompress.mp4)

### Deliverable 2 - Gradio Call Center App
📹 [Watch general demo](./videos%20demos/Entregable2_crompress.mp4)  
📹 [Watch detailed Gradio demo](./videos%20demos/Entregable2gradio_crompress.mp4)

### Deliverable 3 - Executive Dashboard
📹 [Watch general demo](./videos%20demos/Entregable3_crompress.mp4)  
📹 [Watch on PC](./videos%20demos/Entregable3streamlitpc_crompress.mp4)  
📹 [Watch on iPad Air 13](./videos%20demos/Entregable3streamlit_IpadAir13_compress.mp4)  
📹 [Watch on iPhone 16 Pro Max](./videos%20demos/Entregable3streamlit_Iphone16promax_compress.mp4)

For more information about the videos, see [videos_demos.md](./videos%20demos/videos_demos.md).

## Quick Start
```bash
git clone https://github.com/AraceliFradejas/kelcets-dashboard.git
cd kelcets-dashboard
pip install -r requirements.txt
# API keys (optional)
echo "OPENAI_API_KEY=YOUR_KEY" >> .env
echo "GOOGLE_API_KEY=YOUR_KEY" >> .env
```

## Run
| Deliverable | Command |
|-------------|---------|
| **D1** Notebook | Open in Colab ![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg) |
| **D2** Gradio | Open `Gradio_CallCenter_KelceTS.ipynb` in Colab |
| **D3** Dashboard | `streamlit run app.py` |

## Screenshots
See `/data` folder for previews.

## Roadmap
- Emotion & tone classification  
- Multimodal support  
- REST API for CRM integration  
- Deployment to Streamlit Cloud / Hugging Face  

### 👩‍💻 Author
Created by **Araceli Fradejas Muñoz**   
Desarrollador10X Course - Instituto de Inteligencia Artificial  
Contact: [LinkedIn](https://www.linkedin.com/in/araceli-fradejas-munoz-transformaciondigital/)
April 2025
