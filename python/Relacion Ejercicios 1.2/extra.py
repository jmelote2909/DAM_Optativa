# ==============================================================================
# EJERCICIO EXTRA: Análisis completo de Marketing Digital leyendo desde un archivo
# ==============================================================================
# En el Ejercicio 10 teníamos los datos escritos directamente en el código ("a mano").
# En este ejercicio extra, el código se vuelve PROFESIONAL:
# 1. Lee los datos reales desde un archivo externo ('datos_marketing.txt').
# 2. Los transforma en un diccionario estructurado (Mes -> Plataforma -> Métricas).
# 3. Utiliza funciones especializadas para calcular conversiones, CTR, mejor ratio y mejor mes.
# 4. Presenta un informe limpio en la terminal.

import os

# Comprobamos dónde se encuentra el archivo para que funcione tanto si ejecutas
# desde la carpeta raíz como desde dentro de 'Relacion Ejercicios 1.2'.
RUTA_DATOS = (
    "Relacion Ejercicios 1.2/datos_marketing.txt"
    if os.path.exists("Relacion Ejercicios 1.2/datos_marketing.txt")
    else "datos_marketing.txt"
)


# ------------------------------------------------------------------------------
# 1. FUNCIÓN PARA CARGAR Y ESTRUCTURAR LOS DATOS DESDE EL FICHERO
# ------------------------------------------------------------------------------
def cargar_datos(ruta_archivo: str) -> dict:
    """Lee el archivo de texto y devuelve el diccionario estructurado por mes y plataforma."""
    datos = {}

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        # '.readlines()' nos entrega una lista con todas las líneas del archivo.
        lineas = f.readlines()

    # 'lineas[1:]' significa: empieza en la línea 1 y omite la línea 0 (el encabezado: mes,plataforma,...).
    for linea in lineas[1:]:
        linea = linea.strip()
        # Si hay una línea vacía, la saltamos.
        if not linea:
            continue

        # Desempaquetamos los 5 valores de cada fila separados por coma:
        # Ejemplo: "Enero,Facebook,3400,150000,120"
        mes, plataforma, clics, impresiones, conversiones = linea.split(",")

        # Si el mes (ej: "Enero") no está todavía en el diccionario principal, lo creamos vacío.
        if mes not in datos:
            datos[mes] = {}

        # Dentro del mes, guardamos la plataforma con sus números convertidos a enteros (int).
        datos[mes][plataforma] = {
            "clics": int(clics),
            "impresiones": int(impresiones),
            "conversiones": int(conversiones),
        }

    return datos


# ------------------------------------------------------------------------------
# 2. FUNCIÓN: PROMEDIO MENSUAL DE CONVERSIONES POR RED SOCIAL
# ------------------------------------------------------------------------------
def calcular_promedio_mensual_conversiones(datos: dict) -> dict:
    """Calcula el promedio de conversiones mensuales para cada plataforma."""
    total_meses = len(datos)  # Cuántos meses tenemos en total (ej: 3)
    conversiones_totales = {}

    # 'datos.values()' nos da los diccionarios de cada mes.
    for plataformas in datos.values():
        for plataforma, metricas in plataformas.items():
            # '.get(plataforma, 0)' devuelve el valor actual o 0 si aún no existía en el acumulador.
            conversiones_totales[plataforma] = conversiones_totales.get(plataforma, 0) + metricas["conversiones"]

    # Dividimos el total acumulado entre el número de meses para obtener el promedio.
    return {plataforma: total / total_meses for plataforma, total in conversiones_totales.items()}


# ------------------------------------------------------------------------------
# 3. FUNCIÓN: CTR (PORCENTAJE DE EFECTIVIDAD EN CLICS) PROMEDIO
# ------------------------------------------------------------------------------
def calcular_ctr_promedio(datos: dict) -> dict:
    """Calcula el CTR (Click-Through Rate) mensual promedio para cada plataforma."""
    total_meses = len(datos)
    ctr_acumulado = {}

    for plataformas in datos.values():
        for plataforma, metricas in plataformas.items():
            # CTR mensual = (clics conseguidos / veces que se vio el anuncio) * 100
            ctr_mes = (metricas["clics"] / metricas["impresiones"]) * 100
            ctr_acumulado[plataforma] = ctr_acumulado.get(plataforma, 0.0) + ctr_mes

    # Promediamos el CTR entre los meses registrados.
    return {plataforma: total_ctr / total_meses for plataforma, total_ctr in ctr_acumulado.items()}


# ------------------------------------------------------------------------------
# 4. FUNCIÓN: PLATAFORMA MÁS EFICIENTE (MÁS CONVERSIONES POR CADA CLIC)
# ------------------------------------------------------------------------------
def calcular_mas_clics_por_conversiones(datos: dict) -> str:
    """Determina la plataforma con mayor ratio de conversiones por clic."""
    totales = {}

    # Acumulamos clics y conversiones globales por plataforma a lo largo de todo el periodo.
    for plataformas in datos.values():
        for plataforma, metricas in plataformas.items():
            if plataforma not in totales:
                totales[plataforma] = {"clics": 0, "conversiones": 0}
            totales[plataforma]["clics"] += metricas["clics"]
            totales[plataforma]["conversiones"] += metricas["conversiones"]

    # Calculamos la tasa de éxito (conversiones conseguidas / clics recibidos).
    ratios = {
        plataforma: valores["conversiones"] / valores["clics"]
        for plataforma, valores in totales.items()
    }

    # 'max(..., key=ratios.get)' encuentra la plataforma con la tasa más alta.
    return max(ratios, key=ratios.get)


# ------------------------------------------------------------------------------
# 5. FUNCIÓN: MES CON MAYOR VOLUMEN TOTAL DE CONVERSIONES
# ------------------------------------------------------------------------------
def calcular_mes_mas_conversiones(datos: dict) -> str:
    """Determina el mes con mayor volumen total de conversiones."""
    # Para cada mes, sumamos las conversiones de todas las redes sociales que participaron.
    conversiones_por_mes = {
        mes: sum(metricas["conversiones"] for metricas in plataformas.values())
        for mes, plataformas in datos.items()
    }

    # Devolvemos el mes con la puntuación más alta.
    return max(conversiones_por_mes, key=conversiones_por_mes.get)


# ------------------------------------------------------------------------------
# 6. FUNCIÓN DE PRESENTACIÓN DE RESULTADOS
# ------------------------------------------------------------------------------
def mostrar_resultados(datos: dict) -> None:
    """Muestra los resultados con un formato limpio en la consola."""
    print("=== Promedio mensual de conversiones por plataforma ===")
    promedio_conversiones = calcular_promedio_mensual_conversiones(datos)
    for plataforma, promedio in promedio_conversiones.items():
        print(f"Plataforma: {plataforma} - Promedio de conversiones: {promedio}")

    print("\n")

    print("=== CTR mensual por plataforma ===")
    ctr_mensual = calcular_ctr_promedio(datos)
    for plataforma, ctr in ctr_mensual.items():
        print(f"Plataforma: {plataforma} - CTR: {ctr:.2f}%")

    print("\n")

    print("=== Plataforma con más conversiones por clic ===")
    plataforma_mas_clics = calcular_mas_clics_por_conversiones(datos)
    print(f"Plataforma: {plataforma_mas_clics}")

    print("\n")

    print("=== Mes con más conversiones ===")
    mes_mas_conversiones = calcular_mes_mas_conversiones(datos)
    print(f"Mes: {mes_mas_conversiones}")


# ------------------------------------------------------------------------------
# PUNTO DE ENTRADA PRINCIPAL (MAIN)
# ------------------------------------------------------------------------------
def main():
    # Paso A: Cargar los datos desde el archivo.
    datos = cargar_datos(RUTA_DATOS)
    # Paso B: Procesar y mostrar el análisis completo.
    mostrar_resultados(datos)


# 'if __name__ == "__main__":' asegura que este código solo se ejecute cuando
# abres este archivo directamente, y no si otro programa lo importa como librería.
if __name__ == "__main__":
    main()
