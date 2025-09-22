"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():

    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
   
   
    asociaciones = {}
    for letra, numero in [(line[0], int(line[1])) for line in x]:
        if numero not in asociaciones:
            asociaciones[numero] = [letra]       # primera vez → lista con la letra
        else:
            asociaciones[numero].append(letra)   # ya existe → agregamos la letra

    # Convertir a lista de tuplas, ordenada por el número
    resultado = sorted(asociaciones.items())

    return resultado
   
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
print(pregunta_07())
