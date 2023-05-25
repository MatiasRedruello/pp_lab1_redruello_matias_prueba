import json
def castear_json(ruta)->list:
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
lista_dream_team  = castear_json(r"C:\Users\PC\OneDrive\Escritorio\Carpetas\Programar\UTN\1er cuatrimestre\Programacion y Laboratorio\Programacion\Programando con Python\Examen\dt.json")
