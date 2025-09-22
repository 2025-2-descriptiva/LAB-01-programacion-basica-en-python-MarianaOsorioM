"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    
    with open("files\input\data.csv", "r") as f:
        x = f.readlines()

    # Limpiar y dividir las líneas dentro de la función
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    #Lista con la primera columna
    list_1 = [line[0] for line in x] 
    
    #list_1 = []
    #for line in x:
    #    list_1.append(line[0])

    resultado = []
    for letra in sorted(set(list_1)):   # recorrer letras únicas, ordenadas
        resultado.append((letra, list_1.count(letra)))

    return resultado
        
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

print(pregunta_02())