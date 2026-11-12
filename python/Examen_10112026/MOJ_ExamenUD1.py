# Examen UD1 - Optativa de Programación Python aplicado a la Inteligencia Artificial
# Autor/a: Nombre y Apellidos
# Fecha: 10/11/2026
# Solución
#
# -----------------------------------------------------------------------------------------
#

import csv

# ESPECIFICAMOS LA RUTA DEL ARCHIVO A LEER
ruta = "Examen_10112026/"

# DEFINIMOS LISTAS POR CADA COLUMNA DE LA BIBLIOTECA DE DATOS
columnaProducto = []
columnaCategoria = []
columnaPrecio = []
columnaUnidades_vendidas = []

# DEFINIMOS E INICIALIZAMOS LA BIBLIOTECA DE DATOS CON SUS ÍNDICES
datos={
    "Producto":{},
    "Categoria":{},
    "Precio":{},
    "Unidades_Vendidas":{}
}


#a. CALCULALMOS EL NÚMERO TOTAL DE PRODUCTOS REGISTRADOS.
def NumTotalRegistrosProcesados():
    cont = 0
    # RECORREMOS TODOS LOS PRODUCTOS PARA CALCULAR CUANTOS HAY
    for registro in datos["Producto"]:
        cont = cont + 1 
    resultadoA = "Número total de productos: " + str(cont)
    print(resultadoA)
    
    
    #DEVOLVEMOS EL VALOR PARA USARLO MAS ADELANTE
    return cont, resultadoA


#b. CALCULAMOS EL PRECIO MEDIO DE TODOS LOS ARTÍCULOS.
def PrecioMedioArticulos():
    preciomedio = (float(sum(columnaPrecio)) / float(cont_Registros))
    
    resultadoB = f"Precio medio: {preciomedio:.2f}€" # preciomedio:.2f SIGNIFICA QUE EL VALOR SE VA A MOSTRAR CON 2 DECIMALES
    print(resultadoB) 
    
    return resultadoB
    

#c. CALCULAMOS EL PRODUCTO MÁS VENDIDO, INDICANDO EL NÚMERO DE UNIDADES.
def ProductoMasVendido():
    cont_pos = 0
    pos_final = 0
    unidades_final = 0

    # RECORREMOS TODOS LOS VALORES DE LISTA Unidades_Vendidas
    for unidades in datos["Unidades_Vendidas"]:

        # SI EL VALOR DE UNIDADES ES MAYOR AL MÁXIMO
        if (unidades > unidades_final):

            # ESTA SE CONVIERTE EN EL MÁXIMO
            unidades_final = unidades
            # Y NOS QUEDAMOS CON LA POSICIÓN EN LA QUE SE ENCUENTRA EN EL ARRAY
            pos_final = cont_pos
        # PASAMOS A LA SIGUIENTE POSICIÓN
        cont_pos = cont_pos + 1

    resultadoC = "Producto mas vendido: " + datos["Producto"][pos_final] + " ("+  str(datos["Unidades_Vendidas"][pos_final]) + " unidades)"
    print(resultadoC)
    return resultadoC
    
    
#d. CALCULAMOS EL IMPORTE TOTAL DE VENTAS POR CATEGORÍA, CALCULADO COMO precio * unidades_vendidas
def ImporteTotalVentasPorCategoria():
    recaudacion_categoria = {}
    cont_pos = 0

    # RECORREMOS TODOS LOS VALORES DE LA LISTA Categoria
    for categoria in datos["Categoria"]:
        #COGEMOS DE ESA CATEGORÍA EL PRECIO Y LAS UNIDADES VENDIDAS, Y LAS MULTIPLICAMOS
        precio = datos["Precio"][cont_pos]
        unidades_vendidas = datos["Unidades_Vendidas"][cont_pos]
        total_producto = precio * unidades_vendidas

        # COMPROBAMOS SI ESA CATEGORÍA NO ESTÁ EN recaudacion_categoria
        if categoria not in recaudacion_categoria:
            # SI NO ESTÁ, LA CREAMOS 
            recaudacion_categoria[categoria] = 0
        # SI ESTÁ, LE SUMAMOS EL NUEVO TOTAL
        recaudacion_categoria[categoria] = recaudacion_categoria[categoria] + total_producto
        # AVANZAMOS A LA SIGUIENTE POSICIÓN
        cont_pos = cont_pos + 1

    resultadoD = "Importe total por categoria:\n"
    for cat in recaudacion_categoria:
        resultadoD = resultadoD + (" - " + cat + ": " + str(recaudacion_categoria[cat]) + "€\n")
        
    print(resultadoD)
    
    return recaudacion_categoria, resultadoD


# INICIO DEL PROGRAMA
with open(ruta+ "ventas_tienda.csv", "r") as archivo:
    # LEEMOS EL ARCHIVO
    lector = csv.reader(archivo)
    
    # OMITIMOS LA CABECERA DE LA TABLA PASANDO A LA SIGUIENTE FILA
    next(lector)
    
    # LEEMOS LOS DATOS Y LOS GUARDAMOS EN EL DICCIONARIO
    for fila in lector:
        columnaProducto.append((fila[0]))
        datos["Producto"] = columnaProducto
        
        columnaCategoria.append((fila[1]))
        datos["Categoria"] = columnaCategoria
        
        columnaPrecio.append(float(fila[2]))
        datos["Precio"] = columnaPrecio
        
        columnaUnidades_vendidas.append(int(fila[3]))
        datos["Unidades_Vendidas"] = columnaUnidades_vendidas
        
cont_Registros, resultadoA = NumTotalRegistrosProcesados()
resultadoB = PrecioMedioArticulos()
resultadoC = ProductoMasVendido()
recaudacion_categoria, resultadoD = ImporteTotalVentasPorCategoria()

with open(ruta + "MOJ_Solucion.txt", "w", encoding="utf-8") as f_resumen:
    f_resumen.write("Examen UD1 - Optativa de Programación Python aplicado a la Inteligencia Artificial" + "\n")
    f_resumen.write("Autor/a: Jesús Meléndez Oteros" + "\n")
    f_resumen.write("Fecha: 10/11/2026" + "\n")
    f_resumen.write("Solución" + "\n")
    f_resumen.write("-----------------------------------------------------------------------------------------" + "\n")
    f_resumen.write(resultadoA + "\n")
    f_resumen.write(resultadoB + "\n")
    f_resumen.write(resultadoC + "\n")
    f_resumen.write(resultadoD + "\n")
