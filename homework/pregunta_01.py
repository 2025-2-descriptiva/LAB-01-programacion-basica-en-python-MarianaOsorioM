"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():

    with open("files/input/data.csv", "r") as f:
        x = f.readlines()

    # Limpiar y dividir las líneas dentro de la función
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    
    #Sumar la segunda columna
    lista = []
    for line in x:
        lista.append(int(line[1]))
    return sum(lista)

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
print(pregunta_01())
