# ==============================================================================
# EJERCICIO 6: Detectar productos con stock bajo en un inventario
# ==============================================================================

# Un diccionario es como una agenda de teléfono o una tabla de dos columnas:
# A la izquierda está la "clave" (nombre del producto) y a la derecha su "valor" (unidades en almacén).
inventario = {
    "Manzanas": 12,
    "Plátanos": 3,
    "Naranjas": 8,
    "Kiwis": 2,
    "Fresas": 15,
    "Mangos": 4,
    "Uvas": 10
}

# Variable acumuladora (un contador que empieza en 0)
# donde iremos sumando las unidades de los productos que tengan poco stock.
total_cantidad_baja = 0

print("Productos con stock bajo (menos de 5 unidades):")

# '.items()' nos entrega a la vez cada pareja de (clave, valor) en cada vuelta del bucle:
# 'producto' guardará el nombre (ej: "Plátanos") y 'cantidad' su número (ej: 3).
for producto, cantidad in inventario.items():
    # Comprobamos si la cantidad disponible es menor que 5 unidades.
    if cantidad < 5:
        # Mostramos qué producto es y cuántas unidades le quedan.
        print(f"- {producto}: {cantidad} unidades")
        # Sumamos esas unidades a nuestro acumulador total.
        total_cantidad_baja += cantidad

# Al terminar de revisar todo el inventario, mostramos la suma total de unidades escasas.
print(f"\nCantidad total de unidades de estos productos: {total_cantidad_baja}")
