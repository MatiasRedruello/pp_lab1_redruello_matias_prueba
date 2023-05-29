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

def ordenar(lista:list,categoria:str,manera:str)->list:
    """
    Parametros:
        Lista: Lista de diccionarios con los datos de los jugadores.
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
        Manera: Es un str que indica como lo quiero ordenar ascendente(asc) o descendente(desc)
    Funcionamiento: 
        A partir de la estadistica deseada y la lista se ordenan los diccionarios de forma ascendente o descendente.
    Retorna: 
        Una lista de diccionarios ordenada
    """
    rango_a = len(lista)
    flag_swap = True
    while flag_swap:
        flag_swap = False
        rango_a = rango_a - 1
        for indice_a in range(rango_a):
            if manera == "desc" and lista[indice_a]["estadisticas"][categoria] < lista[indice_a+1]["estadisticas"][categoria] \
                or manera == "asc" and lista[indice_a]["estadisticas"][categoria] > lista[indice_a+1]["estadisticas"][categoria]:
                aux = lista[indice_a]
                lista[indice_a] = lista[indice_a+1]
                lista[indice_a+1] = aux
                flag_swap = True
    return lista

def mostrar(lista:list,categoria:str)->str:
    """
    Parametros:
        Lista: La lista de diccionario/os con los datos d elos jugadores 
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
    Funcionamiento: 
        Itero sobre la lista y creo un diccionario que contenga como key el nombre y como clave valor
          numerico de categoria deseada.
        Armo un mensaje que tiene el Top del/los jugador/es, nombre y valor numerico
    Retorna: 
        Un mensjae que tiene un str
    """
    diccionario = {}
    mensaje = ""
    for i in range(len(lista)):
        if categoria in lista[i]:
            for jugador in lista:       
                diccionario[jugador["nombre"]] = jugador[categoria]
            for key,dato in diccionario.items():
                mensaje = "{}:\n".format(key)
                for texto in dato:
                    mensaje = mensaje +  "               ° {}\n".format(texto)             
        else:      
            for jugador in lista:       
                diccionario[jugador["nombre"]] = jugador["estadisticas"][categoria]
            mensaje = "{}\n".format(categoria)
            mensaje = mensaje + "Puesto | Los jugadores son:\n"

            contador = 1
            for key,dato in diccionario.items():
                mensaje = mensaje + "  {})     {} | {}.\n".format(contador,key,dato)
                contador += 1

    return mensaje
# print(mostrar(jugador_mayor_menor_cantidad(lista_dream_team,"logros","mayor"),"logros"))
# print(mostrar(ordenar(buscar_y_comparar(lista_dream_team,"porcentaje_tiros_de_campo",51.5),"porcentaje_tiros_de_campo","asc"),"porcentaje_tiros_de_campo"))
# print(mostrar(jugador_mayor_menor_cantidad(lista_dream_team,"temporadas","mayor"),"temporadas"))
def imprimir(dato:str):
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
    imprimir("Menú de opciones:")
    imprimir("1. Lista de los jugadores y su posicion")
    imprimir("2. Selecionar un jugador apra ver sus caracteristicas")
    imprimir("3. Ordenar los heroes por fuerza")
    imprimir("4. Promedio heroes")
    imprimir("5. Inteligencia de los Heroes")
    imprimir("6. Salir del programa")
    
    
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

