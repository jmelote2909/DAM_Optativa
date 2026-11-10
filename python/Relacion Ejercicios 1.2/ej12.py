# ==============================================================================
# EJERCICIO 12: Filtrar datos de satisfacción de clientes desde un archivo
# ==============================================================================

# Contadores inicializados a 0:
# - 'total_lineas': contará cuántas líneas leemos en total (incluyendo el encabezado).
# - 'alta_satisfaccion': contará cuántas personas calificaron con más de 3 puntos.
total_lineas = 0
alta_satisfaccion = 0

# Abrimos el fichero 'datos.txt' en modo solo lectura ("r").
# Al usar 'with open', el archivo se cerrará solo al salir de este bloque.
with open("Relacion Ejercicios 1.2/datos.txt", "r") as f:
    # Cuando hacemos 'for linea in f:', Python lee el archivo línea por línea de forma eficiente,
    # sin cargar todo el archivo en la memoria a la vez.
    for linea in f:
        total_lineas += 1
        
        # Como la línea 1 son los títulos de las columnas ("edad,ciudad,satisfacción"),
        # usamos 'if total_lineas > 1' para ignorar el encabezado y trabajar solo con los datos reales.
        if total_lineas > 1:
            # '.strip()' elimina el salto de línea invisible al final.
            # '.split(",")' corta la línea en trozos usando la coma como tijera.
            # Ejemplo: "25,Madrid,4" se convierte en: ["25", "Madrid", "4"]
            partes = linea.strip().split(",")
            
            # La posición [1] es la ciudad (segunda columna)
            ciudad = str(partes[1])
            # La posición [2] es la puntuación (tercera columna), la convertimos a entero con 'int()'
            satisfaccion = int(partes[2])

            # Condición: ¿La satisfacción es mayor que 3 (puntuación alta: 4 o 5)?
            if satisfaccion > 3:
                print("Ciudad: ", ciudad, " | Satisfaccion: ", satisfaccion)
                # Sumamos 1 a nuestro contador de clientes muy satisfechos
                alta_satisfaccion += 1

# Mostramos el resumen final de lo que hemos procesado.
print("\nTotal de líneas procesadas:", total_lineas)
print("Entradas con alta satisfacción (más de 3):", alta_satisfaccion)
