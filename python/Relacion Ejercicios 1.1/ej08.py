# ==============================================================================
# EJERCICIO 8: Filtrar métricas de Machine Learning dentro de un rango específico
# ==============================================================================

# Definimos una función con tres parámetros:
# - 'metricas': un diccionario con nombres de métricas y sus puntuaciones.
# - 'min_val': el valor mínimo aceptable del rango.
# - 'max_val': el valor máximo aceptable del rango.
def filtrar_metricas(metricas, min_val, max_val):
    
    # Creamos un nuevo diccionario vacío para guardar solo las que cumplan la condición.
    metricas_filtradas = {}
    # Contador para saber cuántas métricas entraron en el rango.
    conteo = 0

    # Recorremos cada métrica (su nombre en 'metrica' y su número en 'valor').
    for metrica, valor in metricas.items():
        # Verificamos si el valor está comprendido entre 'min_val' y 'max_val' (ambos inclusive).
        if min_val <= valor <= max_val:
            metricas_filtradas[metrica] = valor  # Guardamos la métrica en el nuevo diccionario
            conteo += 1                          # Sumamos 1 al contador

    # Imprimimos el resultado del filtrado.
    print("RESULTADOS DEL FILTRADO")
    print(f"Diccionario filtrado: {metricas_filtradas}")

    # Estructura condicional para mostrar un mensaje descriptivo según si hubo coincidencias o no.
    if conteo > 0:
        print(f"Estado: Se han filtrado {conteo} métrica(s) dentro del rango [{min_val}, {max_val}].")
    else:
        print(f"Estado: Ninguna métrica cumplió con el criterio del rango [{min_val}, {max_val}].")

    # Calculamos cuántas métricas quedaron fuera (total original menos las aceptadas).
    descartadas = len(metricas) - conteo
    if descartadas > 0:
        print(f"Aviso: {descartadas} métrica(s) quedaron fuera del rango establecido.")

    # Devolvemos tanto el diccionario resultante como el número de métricas seleccionadas.
    return metricas_filtradas, conteo


# Diccionario de prueba con métricas habituales en modelos de Inteligencia Artificial (valores entre 0.0 y 1.0).
metricas_modelo = {
    "precision": 0.88,
    "recall": 0.74,
    "f1_score": 0.80,
    "accuracy": 0.85,
    "auc_roc": 0.91,
    "log_loss": 0.32,
    "tasa_falsos_positivos": 0.12
}

# Definimos los límites del filtro deseado (solo queremos valores entre 0.75 y 0.90).
rango_min = 0.75
rango_max = 0.90

# Mostramos el diccionario original antes de filtrar.
print(f"Métricas originales: {metricas_modelo}\n")

# Ejecutamos la función y recogemos los valores devueltos en dos variables: 'resultado_dict' y 'total'.
resultado_dict, total = filtrar_metricas(metricas_modelo, rango_min, rango_max)
