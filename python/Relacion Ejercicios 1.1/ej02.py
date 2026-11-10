# ==============================================================================
# EJERCICIO 2: Clasificar frutas por su tamaño de nombre (largas vs cortas)
# ==============================================================================

# Creamos una lista vacía para almacenar las frutas que el usuario escriba.
frutas = []

# Le preguntamos al usuario cuántas frutas quiere escribir.
# 'int()' convierte la respuesta de texto a un número entero.
numLeg = int(input("¿Cuantas frutas quieres introducir?: "))

# Validamos que se introduzcan al menos 8 frutas.
# Si el usuario introduce menos de 8, el bucle 'while' insistirá hasta que ponga 8 o más.
while numLeg < 8:
    numLeg = int(input("Mínimo 8 frutas, ¿cuantas frutas quieres introducir?: "))

# Bucle 'for': se ejecuta tantas veces como frutas dijo el usuario.
for i in range(numLeg):
    # En cada repetición pedimos el nombre de una fruta (en texto).
    fruta = input("Introduce una fruta: ")
    # La guardamos en nuestra lista 'frutas'.
    frutas.append(fruta)

# Mostramos la lista completa de frutas introducidas.
print(f"\nLista de frutas: {frutas}")

# Creamos dos listas nuevas para clasificar las frutas:
# - 'largas': para las que tengan 5 o más letras.
# - 'cortas': para las que tengan menos de 5 letras.
largas = []
cortas = []

# Recorremos la lista 'frutas' una por una con un bucle 'for'.
for fruta in frutas:
    # 'len(fruta)' cuenta la cantidad de caracteres (letras) que tiene la palabra.
    # Si tiene 5 o más letras, va a 'largas'; si no, va a 'cortas'.
    if len(fruta) >= 5:
        largas.append(fruta)
    else:
        cortas.append(fruta)

# Mostramos los elementos que quedaron en cada lista.
print(f"\nFrutas con longitud mayor o igual a 5: {largas}")
print(f"\nFrutas con longitud menor a 5: {cortas}")

# 'len()' también nos dice cuántos elementos tiene una lista.
# Mostramos la cantidad total de frutas en cada categoría.
print(f"\nCantidad de frutas con longitud mayor o igual a 5: {len(largas)}")
print(f"\nCantidad de frutas con longitud menor a 5: {len(cortas)}")
