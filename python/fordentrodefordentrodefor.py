# ==============================================================================
# EJEMPLO: "FOR DENTRO DE FOR DENTRO DE FOR" - EL CASO DE LA BIBLIOTECA
# ==============================================================================
# ¡Hola, Rubén!
# Si alguna vez te has liado con los bucles anidados (un 'for' metido dentro
# de otro 'for'), no te preocupes: es el concepto donde casi todo el mundo se atasca.
#
# LA ANALOGÍA DEL RELOJ:
# Piensa en las agujas de un reloj:
# 1. Bucle exterior (las HORAS): se mueve muy despacio.
# 2. Bucle del medio (los MINUTOS): da una vuelta entera antes de que la hora avance 1.
# 3. Bucle interior (los SEGUNDOS): da 60 vueltas completas antes de que el minuto avance 1.
#
# EN NUESTRA BIBLIOTECA:
# - Bucle 1 (Exterior)   --> Recorre las PLANTAS del edificio.
# - Bucle 2 (Medio)      --> En cada planta, recorre las ESTANTERÍAS.
# - Bucle 3 (Interior)   --> En cada estantería, saca los LIBROS uno a uno.
# - Bucle 4 (Detalle)    --> Para cada libro, lee sus DATOS (título, páginas, estado).
# ==============================================================================

# 1. LA ESTRUCTURA DE DATOS DE LA BIBLIOTECA
# ------------------------------------------------------------------------------
# Fíjate en cómo encajan las cajas dentro de otras cajas (como muñecas rusas / Matrioskas):
biblioteca = {
    "Planta 1 - Ficción": {
        "Estantería Fantasía": [
            {"titulo": "El Señor de los Anillos", "paginas": 1200, "prestado": False},
            {"titulo": "Harry Potter y el Cáliz", "paginas": 650, "prestado": True},
            {"titulo": "El Nombre del Viento", "paginas": 880, "prestado": False}
        ],
        "Estantería Ciencia Ficción": [
            {"titulo": "Dune", "paginas": 700, "prestado": False},
            {"titulo": "Fundación", "paginas": 350, "prestado": True}
        ]
    },
    "Planta 2 - Ciencias y Cómics": {
        "Estantería Manga y Cómic": [
            {"titulo": "Dragon Ball Vol. 1", "paginas": 190, "prestado": False},
            {"titulo": "Spider-Man: Blue", "paginas": 160, "prestado": False}
        ],
        "Estantería Informática": [
            {"titulo": "Aprende Python en 3 Días", "paginas": 280, "prestado": False},
            {"titulo": "Bases de Datos Avanzadas", "paginas": 520, "prestado": True}
        ]
    }
}

# Variables acumuladoras para hacer estadísticas de toda la biblioteca:
total_libros = 0
total_prestados = 0
total_paginas = 0


print("=" * 70)
print("     INSPECCIÓN DE LA BIBLIOTECA PASO A PASO (BUCLES ANIDADOS)     ")
print("=" * 70)


# ==============================================================================
# NIVEL 1 (EL BUCLE DE FUERA): Recorremos cada PLANTA de la biblioteca
# ==============================================================================
# Aquí 'planta' será "Planta 1 - Ficción", luego en la siguiente vuelta "Planta 2..."
for planta, estanterias in biblioteca.items():
    print(f"\n🚪 [NIVEL 1] ENTRANDO A: {planta}")
    print("-" * 50)

    # ==========================================================================
    # NIVEL 2 (EL BUCLE DEL MEDIO): Recorremos las ESTANTERÍAS de esta planta
    # ==========================================================================
    # Por cada planta, revisamos sus estanterías una a una.
    for estanteria, lista_libros in estanterias.items():
        print(f"  📚 [NIVEL 2] Revisando la '{estanteria}'...")

        # ======================================================================
        # NIVEL 3 (EL BUCLE INTERIOR): Recorremos los LIBROS de esta estantería
        # ======================================================================
        # Por cada estantería, agarramos cada libro de la lista.
        for libro in lista_libros:
            total_libros = total_libros + 1
            total_paginas = total_paginas + libro["paginas"]

            # Comprobamos si el libro está prestado o en la estantería:
            if libro["prestado"] == True:
                estado = "🔴 PRESTADO"
                total_prestados = total_prestados + 1
            else:
                estado = "🟢 DISPONIBLE"

            print(f"    📖 [NIVEL 3] Libro: '{libro['titulo']}' ({libro['paginas']} págs) -> {estado}")

            # ==================================================================
            # NIVEL 4 (OPCIONAL): Leer cada ficha/campo individual del libro
            # ==================================================================
            # Esto es un 4º for para inspeccionar los datos internos del libro:
            # for campo, valor in libro.items():
            #     print(f"        -> {campo}: {valor}")


# ==============================================================================
# RESUMEN FINAL TRAS TERMINAR TODOS LOS BUCLES
# ==============================================================================
disponibles = total_libros - total_prestados

print("\n" + "=" * 70)
print("                    RESUMEN GENERAL DEL INVENTARIO                    ")
print("=" * 70)
print(f"Total de libros encontrados en la biblioteca: {total_libros}")
print(f"Libros actualmente prestados:                 {total_prestados}")
print(f"Libros disponibles para leer:                 {disponibles}")
print(f"Suma total de páginas de todos los libros:    {total_paginas} páginas")
print(f"Grosor medio por libro:                       {total_paginas / total_libros:.1f} páginas/libro")
print("=" * 70)

