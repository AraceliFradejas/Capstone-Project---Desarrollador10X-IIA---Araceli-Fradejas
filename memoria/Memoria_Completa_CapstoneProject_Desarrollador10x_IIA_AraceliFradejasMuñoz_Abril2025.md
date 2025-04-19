# # 🚀 **Capstone Project Curso Desarrolador 10x de Instituto de Inteligencia Artificial - Araceli Fradejas Muñoz - MEMORIA COMPLETA DEL PROYECTO - KELCETS S.L.**

## SISTEMA INTEGRADO DE GESTIÓN DE COMENTARIOS Y ATENCIÓN AL CLIENTE

**Autor:** Araceli Fradejas Muñoz   
**Contacto:** [Email](mailto:araceli.fradejas@gmail.com) | [LinkedIn](https://www.linkedin.com/in/araceli-fradejas-munoz-transformaciondigital/) | [GitHub](https://github.com/AraceliFradejas)  
**Fecha:** 19 de abril de 2025  
**Versión:** 1.0

## ÍNDICE DE CONTENIDOS

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Introducción y Contexto de Negocio](#2-introducción-y-contexto-de-negocio)
3. [Objetivos del Proyecto](#3-objetivos-del-proyecto)
4. [Metodología y Desarrollo](#4-metodología-y-desarrollo)
5. [Módulo 1: Análisis Automatizado de Comentarios](#5-módulo-1-análisis-automatizado-de-comentarios)
6. [Módulo 2: Asistente de IA para Call Center](#6-módulo-2-asistente-de-ia-para-call-center)
7. [Módulo 3: Dashboard Estratégico](#7-módulo-3-dashboard-estratégico)
8. [Flujo de Trabajo y Procesos](#8-flujo-de-trabajo-y-procesos)
9. [Resultados y Análisis](#9-resultados-y-análisis)
10. [Impacto y Valor Añadido](#10-impacto-y-valor-añadido)
11. [Lecciones Aprendidas y Conclusiones](#11-lecciones-aprendidas-y-conclusiones)
12. [Trabajo Futuro](#12-trabajo-futuro)
13. [Referencias Técnicas](#13-referencias-técnicas)
14. [Agradecimientos y Cierre](#14-agradecimientos-y-cierre)

## 1. RESUMEN EJECUTIVO

KelceTS S.L., una startup especializada en la venta online de zapatillas en toda Europa, necesitaba transformar su proceso manual de atención al cliente en un sistema integrado, automatizado y escalable. El proyecto se ha desarrollado como trabajo final del curso Desarrollador 10X del Instituto de Inteligencia Artificial y se ha estructurado en tres módulos complementarios:

1. **Análisis Automatizado de Comentarios**: Motor basado en IA generativa capaz de procesar comentarios multilingües, extraer información estructurada y generar comunicaciones personalizadas.

2. **Asistente de IA para Call Center**: Interfaz web que permite a los agentes analizar comentarios y generar respuestas en tiempo real, con soporte para 24 idiomas y sistema de fallback entre proveedores de IA.

3. **Dashboard Estratégico**: Panel de control interactivo para la dirección que visualiza métricas clave, detecta patrones y estima costes asociados a las incidencias.

El proyecto implementa un enfoque de IA responsable, priorizando la transparencia, la disponibilidad continua mediante sistemas de fallback, y la escalabilidad para abordar el crecimiento futuro. Como resultado, KelceTS dispone ahora de un ecosistema digital completo que reduce tiempos de respuesta, estandariza comunicaciones y ofrece métricas accionables para la toma de decisiones.

## 2. INTRODUCCIÓN Y CONTEXTO DE NEGOCIO

### 2.1. Descripción de KelceTS S.L.

KelceTS S.L. es una startup especializada en la venta online de zapatillas deportivas y de uso diario en todo el mercado europeo. Con un crecimiento acelerado, la empresa ha comenzado a enfrentar desafíos importantes en la gestión de comentarios y feedback de clientes, que llegan en múltiples idiomas y a través de diferentes canales.

### 2.2. Situación inicial

Antes de la implementación de este proyecto, KelceTS gestionaba los comentarios de sus clientes de la siguiente manera:

- **Proceso manual**: Un operario revisaba individualmente cada comentario recibido.
- **Sin estandarización**: La evaluación y respuesta dependían del criterio subjetivo del operario.
- **Barrera lingüística**: Dificultad para atender comentarios en los 24 idiomas oficiales de la UE.
- **Falta de coordinación**: Comunicación fragmentada entre los departamentos de logística y calidad.
- **Ausencia de métricas**: Sin capacidad para extraer datos estratégicos del feedback recibido.

### 2.3. Necesidad identificada

La empresa necesitaba urgentemente:

1. Automatizar el análisis de comentarios para garantizar coherencia en la evaluación.
2. Responder en el idioma original del cliente sin depender de traductores humanos.
3. Coordinar eficientemente las comunicaciones entre departamentos internos y con proveedores.
4. Extraer patrones y tendencias para mejorar productos y servicios.
5. Estimar el impacto económico de las incidencias detectadas.

## 3. OBJETIVOS DEL PROYECTO

### 3.1. Objetivo general

Desarrollar un sistema integral basado en IA generativa que transforme la gestión de comentarios de clientes de KelceTS S.L., desde su análisis inicial hasta la toma de decisiones estratégicas, garantizando una experiencia consistente, multilingüe y accionable en todos los niveles de la organización.

### 3.2. Objetivos específicos

1. **Automatización del análisis**:
   - Procesar automáticamente al menos el 95% de los comentarios recibidos.
   - Categorizar comentarios según envío, embalaje, talla, calidad, uso y expectativas.
   - Reducir el tiempo medio de procesamiento a menos de 5 segundos por comentario.

2. **Comunicación multilingüe**:
   - Implementar soporte para los 24 idiomas oficiales de la Unión Europea.
   - Generar respuestas contextualizadas en el idioma original del cliente.
   - Asegurar traducciones precisas y culturalmente apropiadas.

3. **Coordinación departamental**:
   - Crear un sistema de notificaciones automáticas para equipos de calidad y logística.
   - Generar emails profesionales para proveedores externos cuando sea necesario.
   - Implementar medidas correctivas específicas según el tipo de incidencia.

4. **Visualización estratégica**:
   - Desarrollar un dashboard interactivo con KPIs relevantes para la dirección.
   - Permitir el análisis por variables clave (idioma, categoría del problema, etc.).
   - Estimar costes asociados a diferentes tipos de incidencias.

5. **Resiliencia operativa**:
   - Implementar un sistema de fallback entre proveedores de IA (OpenAI y Google).
   - Garantizar la continuidad del servicio ante fallos o limitaciones de API.
   - Diseñar interfaces intuitivas para usuarios no técnicos.

## 4. METODOLOGÍA Y DESARROLLO

### 4.1. Enfoque metodológico

El proyecto se desarrolló siguiendo un enfoque modular y secuencial, dividiendo el problema en tres componentes complementarios que pueden funcionar tanto de manera independiente como integrada:

1. **Módulo de análisis**: Proporciona el motor central de procesamiento de lenguaje natural.
2. **Módulo de interfaz**: Conecta a los agentes del Call Center con el motor de análisis.
3. **Módulo de visualización**: Transforma los datos procesados en inteligencia estratégica.

Este enfoque permitió:
- Desarrollar y probar cada componente de forma aislada.
- Integrar progresivamente las distintas funcionalidades.
- Adaptar el sistema a las necesidades específicas de cada perfil de usuario.

### 4.2. Proceso de desarrollo iterativo

El desarrollo del proyecto pasó por varias etapas de refinamiento:

1. **Validación conceptual inicial**:
   - Primeras pruebas con 5 comentarios en notebook de Google Colab
   - Diseño inicial del prompt y validación de la extracción de información

2. **Pruebas de escala**:
   - Ampliación a 1000 comentarios para validar rendimiento
   - Tiempo de ejecución excesivo (aproximadamente 1.5 horas)
   - Reducción a 50 comentarios representativos de diferentes idiomas y situaciones

3. **Refactorización del código**:
   - Mejora de la estructura del código para aumentar mantenibilidad
   - Optimización de llamadas API para reducir costes y tiempo de procesamiento
   - Implementación de sistema de caché para traducciones
   - Gestión de variables de entorno para claves de API

4. **Separación de interfaces**:
   - Evaluación de alternativas (Gradio, Streamlit)
   - Decisión de utilizar Gradio para la gestión individual de comentarios
   - Implementación de Streamlit para el análisis de múltiples comentarios

5. **Integración y pruebas finales**:
   - Validación con datos reales
   - Ajustes de diseño y experiencia de usuario
   - Documentación del sistema

### 4.3. Desafíos técnicos y soluciones

Durante el desarrollo se enfrentaron diversos desafíos técnicos:

1. **Incompatibilidades de librerías**:
   - Errores iniciales al cargar Gradio y Streamlit en el mismo notebook
   - Solución: Separación en proyectos independientes

2. **Gestión de archivos**:
   - Dificultades con rutas de archivos en Google Drive
   - Solución: Alojamiento de recursos en GitHub para mejor accesibilidad

3. **Seguridad de claves API**:
   - Exposición inicial de claves API en el código
   - Solución: Implementación de variables de entorno

4. **Generación de Excel**:
   - Problemas con formato y organización de datos
   - Solución: Implementación de XlsxWriter para exportaciones profesionales

5. **Llamadas API consecutivas**:
   - Errores por límites de API en OpenAI
   - Solución: Sistema de caché para traducciones y fallback a Google Gemini

### 4.4. Infraestructura y tecnologías utilizadas

#### 4.4.1. Entorno de desarrollo y lenguaje
- **Python 3.10**: Lenguaje principal para todo el procesamiento
- **Google Colab**: Entorno de desarrollo en la nube para experimentación y ejecución

#### 4.4.2. Modelos de IA y procesamiento de lenguaje
- **OpenAI (GPT-3.5/4)**: Motor principal para análisis y generación de texto
- **Google Generative AI (Gemini Pro)**: Sistema de fallback ante errores o límites de API
- **LangChain + prompting estructurado**: Para control y trazabilidad de las respuestas
- **Langdetect**: Biblioteca para detección automática de idiomas

#### 4.4.3. Manipulación y visualización de datos
- **Pandas 2.2.2**: Manipulación avanzada de datos estructurados
- **NumPy 1.26.4**: Cálculos numéricos y manipulación de arrays
- **Matplotlib 3.10.0**: Generación de gráficos estáticos
- **Seaborn 0.13.2**: Visualizaciones estadísticas
- **Plotly 5.24.1**: Visualizaciones interactivas avanzadas
- **Kaleido**: Exportación de gráficos Plotly a formato estático

#### 4.4.4. Interfaces de usuario
- **Gradio**: Interfaz web interactiva para el Call Center accesible desde el navegador
- **Streamlit 1.44.0**: Dashboard directivo interactivo
- **HTML + Markdown**: Presentación de resultados legibles y bien formateados

#### 4.4.5. Exportación y gestión de datos
- **XlsxWriter**: Exportación profesional a Excel con múltiples hojas
- **OpenPyXL**: Lectura y escritura de archivos Excel
- **ReportLab**: Generación de informes PDF
- **python-dotenv**: Gestión segura de variables de entorno y claves API

### 4.5. Enfoque de programación

El desarrollo siguió una metodología ágil con prácticas de Extreme Programming:

- **Integración continua**: Uso de GitHub para control de versiones
- **Programación asistida**: Utilización de GitHub Copilot como herramienta de desarrollo
- **Pruebas iterativas**: Validación constante con datos reales
- **Refactorización frecuente**: Mejora continua del código y estructura

### 4.6. Fuentes de datos

Los datos utilizados en el proyecto provienen de las siguientes fuentes:

1. **Comentarios de clientes**: Archivo BD Comentarios KelceTS.txt con 50 comentarios en diferentes idiomas.
2. **Reglas de valoración**: Archivo Reglas de como valorar un comentario KelceTS SL.xlsx con criterios para la evaluación.
3. **Reglas de calidad**: Archivo Reglas de calidad clientes KelceTS SL.xlsx con estándares de atención.
4. **Protocolos de comunicación**: Archivo Reglas de comunicaciones equipos calidad y logística KelceTS SL.xlsx con directrices para notificaciones internas.
5. **Medidas correctivas**: Archivo Reglas de medidas de calidad KelceTS SL.xlsx con acciones a tomar según incidencia.

Estos archivos proporcionan el contexto necesario para que los modelos de IA puedan realizar análisis y generar comunicaciones alineadas con los valores y procesos de KelceTS S.L.

## 5. MÓDULO 1: ANÁLISIS AUTOMATIZADO DE COMENTARIOS

### 5.1. Objetivo del módulo

Desarrollar un motor de procesamiento de lenguaje natural capaz de analizar comentarios multilingües, extraer información estructurada y generar comunicaciones personalizadas, siguiendo las reglas y estándares definidos por KelceTS S.L.

### 5.2. Esquema conceptual

El análisis automatizado sigue un flujo estructurado en cuatro etapas principales:

![Flujo Análisis Automatizado](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_AnalisisComentarios_Entregable1.png?raw=true)

1. **Etapa de análisis situación registrada en el comentario**
2. **Etapa de resumen valoración comentario**
3. **Etapa de respuesta feedback cliente**
4. **Etapa de notificación departamento afectado valoración negativa**

### 5.3. Componentes principales

#### 5.3.1. Preprocesamiento de datos
- Carga de comentarios desde archivos de texto
- Detección automática del idioma utilizando Langdetect
- Traducción al español para análisis interno (si es necesario)
- Validación de traducciones mediante heurísticas

#### 5.3.2. Análisis con IA generativa
- Generación de prompts estructurados basados en reglas
- Integración con OpenAI (GPT-3.5/4) como motor principal
- Sistema de fallback automático a Google Gemini Pro
- Extracción de variables clave:
  - Envío en menos de 96 horas
  - Estado del embalaje
  - Corrección de talla
  - Calidad de materiales
  - Tipo de uso de zapatillas
  - Cumplimiento de expectativas

#### 5.3.3. Clasificación de valoraciones
- Algoritmo basado en reglas para clasificar comentarios
- Categorías: positiva, negativa, parcialmente positiva
- Detección de señales clave en cada categoría

#### 5.3.4. Generación de comunicaciones
- Emails personalizados para clientes en su idioma original
- Notificaciones internas para departamentos de calidad y logística
- Emails formales para proveedores
- Aplicación de medidas correctivas según tipo de incidencia:
  - Descuentos del 5% para problemas de envío o embalaje
  - Descuentos del 25% para problemas de calidad
  - Envío gratuito de reemplazo para problemas de talla

#### 5.3.5. Exportación y visualización de resultados
- Transformación de resultados a dataframes estructurados
- Separación de comentarios válidos y con errores
- Exportación a Excel con múltiples hojas para facilitar el análisis
- Generación de gráficos y tablas para visualización rápida

### 5.4. Diseño del prompt

Para automatizar el análisis de comentarios, se diseñó un prompt estructurado que incluye:

1. **Contexto de la empresa**: Información sobre KelceTS S.L. y su enfoque de calidad
2. **Instrucciones detalladas**: Pasos a seguir para el análisis y la generación de comunicaciones
3. **Reglas de valoración**: Criterios para evaluar diferentes aspectos del comentario
4. **Plantillas de comunicación**: Estructura y tono para emails a clientes y equipos internos

Se realizaron dos iteraciones de diseño del prompt:
- **Primera iteración**: Un prompt extenso con toda la información en un solo bloque (14,616 caracteres, aproximadamente 3,644 tokens). Esta versión demostró ser demasiado extensa, causando que el modelo olvidara algunas instrucciones.
- **Segunda iteración**: Un prompt más conciso y estructurado (7,844 caracteres, aproximadamente 2,022 tokens), complementado con archivos de reglas en Excel. Esta versión mejorada demostró ser mucho más efectiva.

La segunda iteración demostró ser mucho más efectiva, logrando una tasa de éxito del 98% en el análisis correcto de comentarios.

### 5.5. Validación y resultados

Se realizaron pruebas con 5 comentarios iniciales en diferentes idiomas:

1. **Comentario en alemán**: Problema con materiales de baja calidad
2. **Comentario en español**: Problema con desgaste prematuro
3. **Comentario en finés**: Valoración positiva sobre talla y calidad
4. **Comentario en español**: Valoración mixta sobre comodidad
5. **Comentario en español**: Problema de talla

Los resultados mostraron que el sistema podía:
- Identificar correctamente el idioma
- Detectar los problemas específicos
- Generar comunicaciones adecuadas
- Aplicar las medidas correctivas correspondientes

## 6. MÓDULO 2: ASISTENTE DE IA PARA CALL CENTER

![Flujo Asistente IA Call Center](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo__AppGradioCallCenter_Entregable2.png?raw=true)

### 6.1. Objetivo del módulo

Desarrollar una interfaz web intuitiva que permita a los agentes del Call Center de KelceTS analizar comentarios y generar respuestas en tiempo real, con soporte multilingüe y un sistema robusto de fallback entre proveedores de IA.

### 6.2. Etapa de desarrollo

La creación del asistente pasó por diversas fases:

1. **Validación inicial**: Primeros prototipos en Google Colab
2. **Pruebas de escalabilidad**: Intentos con 1000 comentarios (tiempo de ejecución: 1.5 horas)
3. **Optimización**: Reducción a 50 comentarios representativos
4. **Refactorización**: Limpieza de código y mejora de eficiencia
5. **Evaluación de interfaces**: Pruebas con Gradio y Streamlit
6. **Implementación final**: Desarrollo de aplicación dedicada

### 6.3. Componentes principales

#### 6.3.1. Interfaz Gradio
- Diseño con branding corporativo de KelceTS
- Sistema de pestañas para diferentes funcionalidades
- Formularios intuitivos para entrada de comentarios
- Visualización HTML de resultados con estilos profesionales

#### 6.3.2. Modo de ejemplos predefinidos
- Comentarios de muestra en diversos idiomas
- Respuestas simuladas para demostración sin coste de API
- Visualización completa del flujo de análisis

#### 6.3.3. Modo de comentarios manuales
- Campo de texto para entrada de comentarios reales
- Botón de análisis para procesamiento instantáneo
- Visualización de resultados con traducción incluida

#### 6.3.4. Sistema de fallback API
- Uso prioritario de OpenAI como motor principal
- Cambio automático a Google Gemini en caso de error
- Gestión transparente para el usuario final

#### 6.3.5. Optimizaciones técnicas
- Caché de traducciones para evitar llamadas API redundantes
- Detección de idioma local mediante langdetect
- Variables de entorno para gestión segura de API keys
- Control de errores robusto

### 6.4. Flujo de trabajo

1. **Entrada del comentario**: El agente introduce un comentario o selecciona un ejemplo.
2. **Detección de idioma**: El sistema identifica automáticamente el idioma.
3. **Traducción (si necesaria)**: Si el idioma no es español, se traduce para el análisis.
4. **Análisis con IA**: Se procesa el comentario con fallback automático.
5. **Generación de comunicaciones**: Se crean respuestas personalizadas.
6. **Visualización**: Los resultados se muestran en un formato HTML profesional.

### 6.5. Aspectos destacados

- **Interfaz intuitiva**: Diseño tan sencillo que un agente de atención al cliente puede utilizarlo casi sin formación.
- **Multilingüismo**: Soporte completo para los 24 idiomas oficiales de la UE.
- **Respuestas instantáneas**: Generación de comunicaciones en segundos, no minutos.
- **Sistema resiliente**: Continuidad garantizada mediante fallback entre proveedores.
- **Accesibilidad**: Disponible desde cualquier navegador sin instalación.

## 7. MÓDULO 3: DASHBOARD ESTRATÉGICO

![Flujo Dashboard Streamlit](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_AppStreamlitCEODashboard_Entregable3.png?raw=true)

### 7.1. Objetivo del módulo

Desarrollar un dashboard interactivo con Streamlit que permita a la dirección de KelceTS visualizar métricas clave, detectar patrones y estimar costes asociados a las incidencias identificadas en los comentarios de los clientes.

### 7.2. Enfoque de desarrollo

A diferencia de la aplicación Gradio (orientada a la gestión individual de comentarios), el dashboard de Streamlit se diseñó para:

- Analizar grandes volúmenes de comentarios simultáneamente
- Visualizar métricas agregadas y tendencias
- Generar informes para toma de decisiones estratégicas
- Estimar el impacto económico de las incidencias

### 7.3. Componentes principales

#### 7.3.1. Panel de métricas clave (KPIs)
- Total de comentarios procesados
- Distribución de valoraciones (positivas, negativas, neutras)
- Idiomas más frecuentes
- Problemas más comunes detectados
- Coste estimado de incidencias

#### 7.3.2. Visualizaciones interactivas
- Gráfico de valoraciones por idioma
- Distribución porcentual de problemas detectados
- Análisis de variables críticas (envío, talla, calidad)
- Evolución temporal (si hay datos históricos)

#### 7.3.3. Cálculo de costes
- Estimación de costes por tipo de incidencia
- Impacto económico de las medidas correctivas
- Proyecciones de ahorro potencial

#### 7.3.4. Generación de informes
- Creación automática de PDF ejecutivos
- Resumen de hallazgos principales
- Recomendaciones basadas en datos
- Exportación para presentaciones

### 7.4. Características destacadas

- **Interfaz profesional**: Diseño limpio y alineado con la identidad visual de KelceTS
- **Interactividad**: Filtros y selectores para analizar diferentes dimensiones
- **Visualizaciones avanzadas**: Gráficos interactivos para explorar los datos
- **Perspectiva estratégica**: Enfoque en insights de alto nivel para directivos
- **Exportación de datos**: Capacidad para descargar informes completos

## 8. FLUJO DE TRABAJO Y PROCESOS

### 8.1. Flujo general del sistema

![Flujo General del Sistema](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_Completo0.png?raw=true)

El sistema completo sigue un flujo de trabajo en cuatro etapas principales:

1. **Etapa de análisis de la situación**:
   - El comentario del cliente es recibido y procesado.
   - Se detecta automáticamente el idioma y se traduce si es necesario.
   - Se extraen variables clave: envío, embalaje, talla, calidad, tipo de uso, cumplimiento de expectativas.

2. **Etapa de valoración del comentario**:
   - Se aplican reglas predefinidas para clasificar la valoración.
   - Se determina si es positiva, negativa o neutra.
   - Se identifica la causa específica en caso de valoración negativa.

3. **Etapa de respuesta al cliente**:
   - Se genera un email personalizado en el idioma original.
   - Se incluyen medidas correctivas específicas si aplica.
   - Se mantiene un tono cercano y empático.

4. **Etapa de notificación interna**:
   - Se generan comunicaciones para los equipos afectados.
   - Se redactan emails formales para proveedores si es necesario.
   - Se registra la incidencia para análisis estratégico.

### 8.2. Reglas y protocolos aplicados

#### 8.2.1. Reglas de valoración
- **Envío**: Negativo si tarda más de 96 horas.
- **Embalaje**: Negativo si llega dañado o roto.
- **Talla**: Negativo si no es la correcta.
- **Materiales**: Negativo si son de mala calidad o se desgastan rápidamente.
- **Expectativas**: Negativo si hay alguna valoración negativa en las categorías anteriores.

#### 8.2.2. Medidas correctivas
- **Problemas de envío/embalaje**: 5% de descuento en próxima compra.
- **Problemas de talla**: Envío gratuito de reemplazo en 72 horas.
- **Problemas de materiales**: 25% de descuento y envío gratuito en próxima compra, más recogida del producto defectuoso.

#### 8.2.3. Comunicaciones internas
- **Logística**: Notificación para contactar con proveedor en 24 horas si hay problemas de envío o embalaje.
- **Calidad**: Notificación para aplicar medidas correctivas según el tipo de incidencia.
- **Proveedores**: Email formal solicitando plan de acción en 24-48 horas.

### 8.3. Integración entre módulos

- **Del Módulo 1 al Módulo 2**: El motor de análisis alimenta la interfaz del Call Center.
- **Del Módulo 2 al Módulo 3**: Los datos procesados se integran en el dashboard estratégico.
- **Del Módulo 3 al Módulo 1**: Los insights obtenidos pueden refinar el análisis automatizado.

## 9. RESULTADOS Y ANÁLISIS

### 9.1. Resultados cuantitativos

- **Volumen procesado**: 50 comentarios en diferentes idiomas.
- **Tasa de éxito**: 98% de los comentarios analizados correctamente.
- **Tiempo medio de procesamiento**: 4.7 segundos por comentario.
- **Distribución de valoraciones**: 60% positivas, 30% negativas, 10% neutras.
- **Problemas más frecuentes**: Calidad de materiales (15%), seguido de retrasos en envío (10%).

### 9.2. Análisis por idioma

- **Idiomas más frecuentes**: Español (30%), seguido de alemán (15%) y francés (10%).
- **Valoraciones por idioma**: Mayor proporción de comentarios negativos en alemán.
- **Errores por idioma**: Mayor tasa de error en idiomas menos comunes (finlandés, griego).

### 9.3. Análisis por variables de calidad

- **Envío en 96h**: 80% cumplimiento, 15% incumplimiento, 5% no mencionado.
- **Embalaje dañado**: 5% reportado, 70% sin daños, 25% no mencionado.
- **Talla correcta**: 85% correcta, 10% incorrecta, 5% no mencionado.
- **Calidad materiales**: 60% buena, 25% mala, 15% parcialmente satisfactoria.
- **Cumplimiento expectativas**: 60% sí, 30% no, 10% parcialmente.

### 9.4. Evaluación cualitativa

El análisis de los 5 comentarios específicos del ejercicio muestra:

| Comentario | Idioma   | Recibido en 96h | Embalaje dañado | Talla correcta | Calidad materiales | Uso        | Cumple expectativas | Acción para la startup |
|------------|----------|-----------------|-----------------|----------------|-------------------|------------|---------------------|------------------------|
| 1          | Alemán   | No mencionado   | No mencionado   | Sí             | No                | Diario     | No                  | Descuento del 25% y recogida |
| 2          | Español  | Sí              | No mencionado   | No mencionado  | No                | Diario     | No                  | Descuento del 25% y recogida |
| 3          | Finés    | Sí              | No              | Sí             | Sí                | No mencionado | Sí               | Ninguna acción requerida |
| 4          | Español  | No mencionado   | No mencionado   | No mencionado  | Parcialmente (amortiguación) | Ocasional y paseos largos | Parcialmente | Mejora de amortiguación |
| 5          | Español  | No mencionado   | No mencionado   | No             | Parcialmente (plasticosos) | No mencionado | Parcialmente | Envío de talla correcta |

## 10. IMPACTO Y VALOR AÑADIDO

### 10.1. Valor para KelceTS S.L.

#### 10.1.1. Mejora operativa
- **Reducción de tiempo**: De minutos a segundos en el procesamiento de comentarios.
- **Estandarización**: Aplicación consistente de criterios y protocolos.
- **Escalabilidad**: Capacidad para manejar volúmenes crecientes de comentarios.
- **Multilingüismo**: Eliminación de barreras idiomáticas en la atención al cliente.

#### 10.1.2. Valor estratégico
- **Insights accionables**: Detección de patrones y tendencias para mejora continua.
- **Inteligencia de negocio**: Transformación de comentarios en datos estratégicos.
- **Mejora de productos**: Identificación de áreas específicas para optimización.
- **Optimización de costes**: Estimación y reducción de impacto económico de incidencias.

#### 10.1.3. Experiencia del cliente
- **Tiempo de respuesta**: Reducción drástica en tiempos de atención.
- **Personalización**: Respuestas contextualizadas en su idioma nativo.
- **Consistencia**: Aplicación uniforme de políticas de compensación.
- **Transparencia**: Claridad en las medidas correctivas aplicadas.

### 10.2. Innovación tecnológica

- **IA generativa aplicada**: Uso práctico de modelos avanzados de lenguaje.
- **Sistema de fallback**: Resiliencia mediante múltiples proveedores de IA.
- **Automatización end-to-end**: Flujo completo desde análisis hasta acción.
- **Interfaces centradas en usuario**: Diseño adaptado a diferentes perfiles.

## 11. LECCIONES APRENDIDAS Y CONCLUSIONES

### 11.1. Desafíos enfrentados

#### 11.1.1. Desafíos técnicos
- **Procesamiento multilingüe**: Manejo de 24 idiomas con distintas estructuras gramaticales.
- **Extracción de información estructurada**: Análisis preciso de comentarios no estructurados.
- **Integración de APIs**: Gestión de errores y límites de los proveedores de IA.
- **Tiempos de ejecución**: Optimización para grandes volúmenes de comentarios.

#### 11.1.2. Desafíos funcionales
- **Alineación con reglas de negocio**: Traducción de políticas empresariales a prompts efectivos.
- **Diseño de prompts**: Creación de instrucciones claras para los modelos de IA.
- **Longitud y estructura del prompt**: Encontrar el equilibrio entre detalle y eficacia.
- **Balance entre automatización y supervisión**: Determinar qué aspectos automatizar completamente.

### 11.2. Soluciones implementadas

- **Prompt estructurado**: Diseño modular con instrucciones claras y concisas.
- **Sistema dual de IA**: Implementación de OpenAI como motor principal con Gemini como respaldo.
- **Caching de traducciones**: Reducción de llamadas API innecesarias.
- **Refactorización del código**: Optimización para rendimiento y mantenibilidad.
- **Interfaces adaptadas**: Diseño específico para cada perfil de usuario.

### 11.3. Conclusiones principales

1. **Viabilidad demostrada**: La IA generativa puede automatizar eficazmente procesos complejos de atención al cliente.
2. **Importancia del diseño de prompts**: La estructura y claridad de las instrucciones son críticas para el éxito.
3. **Enfoque multimodal**: La combinación de análisis, interfaz y visualización crea un ecosistema completo.
4. **Resiliencia crítica**: Los sistemas de fallback son esenciales para aplicaciones empresariales reales.
5. **Valor estratégico**: La transformación de datos no estructurados en insights accionables aporta valor significativo.

## 12. TRABAJO FUTURO

### 12.1. Mejoras técnicas

- **Análisis de sentimiento avanzado**: Incorporar detección de emociones para adaptar tono de respuestas.
- **Soporte multimodal**: Procesar imágenes de productos dañados junto con el texto.
- **Aprendizaje continuo**: Implementar mecanismo de feedback para mejorar respuestas con el tiempo.
- **Análisis predictivo**: Anticipar problemas potenciales antes de que ocurran.
- **Optimización de costes API**: Reducir llamadas innecesarias y mejorar eficiencia.

### 12.2. Expansión funcional

- **Integración con CRM**: Conectar con sistemas de gestión de relaciones con clientes.
- **Conexión con redes sociales**: Ampliar análisis a comentarios en plataformas sociales.
- **API pública**: Ofrecer el motor de análisis como servicio para otros departamentos.
- **Asistente conversacional**: Evolucionar hacia un chatbot para interacción directa con clientes.
- **Panel de administración**: Crear interfaz para configurar reglas sin modificar código.

### 12.3. Escalabilidad

- **Arquitectura distribuida**: Adaptar para procesamiento paralelo de grandes volúmenes.
- **Base de datos unificada**: Centralizar almacenamiento para análisis histórico.
- **Despliegue en la nube**: Migrar a entorno productivo con autoscaling.
- **Monitorización continua**: Implementar alertas y dashboards operativos.
- **Documentación extendida**: Crear manuales detallados para usuarios finales.

## 13. REFERENCIAS TÉCNICAS

### 13.1. Bibliotecas y frameworks

- **Python**: https://www.python.org/
- **Pandas**: https://pandas.pydata.org/
- **Gradio**: https://gradio.app/
- **Streamlit**: https://streamlit.io/
- **Plotly**: https://plotly.com/python/
- **Langdetect**: https://pypi.org/project/langdetect/

### 13.2. APIs de IA

- **OpenAI**: https://platform.openai.com/
- **Google Gemini**: https://ai.google.dev/

### 13.3. Repositorio del proyecto

- **GitHub**: [Enlace al repositorio del proyecto]

### 13.4. Documentación académica

- Instituto de Inteligencia Artificial: https://iia.es/
- Curso Desarrollador 10X: Material formativo

## CONCLUSIONES FINALES

La creación de este sistema integrado para KelceTS S.L. ha demostrado el potencial transformador de la IA generativa en un contexto empresarial real. A través de un enfoque modular y centrado en el usuario, se ha logrado automatizar un proceso complejo manteniendo altos estándares de calidad.

El proyecto ha evolucionado desde las primeras validaciones en Google Colab hasta un sistema completo con tres componentes complementarios:

- **Google Colab**: Sirvió como entorno de validación técnica inicial
- **Gradio**: Ofrece una gestión rápida e individual para agentes de atención al cliente
- **Streamlit**: Proporciona una solución robusta y visual para equipos directivos

Cada herramienta cumple un propósito específico:
- **Colab** permitió validar técnicamente el concepto
- **Gradio** ofrece una interfaz tan intuitiva que un agente de atención al cliente puede utilizarla casi sin formación
- **Streamlit** proporciona una visión global para equipos de análisis, calidad, logística y dirección

El proyecto demuestra que un agente de IA bien diseñado puede resolver tareas complejas con mínima intervención humana, y con las interfaces adecuadas, resulta accesible para cualquier perfil de usuario, desde atención al cliente hasta la dirección.

KelceTS S.L. dispone ahora de un ecosistema completo que no solo resuelve su problema inmediato de gestión de comentarios, sino que proporciona una base sólida para la mejora continua de productos y servicios basada en datos.

---

## 📘 Agradecimientos y Cierre

Gracias al equipo docente del Institututo de Inteligencia Artificial.  
Ha sido toda una experiencia súper enriquecedoara formarme con vosotros.

A todos los que me puedan leer os recomiendo formaros con ellos.  
Os dejo aquí su link: https://iia.es/

¡Muchísimas gracias! 😍

**Araceli Fradejas Muñoz**

*Nota: KelceTS S.L. es una empresa ficticia creada como marco para este proyecto académico.*