"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    
    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    # Diccionario para contar apariciones de claves en columna 5
    conteo = {}
    for line in x:
        pares = line[4].split(",")        # columna 5
        for par in pares:
            clave, _ = par.split(":")     # devuelve lo que está antes y después de ":"
            conteo[clave] = conteo.get(clave, 0) + 1

    return dict(sorted(conteo.items()))
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
print(pregunta_09())