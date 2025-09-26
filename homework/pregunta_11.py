"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
 
    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    suma_por_letra = {}

    for line in x:
        numero = int(line[1])           # columna 2
        letras = line[3].split(",")     # columna 4

        for letra in letras:
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + numero

    return dict(sorted(suma_por_letra.items()))

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """

print(pregunta_11())
