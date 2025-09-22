"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():

    with open("files\input\data.csv", "r") as f:
        x = f.readlines()
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]

    list_meses = [z[2].split("-")[1] for z in x] 

    #resultado = []
    #for mes in sorted(set(list_meses)):   # recorrer los meses únicos, ordenados
    #    resultado.append((mes, list_meses.count(mes)))
    #return resultado

    conteo_meses = {}
    for mes in list_meses:
        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1 
        #si no existe la letra en el diccionario, devuelve 0. Si si, devuelve su valor actual + 1
       
    # Ordenar y devolver como lista de tuplas
    return sorted(conteo_meses.items())
    

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
print(pregunta_04())