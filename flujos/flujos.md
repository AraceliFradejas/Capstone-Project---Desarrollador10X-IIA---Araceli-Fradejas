
# 📁 **Capstone Project Curso Desarrolador 10x de Instituto de Inteligencia Artificial - Flujos entregables**

Este documento describe los cuatro flujos operativos fundamentales del sistema desarrollado para KelceTS S.L. como parte del Capstone Project del curso Desarrollador 10X del Instituto de Inteligencia Artificial. Cada flujo corresponde a uno de los módulos implementados o al sistema completo, y está representado tanto en imagen como en código Mermaid.

El directorio `flujos/` contiene los siguientes elementos visuales:

---
## 🔹 0. Flujo General del Sistema Integrado (`Flujo_Completo0.png`)

Este diagrama resume la integración de los tres módulos y su funcionamiento conjunto como un ecosistema de IA para la atención al cliente.

**Componentes integrados:**
- El análisis (Módulo 1) alimenta a la interfaz del Call Center (Módulo 2).
- La interfaz genera comunicaciones y retroalimenta al dashboard (Módulo 3).
- El dashboard ofrece insights estratégicos que permiten ajustar los análisis futuros.

**Resumen del proceso:**
1. Comentarios → análisis automatizado (M1).
2. M1 → interfaz operativa para agentes (M2).
3. M2 → datos a visualizar por dirección (M3).
4. M3 → mejora continua del sistema (↩️ M1).

---

## 🔹 1. Flujo de Análisis Automatizado de Comentarios (`Flujo_AnalisisComentarios_Entregable1.png`)

Este flujo representa el funcionamiento del Módulo 1, que analiza los comentarios de clientes recibidos en múltiples idiomas, identifica variables clave y genera comunicaciones personalizadas.

**Objetivos del flujo:**
- Procesar automáticamente comentarios multilingües.
- Clasificarlos como positivos, negativos o neutros.
- Generar respuestas personalizadas y notificaciones internas.
- Exportar los resultados para análisis estratégico.

**Resumen del proceso:**
1. Carga y detección automática del idioma.
2. Traducción al español si es necesario.
3. Análisis con modelo generativo (GPT-4 o fallback a Gemini).
4. Clasificación de la valoración.
5. Generación de comunicaciones internas y externas.
6. Exportación de resultados a Excel y gráficos.

---

## 🔹 2. Flujo del Asistente de IA para el Call Center (`Flujo__AppGradioCallCenter_Entregable2.png`)

Este flujo representa el Módulo 2: una interfaz basada en Gradio diseñada para que agentes del Call Center puedan analizar comentarios de forma individual y obtener respuestas inmediatas.

**Funciones principales:**
- Entrada de comentarios reales o de ejemplo.
- Traducción automática desde 24 idiomas oficiales.
- Análisis en tiempo real con fallback entre modelos IA.
- Generación de respuestas en HTML para copiar/pegar.

**Resumen del proceso:**
1. Entrada del comentario (manual o ejemplo).
2. Detección de idioma y traducción si es necesario.
3. Análisis con OpenAI o Gemini.
4. Generación de respuesta personalizada.
5. Visualización clara y accesible.

---

## 🔹 3. Flujo del Dashboard Estratégico (`Flujo_AppStreamlitCEODashboard_Entregable3.png`)

Este flujo representa el Módulo 3: un panel directivo desarrollado en Streamlit para visualizar datos agregados del sistema.

**Funciones clave:**
- Mostrar KPIs clave como número de comentarios, idiomas, valoraciones y problemas detectados.
- Estimar el impacto económico de las incidencias.
- Permitir análisis por idioma, tipo de problema y otras variables.
- Exportar informes ejecutivos en PDF.

**Resumen del proceso:**
1. Recepción de los datos del análisis automatizado.
2. Cálculo de métricas y costes.
3. Visualización interactiva mediante Plotly.
4. Generación de informes ejecutivos.
5. Uso por parte de dirección para la toma de decisiones.

---

## 📂 Estructura del directorio `/flujos`

```
/flujos/
├── Flujo_AnalisisComentarios_Entregable1.png
├── Flujo__AppGradioCallCenter_Entregable2.png
├── Flujo_AppStreamlitCEODashboard_Entregable3.png
├── Flujo_Completo0.png
├── flujos.md  ← este archivo
```

Cada imagen del directorio corresponde a un entregable del proyecto y puede ser reutilizada en presentaciones, informes o documentación técnica.

---

**Autora:** Araceli Fradejas Muñoz  
**Proyecto:** KelceTS S.L. - Capstone Project Curso Desarrollador 10X - Instituto Inteligencia Artificial  
**Fecha:** Abril de 2025
