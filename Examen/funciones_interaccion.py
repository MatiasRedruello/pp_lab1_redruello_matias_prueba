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
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0: 
                if validacion_re[0] in lista_categoria:
                    categoria = categoria.replace(" ","_")    
                    if re.match(r"^(asc|desc)$",manera,re.IGNORECASE):
                        rango_a = len(lista)
                        flag_swap = True
                        while flag_swap:
                            flag_swap = False
                            rango_a = rango_a - 1
                            for indice_a in range(rango_a):
                                if manera == "asc" and lista[indice_a]["estadisticas"][categoria] < lista[indice_a+1]["estadisticas"][categoria] \
                                    or manera == "desc" and lista[indice_a]["estadisticas"][categoria] > lista[indice_a+1]["estadisticas"][categoria]:
                                    aux = lista[indice_a]
                                    lista[indice_a] = lista[indice_a+1]
                                    lista[indice_a+1] = aux
                                    flag_swap = True
                    else:
                        return errores(-7)
                else:
                    return errores(-5)
            else:
                return errores(-1)
        else:
            return errores(-4)
    else:
        return errores(-1)
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
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0: 
                if validacion_re[0] in lista_categoria:
                    categoria = categoria.replace(" ","_")     
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
                else:
                    return errores(-5) 
            else:
                return errores(-1)  
        else: 
            return errores(-4)
    else:
        return errores(-1)                 

    return mensaje
def imprimir(dato:str):
    """
    Parametros: 
        Recibe un dato
    funcionalidad: 
        Imprime lo que recibe
    """
    print(dato)
    
def imprimir_menu_examen():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Muesta por consola un menu con opciones
    Retorno: 
         No retorna nada
    """
    imprimir("Menú de opciones:")
    imprimir("0. Lista de los jugadores y su posicion")
    imprimir("1. Selecionar un jugador para ver sus caracteristicas")
    imprimir("2. Guardar el jugador en formato csv")
    imprimir("3. Logros del jugador")
    imprimir("4. Promedio de puntos por partido de todo el equipo")
    imprimir("5. Basketball Hall of Fame")
    imprimir("6. Calcular y mostrar")
    imprimir("7. Ingresar un valor y mostrar los jugadores que han promediado mas que ese valor")
    imprimir("8. Promedio de puntos por partido excluyendo al que menos puntos hizo")
    imprimir("9. Jugadores ordenados por posicion en la cancha")
    imprimir("10. Salir del programa")
    
    
def menu_principal_examen()->str:
    """
    Parametros: 
        No ingresa nada
    funcionalidad: 
        Llama a la funcion menu principal y valida que se ingrese opciones nuemricas
        de lo contrario vulve a preguntar y validar.
    Retorno: 
        Retorna la opcion elegida.
    """
    imprimir_menu_examen()  
    opcion_elegida = pregunta("Elija una opcion")
    opcion_validada = re.match(r"([0-9]+)",opcion_elegida)
    while opcion_validada == None:
        opcion_elegida = pregunta("Error las opciones son del 1-9")
        opcion_validada = re.match(r"([0-9]+)",opcion_elegida)
    
    resultado = opcion_elegida

    return resultado 
def imprimir_menu_indices():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Muesta por consola un menu con opciones
    Retorno: 
         No retorna nada
    """
    imprimir("Menú de opciones:")
    imprimir("0. Michael Jordan")
    imprimir("1. Magic Johnson")
    imprimir("2. Larry Bird")
    imprimir("3. Charles Barkley")
    imprimir("4. Scottie Pippen")
    imprimir("5. David Robinson")
    imprimir("6. Patrick Ewing")
    imprimir("7. Karl Malone")
    imprimir("8. John Stockton")
    imprimir("9. Clyde Drexler")
    imprimir("10. Chris Mullin")
    imprimir("11. Christian Laettner")

def imprimir_menu_estadisticas():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Muesta por consola un menu con opciones
    Retorno: 
         No retorna nada
    """
    
    imprimir("Menú de opciones:")
    imprimir("temporadas")
    imprimir("puntos totales")
    imprimir("promedio puntos por partido")
    imprimir("rebotes totales")
    imprimir("promedio rebotes por partido")
    imprimir("asistencias totales")
    imprimir("promedio asistencias por partido")
    imprimir("robos totales")
    imprimir("bloqueos totales")
    imprimir("porcentaje tiros de campo")
    imprimir("porcentaje tiros libres")
    imprimir("porcentaje tiros triples")
    imprimir("logros")

def imprimir_menu_posiciones():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Muesta por consola un menu con opciones
    Retorno: 
         No retorna nada
    """
    imprimir("Guia por si desconose las posiciones\n")
    imprimir("1 - Base")
    imprimir("2 - Escolta")
    imprimir("3 - Alero")
    imprimir("4 - Ala-Pivot")
    imprimir("5 - Pivot")

