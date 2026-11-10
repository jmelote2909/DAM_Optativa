# ==============================================================================
# EJERCICIO 14: Procesar métricas de modelos con control de errores en fichero
# ==============================================================================

# FUNCIÓN 1: Lee el archivo línea por línea y crea un diccionario ordenado
# ------------------------------------------------------------------------------
def leer_metricas(ruta_archivo):
    # Creamos un diccionario vacío para organizar los datos por modelo.
    # Ejemplo de estructura final esperada:
    # {'modelo1': {'accuracy': 0.85, 'loss': 0.20}, 'modelo2': {...}}
    modelos = {}
    
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            # '.strip()' elimina espacios en blanco y saltos de línea al principio y final.
            linea = linea.strip()
            
            # Si la línea está vacía (por ejemplo, una línea en blanco al final del archivo),
            # la saltamos con 'continue' para no provocar errores.
            if not linea:
                continue

            # Cortamos la línea por las comas. Esperamos exactamente 3 partes: [modelo, métrica, valor].
            partes = linea.split(",")
            
            # CONTROL DE SEGURIDAD 1 (Validar formato):
            # Si la línea no tiene exactamente 3 partes (ej: si faltaba una coma o sobraba texto),
            # avisamos del problema y usamos 'continue' para saltar a la siguiente fila sin que el programa falle.
            if len(partes) != 3:
                print(f"Línea ignorada por formato incorrecto: {linea}")
                continue

            modelo = partes[0]
            metrica = partes[1]
            
            # CONTROL DE SEGURIDAD 2 (Validar que el dato sea un número):
            # Usamos 'try / except' (como poner una red de seguridad debajo de un trapecista).
            # Intentamos convertir el texto a número decimal con 'float()'.
            # Si alguien escribió letras en vez de números (ej: "alto"), saltaría un 'ValueError'.
            # En vez de cerrarse el programa con un error rojo, lo capturamos amablemente.
            try:
                valor = float(partes[2])
            except ValueError:
                print(f"Línea ignorada por valor no numérico: {linea}")
                continue

            # Guardamos el dato en el diccionario anidado:
            # Si es la primera vez que vemos este modelo, le creamos su propia "caja" (un diccionario interno vacío).
            if modelo not in modelos:
                modelos[modelo] = {}
            # Guardamos la métrica con su valor numérico dentro del modelo correspondiente.
            modelos[modelo][metrica] = valor

    # Devolvemos el diccionario completo ya estructurado y limpio.
    return modelos


# FUNCIÓN 2: Calcula las medias de cada métrica y encuentra el mejor modelo
# ------------------------------------------------------------------------------
def procesar_metricas(modelos):
    print("Diccionario de modelos procesado:")
    print(modelos)
    print()

    # Diccionarios auxiliares para acumular sumas y contar cuántas veces aparece cada métrica:
    totales = {}  # Guardará la suma de valores para cada métrica (ej: suma de todas las 'accuracy')
    conteos = {}  # Guardará cuántas veces se evaluó cada métrica
    
    mejor_modelo = None       # Guardará el nombre del modelo ganador
    mayor_accuracy = -1.0     # Empezamos con un valor muy bajo para que el primer modelo lo supere fácilmente

    # Bucle anidado para recorrer cada modelo y luego cada métrica dentro de ese modelo.
    for modelo, metricas in modelos.items():
        for metrica, valor in metricas.items():
            # Si es la primera vez que encontramos esta métrica, inicializamos sus contadores a 0.
            if metrica not in totales:
                totales[metrica] = 0.0
                conteos[metrica] = 0
            # Sumamos el valor numérico y añadimos 1 al contador.
            totales[metrica] += valor
            conteos[metrica] += 1

        # ALGORITMO DEL "MÁXIMO":
        # Verificamos si este modelo tiene evaluada la métrica 'accuracy' (precisión).
        # Si su precisión es más alta que la mayor que hayamos visto hasta ahora,
        # actualizamos el récord y recordamos su nombre.
        if "accuracy" in metricas:
            if metricas["accuracy"] > mayor_accuracy:
                mayor_accuracy = metricas["accuracy"]
                mejor_modelo = modelo

    # Mostramos los promedios de cada métrica dividiendo la suma total entre el conteo.
    print("Promedios de cada métrica:")
    for metrica in totales:
        promedio = totales[metrica] / conteos[metrica]
        print(f"Promedio {metrica}: {promedio:.2f}")

    print()
    print(f"Modelo con mayor accuracy: {mejor_modelo} con {mayor_accuracy}")
    

# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------
# 1. Definimos la ruta del archivo de texto.
ruta = "Relacion Ejercicios 1.2/metricas.txt"

# 2. Leemos y transformamos los datos a un diccionario.
datos_modelos = leer_metricas(ruta)

# 3. Analizamos las métricas y mostramos el informe final por pantalla.
procesar_metricas(datos_modelos)
