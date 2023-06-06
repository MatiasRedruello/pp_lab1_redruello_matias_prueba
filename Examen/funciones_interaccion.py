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
    validacion = True #Puedo usar validacion en sustitucion de flag swap ya que cumple la msima funcion 
    rango_a = len(lista)
   
    # Verifica si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia   
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re) :
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    # Verifica que la categoria este en la lista.
    if validar_que_este_en_la_lista(validacion_re,lista_estadisticas):
        respuesta = LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA
        validacion = False

    # Verifico que se ingrese ascendente o descendente.   
    if not validar_manera_asc_o_desc(manera):
        respuesta = LEYENDA_NO_INGRIESO_ASCENDENTE_O_DESCENDENTE
        validacion = False

    #validar que la herencia para la variable lista lista no sea un str
    if validar_tipo_lista(lista):
        respuesta = LEYENDA_HERENCIA_FUERA_DE_RANGO
        validacion = False 

    #Ordeno la lista
    if validacion:
        categoria = categoria.replace(" ","_")    
        while validacion:
            validacion = False
            rango_a = rango_a - 1
            for indice_a in range(rango_a):
                if manera == "asc" and lista[indice_a]["estadisticas"][categoria] < lista[indice_a+1]["estadisticas"][categoria] \
                    or manera == "desc" and lista[indice_a]["estadisticas"][categoria] > lista[indice_a+1]["estadisticas"][categoria]:
                    aux = lista[indice_a]
                    lista[indice_a] = lista[indice_a+1]
                    lista[indice_a+1] = aux
                    validacion = True
        respuesta = lista
    return respuesta
# print(ordenar(lista_dream_team,"robos totales","asc"))
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
    contador = 1
    mensaje = ""
    validacion = True
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)

    # Verifica si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia   
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re) :
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    # Verifica que la categoria este en la lista.
    if validar_que_este_en_la_lista(validacion_re,lista_estadisticas):
        respuesta = LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA
        validacion = False
        
    #validar que la herencia para la variable lista no sea un str
    if validar_tipo_lista(lista):
        respuesta = LEYENDA_HERENCIA_FUERA_DE_RANGO
        validacion = False        

    if validacion:
        #Primera parte del mensaje
        categoria = categoria.replace(" ","_")   
        for jugador in lista:       
            diccionario[jugador["nombre"]] = jugador["estadisticas"][categoria]
        mensaje = "{}\n".format(categoria)
        mensaje = mensaje + "Puesto | El/Los jugador/es son:\n"
        #Segunda parte del mensaje
        for key,dato in diccionario.items():
            mensaje = mensaje + "  {})     {} | {}.\n".format(contador,key,dato)
            contador += 1                 
        respuesta = mensaje
    return respuesta
# print(mostrar(jugador_mayor_menor_cantidad(lista_dream_team,"robos totales","mayor"),"robos totales"))
def imprimir(dato:str):
    """
    Parametros: 
        Recibe un dato
    funcionalidad: 
        Imprime lo que recibe
    """
    return print(dato)
    
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
def armar_menu_informaivos(lista:list,largo:int)->str:
    """
    Parametros:
        Lista:lista con la que voy a trabajar
        Largo:Recibe el largo de una lista
    funcionalidad:
        Con el indice de la lista itera sobre la lista y arma un menu informativo en relacion a la lista que recibio.
    Retorno: 
        Retorna un mensaje tipo str
    """
    mensaje_final = ""
    if lista is lista_nombres:
        for i in range(largo):
            mensaje_inicial = "{}. {}\n".format(i,lista[i])
            mensaje_final += mensaje_inicial
    else:
        for i in range(largo):
            mensaje_inicial = "* {}\n".format(lista[i])
            mensaje_final += mensaje_inicial        

    return mensaje_final
def imprimir_menu_indices()->str:
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Llama a otra funcion para que arme el menu.
    Retorno: 
         Retorna un mensaje tipo str
    """
    return armar_menu_informaivos(lista_nombres,len(lista_nombres))
         
def imprimir_menu_estadisticas():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Llama a otra funcion para que arme el menu.
    Retorno: 
         Retorna un mensaje tipo str
    """
    return armar_menu_informaivos(lista_estadisticas,len(lista_estadisticas))

def imprimir_menu_estadisticas_dos():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Llama a otra funcion para que arme el menu.
    Retorno: 
         Retorna un mensaje tipo str
    """
    return armar_menu_informaivos(lista_estadisticas,len(lista_estadisticas)-1)

def imprimir_menu_posiciones():
    """
    Parametros:
         No ingresa nada
    funcionalidad:
         Muesta por consola un menu con opciones
    Retorno: 
         No retorna nada
    """
    mensaje_uno = "                        GUIA POR SI DESCONOCE LAS POSICIONES DEL BASQUETBOL\n"
    mensaje_dos ="1 - Base\n2 - Escolta\n3 - Alero\n4 - Ala-Pivot\n5 - Pivot"

  
    return mensaje_uno + mensaje_dos

  

    