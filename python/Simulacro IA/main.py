import csv
ruta = "Simulacro IA/ventas_videojuegos.csv"
fila_titulo = []
fila_genero = []
fila_precio = []
fila_copias_vendidas = []

datos = {
    "titulo": [],
    "genero": [],
    "precio": [],
    "copias_vendidas": []
}

#a. Número total de registros de videojuegos procesados.
def numTotalRegistrosProcesados():
    cont = 0
    for registro in datos["titulo"]:
        cont = cont + 1 
    print(cont)
    return cont


#b. Precio medio de los títulos ofertados en el catálogo.
def precioMedioPorTitulo():
    print(sum(fila_precio) / float(cont_Registros))


#c. El videojuego con mayor volumen de ventas, indicando el título y el número de copias vendidas.
def mayorVolumenVentas():
    cont_pos = 0
    pos_final = 0
    copias_final = 0

    for copias in datos["copias_vendidas"]:

        if (copias > copias_final):

            copias_final = copias
            pos_final = cont_pos

        cont_pos = cont_pos + 1

    print(datos["titulo"][pos_final], "(", [pos_final], ")")

    
#d. La recaudación total agrupada por género, calculada para cada registro como:
def recaudacionTotalPorGenero():
    recaudacion_genero = {}
    cont_pos = 0

    for genero in datos["genero"]:
        precio = datos["precio"][cont_pos]
        copias = datos["copias_vendidas"][cont_pos]
        total_juego = precio * copias

        if genero not in recaudacion_genero:
            recaudacion_genero[genero] = 0

        recaudacion_genero[genero] = recaudacion_genero[genero] + total_juego
        cont_pos = cont_pos + 1

    print("Recaudación total por género:")
    for gen in recaudacion_genero:
        print(" -", gen, ":", recaudacion_genero[gen], "€")
    
    return recaudacion_genero


#MAIN
with open(ruta, "r") as f:
    lista = csv.reader(f)

    #OMITE LA CABECERA (PASA A LA SIGUIENTE FILA)
    next(lista)

    for fila in lista:
        fila_titulo.append(fila[0])
        datos["titulo"] = fila_titulo

        fila_genero.append(fila[1])
        datos["genero"] = fila_genero

        fila_precio.append(float(fila[2]))
        datos["precio"] = fila_precio

        fila_copias_vendidas.append(int(fila[3]))
        datos["copias_vendidas"] = fila_copias_vendidas

    
    print(datos)
    print("-----------------")
    cont_Registros = numTotalRegistrosProcesados()
    precioMedioPorTitulo()
    mayorVolumenVentas()
    recaudacionTotalPorGenero()