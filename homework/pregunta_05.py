"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():

    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    # Diccionario con listas: letra -> [valores de columna 2]
    # valores = {}
    # for letra, numero in [(line[0], int(line[1])) for line in x]:
    #     if letra not in valores:
    #         valores[letra] = []
    #     valores[letra].append(numero)

    # max y min para cada letra
    # resultado = []
    # for letra in sorted(valores.keys()):
    #     resultado.append((letra, max(valores[letra]), min(valores[letra])))

    # return resultado

    extremos = {}
    for letra, numero in [(line[0], int(line[1])) for line in x]:
        if letra not in extremos:
            extremos[letra] = (numero, numero)  # (max, min) inicial
        else:
            max_actual, min_actual = extremos[letra]
            extremos[letra] = (max(max_actual, numero), min(min_actual, numero))

    resultado = sorted((letra, max_min[0], max_min[1]) for letra, max_min in extremos.items())   
    #resultado = [(letra, extremos[letra][0], extremos[letra][1]) for letra in sorted(extremos.keys())]

    return resultado

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
print(pregunta_05())