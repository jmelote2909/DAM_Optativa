# ==============================================================================
# EJERCICIO 4: Ubicar coordenadas (x, y) en cuadrantes y calcular su suma
# ==============================================================================

# Una tupla es una colección ordenada e inmutable (fija).
# Aquí tenemos una tupla principal que contiene 4 pares de coordenadas (x, y).
# En un plano cartesiano:
# - Eje X: horizontal (positivo hacia la derecha, negativo hacia la izquierda).
# - Eje Y: vertical (positivo hacia arriba, negativo hacia abajo).
tupla = ((-4, 2), (-3, 5), (6, -3), (7, -8))

# Al escribir 'for x, y in tupla:', Python desempaca automáticamente
# el primer número del par en la variable 'x' y el segundo en 'y'.
for x, y in tupla:
    # 1º Cuadrante: x es positivo (derecha) e y es positivo (arriba) (+, +)
    if x > 0 and y > 0:
        print(f"({x}, {y}) está en el primer cuadrante.")
    # 2º Cuadrante: x es negativo (izquierda) e y es positivo (arriba) (-, +)
    elif x < 0 and y > 0:
        print(f"({x}, {y}) está en el segundo cuadrante.")
    # 3º Cuadrante: x es negativo (izquierda) e y es negativo (abajo) (-, -)
    elif x < 0 and y < 0:
        print(f"({x}, {y}) está en el tercer cuadrante.")
    # 4º Cuadrante: x es positivo (derecha) e y es negativo (abajo) (+, -)
    elif x > 0 and y < 0:
        print(f"({x}, {y}) está en el cuarto cuadrante.")
    # Si alguno de los dos valores es 0, el punto no está dentro de ningún cuadrante, sino sobre un eje.
    else:
        print(f"({x}, {y}) está en un eje.")
    
    # Mostramos la suma matemática de las dos coordenadas (x + y).
    print(f"Suma total: {x + y}\n")
