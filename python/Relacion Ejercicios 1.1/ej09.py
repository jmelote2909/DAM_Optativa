# ==============================================================================
# EJERCICIO 9: Agrupar palabras por su longitud (NLP / Procesamiento de Lenguaje)
# ==============================================================================

# Definimos una función que recibe una lista de palabras ('corpus').
def agrupar_por_longitud(corpus):

    # Creamos un diccionario vacío para clasificar las palabras.
    # Las claves serán números (el largo de la palabra, ej: 4) y los valores serán listas de palabras.
    longitudes_dict = {}

    # Recorremos cada palabra de la lista original.
    for palabra in corpus:
        # 'len(palabra)' calcula el número de caracteres (letras) que tiene.
        longitud = len(palabra)
        
        # Comprobamos si ya tenemos una categoría en el diccionario para este número de letras:
        # Si ya existe (por ejemplo, ya había una palabra de 4 letras), simplemente la agregamos a su lista.
        if longitud in longitudes_dict:
            longitudes_dict[longitud].append(palabra)
        # Si es la primera vez que aparece una palabra con esta cantidad de letras,
        # creamos una nueva clave con una lista que contiene esta primera palabra.
        else:
            longitudes_dict[longitud] = [palabra]

    # Medimos el número total de palabras del corpus.
    total_palabras = len(corpus)
    if total_palabras > 0:
        # Sumamos la longitud de todas las palabras procesadas y dividimos entre el total para hallar la media.
        suma_longitudes = sum(len(palabra) for palabra in corpus)
        longitud_promedio = suma_longitudes / total_palabras
    else:
        longitud_promedio = 0.0

    # Imprimimos las estadísticas calculadas.
    print("Preprocesamiento de Corpus (NLP / Data Science)")
    print(f"Diccionario resultante:\n{longitudes_dict}")
    print(f"\nNúmero total de palabras procesadas: {total_palabras}")
    # ':.2f' formatea el promedio con dos decimales.
    print(f"Longitud promedio de las palabras: {longitud_promedio:.2f} caracteres\n")

    return longitudes_dict

# Lista de palabras de prueba
tokens_dataset = [
    "excelente", "producto", "bueno", "calidad", "precio", 
    "recomiendo", "rapido", "servicio", "app", "crush", 
    "bug", "solucion", "datos", "ia", "modelo", "nlp"
]

# Ejecutamos la función pasándole la lista.
resultado = agrupar_por_longitud(tokens_dataset)
