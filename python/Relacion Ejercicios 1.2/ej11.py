# ==============================================================================
# EJERCICIO 11: Crear, leer y analizar un archivo de temperaturas
# ==============================================================================

# PARTE 1: CREAR Y ESCRIBIR EN UN FICHERO
# ------------------------------------------------------------------------------
# Preparamos los datos en una tupla de textos.
# Cada línea incluye '\n', que significa 'salto de línea' (como pulsar Enter).
# La primera fila es el encabezado: indica qué significa cada columna.
canary_iata = (
    "Ciudad,Temperatura\n",
    "Madrid,32\n",
    "Barcelona,30\n",
    "Sevilla,35\n",
    "Valencia,31\n"
)

# 'open(..., "w")': Abre el archivo en modo ESCRITURA ("w" viene de "write").
# Si el archivo no existe lo crea; si ya existía, borra lo anterior y escribe de cero.
f = open("Relacion Ejercicios 1.2/datos_temperatura.txt", "w")

# '.writelines()' toma la tupla completa y escribe todas sus líneas en el fichero.
f.writelines(canary_iata)

# '.close()' cierra el archivo. Es como cerrar la puerta del archivador para que los datos queden bien guardados.
f.close()


# PARTE 2: ABRIR Y LEER EL ARCHIVO
# ------------------------------------------------------------------------------
# 'with open(..., "r") as f2:' abre en modo LECTURA ("r" viene de "read").
# El bloque 'with' es la forma recomendada en Python: se encarga de cerrar el archivo automáticamente al terminar.
with open("Relacion Ejercicios 1.2/datos_temperatura.txt", "r") as f2:
    # '.read()' lee todo el contenido del fichero de golpe y lo guarda como un solo texto gigante.
    lista = f2.read()
    print("Contenido leído del archivo:")
    print(lista)


# PARTE 3: EXTRAER SOLO LOS NÚMEROS DE LAS TEMPERATURAS (PASO A PASO)
# ------------------------------------------------------------------------------
# 1. Separamos el texto completo en una lista de líneas individuales:
lineas = lista.strip().splitlines()

# 2. Creamos una lista vacía para ir guardando solo las temperaturas numéricas:
listaTemperaturas = []

# 3. Recorremos las líneas con un bucle 'for':
# Usamos '[1:]' para saltarnos la línea 0 (el encabezado "Ciudad,Temperatura") y empezar en "Madrid,32".
for linea in lineas[1:]:
    # Cortamos la línea por la coma. Ejemplo: "Madrid,32" -> ["Madrid", "32"]
    partes = linea.split(",")
    
    # Cogemos el segundo dato (posición 1, la temperatura) y lo convertimos a número entero:
    temperatura = int(partes[1])
    
    # Lo añadimos a nuestra lista final:
    listaTemperaturas.append(temperatura)

print("Lista de temperaturas extraídas:", listaTemperaturas)


# PARTE 4: CALCULAR EL PROMEDIO
# ------------------------------------------------------------------------------
# Acumulador que arranca en 0.
total = 0

# Recorremos la lista de temperaturas y las sumamos todas.
for temperatura in listaTemperaturas:
    total += temperatura

# Calculamos el promedio: (suma total de grados) / (cantidad de ciudades).
print("Promedio de temperatura: ", total / len(listaTemperaturas))
