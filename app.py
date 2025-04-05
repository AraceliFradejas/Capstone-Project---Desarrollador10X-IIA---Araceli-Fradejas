@st.cache_data(ttl=10)  # Reducimos el tiempo de caché a 10 segundos
def cargar_datos():
    try:
        # Rutas de posibles ubicaciones de los archivos
        rutas_txt_posibles = [
            "comentarios.txt",  # Directorio actual
            "./comentarios.txt",
            "../comentarios.txt",
            "/workspaces/kelcets-dashboard/comentarios.txt",  # Ajusta esta ruta a tu Codespace
            "BD Comentarios KelceTS.txt",
            "./BD Comentarios KelceTS.txt",
            "/workspaces/kelcets-dashboard/BD Comentarios KelceTS.txt",
            "comentarios_kelcets.txt",
            "./comentarios_kelcets.txt"
        ]
        
        # Intentar cargar desde cada ruta posible
        comentarios = None
        archivo_cargado = None
        
        for ruta in rutas_txt_posibles:
            try:
                st.sidebar.text(f"Intentando cargar: {ruta}")
                if os.path.exists(ruta):
                    # Cargar los datos desde el archivo de texto
                    with open(ruta, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                    
                    # Dividir el contenido en comentarios (ajusta según el formato de tu archivo)
                    comentarios = [comment.strip() for comment in contenido.split('\n\n') if comment.strip()]
                    
                    archivo_cargado = ruta
                    st.sidebar.success(f"Datos cargados desde: {ruta}")
                    st.sidebar.text(f"Total de comentarios: {len(comentarios)}")
                    break
            except Exception as e:
                st.sidebar.error(f"Error al cargar {ruta}: {e}")
        
        if comentarios is None:
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
            comentarios = [
                "Ejemplo de comentario 1",
                "Ejemplo de comentario 2",
                "Ejemplo de comentario 3",
                "Ejemplo de comentario 4",
                "Ejemplo de comentario 5"
            ]
        
        # Procesar comentarios y crear DataFrames simulados
        # Esto es una simulación - ajusta según el formato real de tus comentarios
        data_resumen = {
            'ID': list(range(1, len(comentarios) + 1)),
            'Comentario_Original': comentarios,
            'Idioma': ['español', 'alemán', 'español', 'finés', 'portugués'] * ((len(comentarios) // 5) + 1),
            'Valoracion': ['positiva', 'negativa', 'positiva', 'negativa', 'neutra'] * ((len(comentarios) // 5) + 1),
            'Envio_96h': ['sí', 'no', 'sí', 'no', 'no mencionado'] * ((len(comentarios) // 5) + 1),
            'Embalaje_Danado': ['no', 'sí', 'no', 'no', 'no mencionado'] * ((len(comentarios) // 5) + 1),
            'Talla_Correcta': ['sí', 'no', 'sí', 'no', 'no mencionado'] * ((len(comentarios) // 5) + 1),
            'Materiales_Calidad': ['sí', 'no', 'parcialmente', 'no', 'no mencionado'] * ((len(comentarios) // 5) + 1),
            'Tipo_Uso': ['diario', 'ocasional', 'diario', 'ocasional', 'no mencionado'] * ((len(comentarios) // 5) + 1),
            'Cumple_Expectativas': ['sí', 'no', 'parcialmente', 'no', 'no mencionado'] * ((len(comentarios) // 5) + 1)
        }
        
        # Recortar listas al tamaño de comentarios
        for key in data_resumen:
            if key != 'ID' and key != 'Comentario_Original':
                data_resumen[key] = data_resumen[key][:len(comentarios)]
        
        # Crear estadísticas a partir de los datos
        valoraciones_positivas = data_resumen['Valoracion'].count('positiva')
        valoraciones_negativas = data_resumen['Valoracion'].count('negativa')
        valoraciones_neutras = data_resumen['Valoracion'].count('neutra')
        problemas_materiales = data_resumen['Materiales_Calidad'].count('no')
        problemas_talla = data_resumen['Talla_Correcta'].count('no')
        problemas_envio = data_resumen['Envio_96h'].count('no')
        problemas_embalaje = data_resumen['Embalaje_Danado'].count('sí')
        
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
            'Valor': [
                len(comentarios),
                valoraciones_positivas,
                valoraciones_negativas,
                valoraciones_neutras,
                problemas_materiales,
                problemas_talla,
                problemas_envio,
                problemas_embalaje,
                round(valoraciones_positivas / len(comentarios) * 100 if len(comentarios) > 0 else 0, 2)
            ]
        }
        
        df = pd.DataFrame(data_resumen)
        df_comunicaciones = pd.DataFrame({
            'ID': df['ID'],
            'Comentario_Original': df['Comentario_Original'],
            'Email_Cliente': ['Email simulado para cliente ' + str(i) for i in range(1, len(comentarios) + 1)]
        })
        df_estadisticas = pd.DataFrame(data_estadisticas)
        
        return df, df_comunicaciones, df_estadisticas, (archivo_cargado is not None)
        
    except Exception as e:
        st.error(f"Error en la función cargar_datos: {e}")
        import traceback
        st.error(traceback.format_exc())
        return None, None, None, False