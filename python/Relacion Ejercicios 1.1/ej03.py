# ==============================================================================
# EJERCICIO 3: Separar elementos únicos y duplicados en una lista
# ==============================================================================

# Definimos una función llamada 'numerosDuplicados' que recibe como parámetro una lista.
def numerosDuplicados(lista):
    # Creamos dos listas vacías:
    # - 'listaSinDuplicados': para guardar los números la primera vez que los vemos.
    # - 'listaDuplicados': para guardar los números que ya habían aparecido antes (repetidos).
    listaSinDuplicados = []
    listaDuplicados = []
    
    # Recorremos cada número de la lista original uno a uno.
    for numero in lista:
        # El operador 'not in' pregunta: "¿Este número NO está todavía en 'listaSinDuplicados'?"
        # Si NO está, significa que es la primera vez que lo vemos, así que lo guardamos allí.
        if numero not in listaSinDuplicados:
            listaSinDuplicados.append(numero)
        # Si la condición no se cumple (es decir, ya está en la lista), significa que está repetido.
        else:
            listaDuplicados.append(numero)
            
    # La función devuelve un paquete con las dos listas resultantes y un texto que indica que son listas.
    return "Lista sin duplicados", listaSinDuplicados, "Lista de duplicados", listaDuplicados

# Creamos una lista de prueba con algunos números repetidos (del 1 al 5 están dos veces).
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

print(f"Lista original: {lista}")

# Llamamos a la función con nuestra lista y mostramos el resultado devuelto en pantalla.
print(numerosDuplicados(lista))
