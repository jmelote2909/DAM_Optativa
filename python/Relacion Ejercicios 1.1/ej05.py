# ==============================================================================
# EJERCICIO 5: Contar elementos únicos por tipo de dato en una tupla mixta
# ==============================================================================

# Una tupla que mezcla muchos tipos de datos distintos:
# - Enteros (int): 10, 45, etc.
# - Textos (str): "hola", "frutinovelas", "views", "COCARDO"
# - Booleanos (bool): True, False
# - Decimales (float): 3.14
# Nota: el 45 aparece dos veces, por lo que NO es un elemento único.
tupla_mixta = (10, "hola", True, 45, "frutinovelas", False, 3.14, "views", 45, "COCARDO")

# Función que clasifica y cuenta únicamente los elementos que NO están repetidos.
def contar_unicos_por_tipo(tupla):
    # Creamos contadores en cero para cada tipo de dato y uno general.
    unicos_int = 0        # Para números enteros
    unicos_float = 0      # Para números con decimales
    unicos_cadenas = 0    # Para textos / cadenas
    unicos_booleanos = 0  # Para valores Verdadero/Falso (True/False)
    unicos_totales = 0    # Para la suma total de elementos únicos
    
    # Recorremos cada elemento de la tupla uno por uno.
    for elemento in tupla:
        # 'tupla.count(elemento)' nos dice cuántas veces existe ese elemento en la tupla.
        # Si devuelve 1, significa que aparece una única vez (no tiene copias).
        if tupla.count(elemento) == 1:
            unicos_totales += 1  # Incrementamos el contador general en 1
            
            # DETALLE CLAVE DE PYTHON:
            # En Python, los booleanos (True y False) son internamente una subclase de los enteros (int).
            # True vale 1 y False vale 0. Por eso, SIEMPRE comprobamos primero si es 'bool'
            # usando 'type(elemento) is bool' antes de comprobar 'int', para que no se confundan.
            if type(elemento) is bool:
                unicos_booleanos += 1
            elif type(elemento) is int:
                unicos_int += 1
            elif type(elemento) is float:
                unicos_float += 1
            elif type(elemento) is str:
                unicos_cadenas += 1

    # Devolvemos una tupla con todos los resultados empaquetados en orden:
    # posición 0: enteros, 1: flotantes, 2: cadenas, 3: booleanos, 4: totales.
    return (unicos_int, unicos_float, unicos_cadenas, unicos_booleanos, unicos_totales)


# Llamamos a la función pasándole nuestra tupla de prueba y guardamos la respuesta en 'conteos'.
conteos = contar_unicos_por_tipo(tupla_mixta)

# Mostramos los resultados de forma clara y legible.
print(f"Tupla original: {tupla_mixta}")
print(f"\nElementos totales: {len(tupla_mixta)} | únicos {conteos[4]}")
print(f"\nConteos de elementos únicos por tipo:")
print(f"- Enteros únicos: {conteos[0]}")
print(f"- Flotantes únicos: {conteos[1]}")
print(f"- Cadenas únicas: {conteos[2]}")
print(f"- Booleanos únicos: {conteos[3]}")
