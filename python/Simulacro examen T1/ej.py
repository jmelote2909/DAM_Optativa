import csv

ruta = "Simulacro examen T1/reservas_viajes.csv"

columnaDestino = []
columnaProducto = []
columnaPrecio = []
columnaUnidades = []
datos = {
    "Destino": {},
    "Producto": {},
    "Precio": {},
    "Unidades_reservadas":{}
}

with open(ruta, "r") as archivo:
    lector = csv.reader(archivo)

    next(lector)

    # LECTURA DE DATOS Y GUARDADO EN DICCIONARIO
    for fila in lector:
        columnaDestino.append((fila[0]))
        datos["Destino"] = columnaDestino
        columnaProducto.append((fila[1]))
        datos["Producto"] = columnaProducto
        columnaPrecio.append((fila[2]))
        datos["Precio"] = columnaPrecio
        columnaUnidades.append((fila[3]))
        datos["Unidades_reservadas"] = columnaUnidades

    # CALCULO DE Número total de registros procesados
    cont_Registros = 0
    for destino in datos["Destino"]:
        cont_Registros = cont_Registros + 1 

    # CALCULO DE Precio medio de todos los paquetes/productos ofertados.
    cont_Precio = 0
    for precio in datos["Precio"]:
        cont_Precio = cont_Precio + float(precio)

    # CALCULO DE El destino o producto más reservado, indicando el número total de unidades reservadas.
    cont_reserva1 = 0
    cont_reserva_final = 0
    cantMax_Reservas = 0
    
    for unidades in datos["Unidades_reservadas"]:
        
        if (int(unidades) > int(cantMax_Reservas)):
            cont_reserva_final = cont_reserva1
            cantMax_Reservas = unidades
        cont_reserva1 = cont_reserva1 + 1
            
    destino_max_reservas = datos["Producto"][cont_reserva_final]
    
    #CALCULO DE LA Facturación total por tipo de producto:
    facturacion_producto = {}
    pos = 0

    for producto in datos["Producto"]:
        precio = float(datos["Precio"][pos])
        unidades = int(datos["Unidades_reservadas"][pos])
        total_reserva = precio * unidades

        if producto not in facturacion_producto:
            facturacion_producto[producto] = 0

        facturacion_producto[producto] = facturacion_producto[producto] + total_reserva
        pos = pos + 1

    
    
print(datos)
print("Numero total de registros:", cont_Registros)
print("Precio medio de la oferta:", cont_Precio/cont_Registros)
print("Producto/Reserva más vendido/a:", destino_max_reservas, "(",cantMax_Reservas, "unidades)")
print("Facturación total por tipo de producto:")
for prod in facturacion_producto:
    print(" -", prod, ":", facturacion_producto[prod], '€')