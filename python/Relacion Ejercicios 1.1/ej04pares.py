# ==============================================================================
# EJERCICIO 4 (Variante Pares): Comprobar la paridad de cada coordenada
# ==============================================================================

# Tenemos una tupla de pares de números (x, y).
tupla = ((4, 2), (3, 5), (6, 3), (7, 8))

# Recorremos cada pareja de números (x, y).
for x, y in tupla:
    # Usamos el operador '%' (resto de la división entera entre 2):
    # - Si 'num % 2 == 0', el número es PAR.
    # - Si 'num % 2 != 0', el número es IMPAR.

    # Caso 1: Los dos números (tanto x como y) son pares.
    if x % 2 == 0 and y % 2 == 0:
        print(f"({x}, {y}) es par en el primer y segundo cuadrante")
    # Caso 2: Ninguno de los dos es par (ambos son impares).
    elif x % 2 != 0 and y % 2 != 0:
        print(f"({x}, {y}) es par en ningun cuadrante")
    # Caso 3: Solo el primer número (x) es par, mientras que el segundo (y) es impar.
    elif x % 2 == 0 and y % 2 != 0:
        print(f"({x}, {y}) es par en el primer cuadrante")
    # Caso 4: Solo el segundo número (y) es par, mientras que el primero (x) es impar.
    elif y % 2 == 0 and x % 2 != 0:
        print(f"({x}, {y}) es par en el segundo cuadrante")
    
    # Mostramos la suma total de x e y.
    print(f"Suma total: {x + y}\n")
