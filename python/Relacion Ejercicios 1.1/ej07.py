# ==============================================================================
# EJERCICIO 7: Evaluar notas y promedios de estudiantes
# ==============================================================================

# Definimos una función que recibe un diccionario con alumnos y sus listas de notas.
def evaluar_estudiantes(estudiantes):
    # Recorremos el diccionario usando '.items()':
    # 'estudiante' guardará el nombre (ej: "Ana") y 'notas' la lista de notas (ej: [75, 80, 90]).
    for estudiante, notas in estudiantes.items():
        # Variable para sumar las notas de este estudiante en particular.
        suma_notas = 0
        
        # Bucle para sumar cada nota de la lista del estudiante actual.
        for nota in notas:
            suma_notas += nota
        
        # Calculamos la media dividiendo la suma total entre el número de exámenes:
        # 'len(notas)' nos dice cuántas notas tiene.
        # Añadimos 'if len(notas) > 0 else 0' por seguridad para evitar dividir entre cero si no tuviese notas.
        promedio = suma_notas / len(notas) if len(notas) > 0 else 0

        # Regla de aprobado: si la media es 60 o superior está aprobado; si no, reprobado.
        if promedio >= 60:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        # Imprimimos el informe del estudiante.
        # 'promedio:.2f' formatea el número para mostrar solo 2 decimales (ej: 81.67).
        print(f"Estudiante: {estudiante} | Promedio: {promedio:.2f} | Estado: {estado}")


# Diccionario de prueba:
# Las claves son los nombres de los alumnos y los valores son listas con sus notas.
estudiantes = {
    "Ana": [75, 80, 90],
    "Carlos": [50, 60, 55],
    "Beatriz": [95, 85, 92],
    "David": [40, 58, 62],
    "Elena": [60, 65, 70]
}

# Ejecutamos la función pasándole nuestros datos.
evaluar_estudiantes(estudiantes)
