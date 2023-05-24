import json

def castear_json(ruta)->list:

    lista_json = []
    with open(ruta,"r",encoding="utf-8") as archivo:
       diccionarios = json.load(archivo)
       lista_json = diccionarios["jugadores"]
       
    return lista_json       
lista_deportistas  = castear_json(r"C:\Users\PC\OneDrive\Escritorio\Carpetas\Programar\UTN\1er cuatrimestre\Programacion y Laboratorio\Programacion\Programando con Python\Examen\dt.json")
