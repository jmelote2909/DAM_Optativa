# ==============================================================================
# EJERCICIO 1: Filtrar números pares y pedir un mínimo de 10 números
# ==============================================================================

# Creamos dos listas vacías (como si fueran dos cajones vacíos):
pares = []
numeros = []

# Le pedimos al usuario por teclado cuántos números desea ingresar.
numLeg = int(input("¿Cuantos numeros quieres introducir?: "))

# REGLA: Exigimos que al menos sean 10 números.
while numLeg < 10:
    numLeg = int(input("Mínimo 10 numeros, ¿cuantos numeros quieres introducir?: "))

# Bucle 'for': se repite tantas veces como el número que nos dijo el usuario ('numLeg').
for i in range(numLeg):
    # Pedimos un número en cada vuelta.
    num = int(input("Introduce un número: "))
    
    # '.append(num)' añade el número al final de la lista 'numeros'.
    numeros.append(num)
        
    # El operador '%' (módulo) calcula el resto de la división entre 2.
    if num % 2 == 0:
        pares.append(num)

# Mostramos en pantalla la lista con todos los números introducidos.
print(f"\nTodos los numeros: {numeros}")

# Comprobamos si la lista de pares está vacía usando 'len()' (que mide la longitud o tamaño).
# Si el tamaño es 0, es que no se encontró ningún número par.
if len(pares) == 0:
    print("No hay numeros pares")
else:
    print(f"Pares: {pares}")
