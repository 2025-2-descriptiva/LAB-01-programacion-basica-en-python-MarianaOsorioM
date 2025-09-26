"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():

    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    suma_por_letra = {}

    for line in x:
        letra = line[0]                     # columna 1
        pares = line[4].split(",")          # columna 5
        suma_valores = sum(int(par.split(":")[1]) for par in pares)

        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

    return dict(sorted(suma_por_letra.items()))


    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
print(pregunta_12())