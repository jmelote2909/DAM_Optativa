# ==============================================================================
# EJERCICIO 13: Análisis básico de sentimientos en comentarios de clientes
# ==============================================================================

# Listas de palabras clave (vocabulario detector):
# Si una opinión contiene alguna de estas palabras, la consideraremos positiva o negativa.
positivas = ["excelente", "bueno", "buen", "recomendado", "satisfecho"]
negativas = ["mala", "no", "problema", "defecto"]

# Contadores para saber cuántos comentarios caen en cada categoría.
cont_positivos = 0
cont_negativos = 0

# PASO A: LEER TODO EL ARCHIVO
# ------------------------------------------------------------------------------
# 'encoding="utf-8"' es fundamental cuando trabajamos con español, ya que permite leer
# tildes (á, é, í...), la letra 'ñ' y caracteres especiales sin que salgan símbolos raros.
with open("Relacion Ejercicios 1.2/comentarios_productos.txt", "r", encoding="utf-8") as f:
    # '.readlines()' lee todo el fichero y devuelve una lista donde cada elemento es una línea del texto.
    lineas = f.readlines()

# Contamos cuántos comentarios hay en total con 'len()'.
total_lineas = len(lineas)


# PASO B: CLASIFICAR CADA COMENTARIO
# ------------------------------------------------------------------------------
for linea in lineas:
    # Convertimos toda la frase a minúsculas con '.lower()'.
    # ¿Por qué? Porque si un cliente escribió "EXCELENTE" o "Excelente",
    # queremos que coincida con nuestra palabra "excelente" sin problemas de mayúsculas.
    texto = linea.lower()

    # Revisamos si contiene alguna de las palabras positivas.
    for p in positivas:
        if p in texto:
            cont_positivos += 1
            # 'break' detiene este bucle interior inmediatamente: si ya encontramos
            # una palabra positiva, no necesitamos seguir buscando más en la misma línea.
            break

    # Revisamos si contiene alguna de las palabras negativas.
    for n in negativas:
        if n in texto:
            cont_negativos += 1
            # 'break' detiene la búsqueda si ya detectamos que tiene una palabra negativa.
            break


# PASO C: CALCULAR PORCENTAJES Y MOSTRAR RESULTADOS
# ------------------------------------------------------------------------------
# Fórmula de porcentaje: (cantidad encontrada / total de comentarios) * 100
pct_positivos = (cont_positivos / total_lineas) * 100
pct_negativos = (cont_negativos / total_lineas) * 100

# Imprimimos en pantalla con formato de un decimal (ej: 60.0%).
print(f"Total comentarios: {total_lineas}")
print(f"Positivos: {cont_positivos} ({pct_positivos:.1f}%)")
print(f"Negativos: {cont_negativos} ({pct_negativos:.1f}%)")


# PASO D: GUARDAR UN INFORME EN UN NUEVO ARCHIVO
# ------------------------------------------------------------------------------
# Abrimos en modo "w" (escritura). Si el archivo 'resumen_sentimientos.txt' no existe, lo crea.
with open("Relacion Ejercicios 1.2/resumen_sentimientos.txt", "w", encoding="utf-8") as f_resumen:
    # '.write()' escribe una frase dentro del archivo. Añadimos '\n' para dar un salto de línea al final.
    f_resumen.write(f"Total comentarios: {total_lineas}\n")
    f_resumen.write(f"Comentarios positivos: {cont_positivos} ({pct_positivos:.1f}%)\n")
    f_resumen.write(f"Comentarios negativos: {cont_negativos} ({pct_negativos:.1f}%)\n")
