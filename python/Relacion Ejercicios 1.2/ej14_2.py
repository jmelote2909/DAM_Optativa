# ==============================================================================
# EJERCICIO 14.2: Procesar métricas usando el módulo estándar 'csv' de Python
# ==============================================================================
# Este archivo es una variante del Ejercicio 14.
# En lugar de cortar las líneas a mano con '.split(",")', usamos la librería oficial 'csv'.
# 'csv.reader' es una herramienta especializada que se encarga de leer archivos de tablas
# separadas por comas o tabuladores de forma automática y mucho más limpia.

import csv
import os

# FUNCIÓN 1: Lee el archivo CSV y genera el diccionario de modelos y métricas
# ------------------------------------------------------------------------------
def leer_metricas(ruta_archivo):
    modelos = {}
    
    # Comprobamos si el archivo existe antes de abrirlo para evitar errores
    if not os.path.exists(ruta_archivo):
        print(f"Aviso: El archivo '{ruta_archivo}' no se encontró.")
        return modelos

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        # 'csv.reader' analiza el archivo y nos entrega cada fila ya convertida en una lista de palabras/valores.
        csv_reader = csv.reader(f)
        
        for fila in csv_reader:
            # Si la fila está vacía, la ignoramos
            if not fila:
                continue

            # Si la fila es el encabezado (ej: ["modelo", "métrica", "valor"]), la saltamos
            if fila[0].lower() in ("modelo", "model"):
                continue

            # Control de formato: verificamos que la fila tenga al menos 3 columnas
            if len(fila) < 3:
                continue

            modelo = fila[0].strip()
            metrica = fila[1].strip()
            
            # Intentamos convertir el valor a número decimal
            try:
                valor = float(fila[2].strip())
            except ValueError:
                continue

            # Guardamos en el diccionario anidado
            if modelo not in modelos:
                modelos[modelo] = {}
            modelos[modelo][metrica] = valor

    return modelos


# FUNCIÓN 2: Calcula las estadísticas y busca el modelo con mejor precisión
# ------------------------------------------------------------------------------
def procesar_metricas(modelos):
    if not modelos:
        print("No hay datos de modelos para procesar.")
        return

    print("Diccionario de modelos (leído con módulo CSV):")
    print(modelos)
    print()

    totales = {}
    conteos = {}
    mejor_modelo = None
    mayor_accuracy = -1.0

    for modelo, metricas in modelos.items():
        for metrica, valor in metricas.items():
            if metrica not in totales:
                totales[metrica] = 0.0
                conteos[metrica] = 0
            totales[metrica] += valor
            conteos[metrica] += 1

        if "accuracy" in metricas:
            if metricas["accuracy"] > mayor_accuracy:
                mayor_accuracy = metricas["accuracy"]
                mejor_modelo = modelo

    print("Promedios de cada métrica:")
    for metrica in totales:
        promedio = totales[metrica] / conteos[metrica]
        print(f"Promedio {metrica}: {promedio:.2f}")

    print()
    if mejor_modelo:
        print(f"Modelo con mayor accuracy: {mejor_modelo} con {mayor_accuracy}")


# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------
# Primero definimos las funciones arriba para que Python las conozca antes de llamarlas.
# Usamos 'metricas.txt' o 'metricas.csv' si están disponibles.
ruta = "Relacion Ejercicios 1.2/metricas.txt" if os.path.exists("Relacion Ejercicios 1.2/metricas.txt") else "Relacion Ejercicios 1.2/metricas.csv"

datos_modelos = leer_metricas(ruta)
procesar_metricas(datos_modelos)
