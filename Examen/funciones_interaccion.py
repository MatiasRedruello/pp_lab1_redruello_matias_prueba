from funciones_calculos import *
import re
def pregunta(texto:str)->str:
    """
    Parametros: recive un cadena de texto la cual va  a ser la leyenda de la pregunta
    Funcionamiento: recibe un dato por input
    Retorna:la respuesta
    """
    respuesta = input(texto)
    return respuesta

def exportar_csv(archivo_nombre:str,lista:str)->None:
    if len(lista) > 0:
        with open(archivo_nombre,"w") as archivo:
            lista_str = ",".join(lista)          
            archivo.write(lista_str)
    else:
        print("Error no se ingreso una lista")

def imprimir_dato(dato:str):
    """
    Parametros: recibe un dato
    funcionalidad: imprime lo que recibe
    """
    print(dato)
    
def imprimir_menu_examen():
    """
    ingresa un dato
    muesta por consola ese dato
    """
    imprimir_dato("Menú de opciones:")
    imprimir_dato("1. Lista de los jugadores y su posicion")
    imprimir_dato("2. Selecionar un jugador apra ver sus caracteristicas")
    imprimir_dato("3. Ordenar los heroes por fuerza")
    imprimir_dato("4. Promedio heroes")
    imprimir_dato("5. Inteligencia de los Heroes")
    imprimir_dato("6. Salir del programa")
    
    
def menu_principal_examen():
        imprimir_menu_examen()  
         # Mostrar menú de opciones
        opcion_elegida = pregunta("Elija una opcion")
        opcion_validada = re.match(r"([1-6])",opcion_elegida)
        while opcion_validada == None:
            opcion_elegida = pregunta("Error las opciones son del 1-6")
            opcion_validada = re.match(r"([1-6])",opcion_elegida)
        
        resultado = opcion_elegida
    
        return resultado 