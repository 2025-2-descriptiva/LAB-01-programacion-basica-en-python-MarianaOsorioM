"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():

    with open("files/input/data.csv", "r") as f:
        filas = f.readlines()

    filas = [linea.strip().split("\t") for linea in filas]

    extremos = {}

    for fila in filas:
        pares = fila[4].split(",")  # columna 5
        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)

            if clave not in extremos:
                extremos[clave] = (valor, valor)  # inicializar (min, max)
            else:
                min_actual, max_actual = extremos[clave]
                extremos[clave] = (min(min_actual, valor), max(max_actual, valor))

    # devolver como lista de tuplas, ordenadas por la clave
    return [(k, v[0], v[1]) for k, v in sorted(extremos.items())]
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
print(pregunta_06())