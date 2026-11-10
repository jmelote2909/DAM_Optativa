# ==============================================================================
# EJERCICIO 15: Escribir y leer temperaturas usando la librería 'csv'
# ==============================================================================

# Importamos el módulo 'csv' (herramienta especializada incluida en Python para tablas).
import csv

# Datos iniciales en una tupla de textos listos para ser guardados.
datos = (
    "ciudad, temperatura\n",
    "Madrid, 32\n",
    "Barcelona, 30\n",
    "Valencia, 31\n",
    "Sevilla, 35\n"
)

# Guardamos la ruta del archivo en una variable para no tener que repetirla muchas veces.
ruta = "Relacion Ejercicios 1.2/temperaturas.txt"


# PASO 1: GUARDAR LOS DATOS EN EL ARCHIVO
# ------------------------------------------------------------------------------
def guardar_archivo():
    # Abrimos en modo "w" (escritura). Si el archivo no existe, lo crea automáticamente.
    with open(ruta, "w") as archivo:
        # '.writelines()' escribe todas las frases de la tupla en el archivo de texto.
        archivo.writelines(datos)

# Llamamos a la función para que se cree y guarde el archivo en el disco.
guardar_archivo()


# PASO 2: LEER LOS DATOS CON CSV.READER
# ------------------------------------------------------------------------------
# Lista vacía donde guardaremos únicamente los grados de temperatura.
temperaturas = []

# Abrimos el archivo en modo "r" (lectura).
with open(ruta, "r") as archivo:
    # 'csv.reader' es un lector inteligente: lee el archivo y separa cada columna por su coma automáticamente.
    lector = csv.reader(archivo)

    # 'next(lector)': Esta función mágica lee la primera fila (el encabezado "ciudad, temperatura")
    # y la descarta. Así el bucle 'for' empezará directamente desde los datos reales de Madrid.
    next(lector)

    # Recorremos cada fila restante. 'fila' es una lista como: ['Madrid', ' 32']
    for fila in lector:
        # 'fila[1]' es la segunda columna (la temperatura).
        # Usamos 'float()' para convertirla en número con decimales y la agregamos a la lista.
        temperaturas.append(float(fila[1]))


# PASO 3: CALCULAR EL PROMEDIO Y MOSTRAR RESULTADOS
# ------------------------------------------------------------------------------
# 'sum(temperaturas)' es una función nativa de Python que suma todos los números de la lista directamente.
# 'len(temperaturas)' nos dice cuántos elementos hay (en este caso 4).
# Al dividir la suma entre la cantidad obtenemos el promedio.
promedio_temperatura = sum(temperaturas) / len(temperaturas)

print(f"Temperaturas extraídas: {temperaturas}")
print(f"Promedio de temperaturas: {promedio_temperatura} ºC")
