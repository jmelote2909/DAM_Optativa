# ==============================================================================
# EJERCICIO 10: Análisis de métricas de Marketing Digital en Redes Sociales
# ==============================================================================

# Estructura de datos compleja (diccionario anidado):
# Contiene los datos organizados por: Mes -> Red Social -> Métricas clave.
# - 'impresiones': veces que se mostró el anuncio en pantalla.
# - 'clics': personas que hicieron clic en el anuncio.
# - 'conversiones': personas que realizaron una compra o acción tras hacer clic.
datos = {
    "Enero": {
        "Facebook": {"clics": 3400, "impresiones": 150000, "conversiones": 120},
        "Instagram": {"clics": 4100, "impresiones": 170000, "conversiones": 150},
        "Twitter": {"clics": 900, "impresiones": 60000, "conversiones": 45}
    },
    "Febrero": {
        "Facebook": {"clics": 3200, "impresiones": 140000, "conversiones": 110},
        "Instagram": {"clics": 3900, "impresiones": 160000, "conversiones": 140},
        "Twitter": {"clics": 950, "impresiones": 58000, "conversiones": 50}
    },
    "Marzo": {
        "Facebook": {"clics": 3700, "impresiones": 155000, "conversiones": 130},
        "Instagram": {"clics": 4300, "impresiones": 175000, "conversiones": 160},
        "Twitter": {"clics": 1000, "impresiones": 62000, "conversiones": 55}
    }
}

# ------------------------------------------------------------------------------
# 1. Función para calcular el total de conversiones por plataforma
# ------------------------------------------------------------------------------
def calcular_promedio_mesual_coversiones(datos):
    conversiones_totales = {}
    
    # Recorremos cada mes (ej: 'Enero') y su contenido ('plataformas').
    for mes, plataformas in datos.items():
        # Para ese mes, recorremos cada red social y sus métricas.
        for plataforma, datos_plataforma in plataformas.items():
            # Si es la primera vez que vemos esta red social, la inicializamos a 0.
            if plataforma not in conversiones_totales:
                conversiones_totales[plataforma] = 0
            # Le sumamos las conversiones que tuvo en este mes.
            conversiones_totales[plataforma] += datos_plataforma["conversiones"]

    return conversiones_totales

# ------------------------------------------------------------------------------
# 2. Función para calcular el CTR (Click-Through Rate / Efectividad en clics)
# ------------------------------------------------------------------------------
# El CTR mide qué porcentaje de personas que vieron el anuncio hicieron clic en él.
# Fórmula básica: (clics / impresiones) * 100
def calcular_ctr_mensual(datos):
    ctr_totales = {}
    
    for mes, plataformas in datos.items():
        for plataforma, datos_plataforma in plataformas.items():
            if plataforma not in ctr_totales:
                ctr_totales[plataforma] = 0
            # Calculamos el porcentaje de clics del mes y lo acumulamos para luego promediar.
            ctr_totales[plataforma] += (datos_plataforma["clics"] / datos_plataforma["impresiones"]) * 100

    return ctr_totales

# ------------------------------------------------------------------------------
# 3. Función para encontrar la red más eficiente (más conversiones por clic)
# ------------------------------------------------------------------------------
def calcular_mas_clics_por_conversiones(datos):
    totales = {}
    
    # Acumulamos el total de clics y conversiones de los 3 meses para cada red social.
    for mes, plataformas in datos.items():
        for plataforma, datos_plataforma in plataformas.items():
            if plataforma not in totales:
                totales[plataforma] = {
                    "clics": 0,
                    "conversiones": 0
                }
            totales[plataforma]["clics"] += datos_plataforma["clics"]
            totales[plataforma]["conversiones"] += datos_plataforma["conversiones"]

    # Calculamos la tasa de éxito o ratio (conversiones obtenidas entre clics recibidos).
    ratios = {}
    for plataforma in totales:
        ratios[plataforma] = totales[plataforma]["conversiones"] / totales[plataforma]["clics"]

    # 'max(ratios, key=ratios.get)' busca cuál es la clave con el valor numérico más alto.
    return max(ratios, key=ratios.get)

# ------------------------------------------------------------------------------
# 4. Función para descubrir qué mes fue el más exitoso en conversiones
# ------------------------------------------------------------------------------
def calcular_mes_mas_conversiones(datos):
    conversiones_totales = {}
    
    for mes, plataformas in datos.items():
        # Sumamos las conversiones de todas las redes sociales en el mes actual.
        total_conversiones_mes = sum(datos_plataforma["conversiones"] for datos_plataforma in plataformas.values())
        conversiones_totales[mes] = total_conversiones_mes

    # Devolvemos el nombre del mes que tuvo el mayor número total de conversiones.
    return max(conversiones_totales, key=conversiones_totales.get)


# ==============================================================================
# IMPRESIÓN DE RESULTADOS POR CONSOLA
# ==============================================================================

# Mostramos el promedio mensual de conversiones por plataforma (dividiendo el total acumulado entre 3 meses).
print("=== Promedio mensual de conversiones por plataforma ===")
promedio_conversiones = calcular_promedio_mesual_coversiones(datos)
for plataforma, promedio in promedio_conversiones.items():
    print(f"Plataforma: {plataforma} - Promedio de conversiones: {promedio / len(datos)}")

print("\n")

# Mostramos el CTR promedio mensual de cada red social.
print("=== CTR mensual por plataforma ===")
ctr_mensual = calcular_ctr_mensual(datos)
for plataforma, ctr in ctr_mensual.items():
    print(f"Plataforma: {plataforma} - CTR: {ctr / len(datos):.2f}%")

print("\n")

# Mostramos cuál fue la plataforma con mejor rendimiento de conversión.
print("=== Plataforma con más clics ===")
plataforma_mas_clics = calcular_mas_clics_por_conversiones(datos)
print(f"Plataforma: {plataforma_mas_clics}")

print("\n")

# Mostramos cuál fue el mes más productivo.
print("=== Mes con más conversiones ===")
plataforma_mas_conversiones = calcular_mes_mas_conversiones(datos)
print(f"Mes: {plataforma_mas_conversiones}")
