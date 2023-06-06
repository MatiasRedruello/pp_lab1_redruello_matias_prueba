import json
def abrir_json(ruta)->list:
    """
    Parametros:
        Ruta: recibo la ruta del archivo json
    Funcionamiento:
        Mediante el controlador de contexto y el metodo load cargo la lista de diccionarios en una variable lista
    Retorno:Una lista de diccionarios
    """

    lista_json = []
    with open(ruta,"r",encoding="utf-8") as archivo:
       diccionarios = json.load(archivo)
       lista_json = diccionarios["jugadores"]  
    return lista_json       
lista_dream_team  = abrir_json(r"C:\Users\PC\OneDrive\Escritorio\Carpetas\Programar\UTN\1er cuatrimestre\Programacion y Laboratorio\Programacion\Programando con Python\Examen\dt.json")
                              
def guardar_nombres(lista:list)->list:
    """
    Parametros:
        lista: lista donde esta toda la informacion del Dream Team
    Funcionamiento:
        Busca en el diccionario nombre y  separo los nombres
    Retorno:
        Lista de nombres
    """
    lista_vacia = []

    for jugadores in lista:
        for clave,dato in jugadores.items():
            if clave == "nombre": 
                lista_vacia.append(dato)

    return lista_vacia
lista_nombres = guardar_nombres(lista_dream_team)
def guardar_estadisticas(lista:list)->list:
    """
    Parametros:
        lista: lista donde esta toda la informacion del Dream Team
    Funcionamiento:
        Busca el diccionario nombre y lo separo en una nueva lista 
    Retorno:
        Lista de nombres
    """
    lista_vacia = []

    for clave in lista[0]["estadisticas"].keys():
            lista_vacia.append(clave)

    palabras =",".join(lista_vacia)
    palabras = palabras.replace("_"," ")
    lista_vacia = palabras.split(",")
    lista_vacia.append("logros")

    return lista_vacia
lista_estadisticas = guardar_estadisticas(lista_dream_team)





