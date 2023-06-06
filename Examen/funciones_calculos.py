from funciones_base import *
from validaciones import *
import re

lista_nada = []
"1)"
def lista_jugador_posicion(lista:list)->str:
    """
    Parametros:
        lista: Contine  la informacion del Dream Team
    Funcionamiento:
        Busca el nombre y la posicion de juego del jugador y la muestra con el formato (Nombre Jugador - Posición)
    Retorno:
        un string con el nombre y la posicion de cada jugador
    """
    formato_final = ""

    # Verificar si la lista está vacía
    if validar_lista_vacia(lista):  
        return print(LEYENDA_LISTA_VACIA)
    
    
    for jugadores in lista :
        formato_inicial = "{0} - {1}\n".format(jugadores["nombre"],jugadores["posicion"]) 
        formato_final += formato_inicial

    return formato_final
# lista_jugador_posicion(lista_dream_team)

"2)"
lista_vacia = []
def estadisticas_jugadores(lista:list,indice:int)->list:
    """
    Parametros:
        Lista:lista donde esta toda la informacion del Dream Team
        Indice: Es un numero entregado por el usuario con el fin de elegir un jugador
    Funcionamiento:
        Creo una lista y guardo el nombre y las estadisticas de un jugador dado.
        Por otro lado creo un mensaje con lamisma informacion y lo muestro por pantalla
    Retorno:
        Una lista con el jugador que se busca y sus estadisticas o el tipo de error
    """
    mensaje_nombre = ""
    mensaje_final = ""
    lista_jugadores = []
    validacion = True 

    # Verificar si la lista está vacía
    if validar_lista_vacia(lista):  
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    # Validar el valor ingresado por el usuario
    if not validar_indice(indice, lista):
        respuesta = LEYENDA_INDICE
        validacion = False

    # guarda en una lista los nombres de los jugadores y las estadisticas
    if validacion:
        for i in range(len(lista)):
            if i == int(indice):
                lista_jugadores.append(lista[i]["nombre"])
                lista_jugadores.append(lista[i]["estadisticas"])

                # crea mensaje con nombre y estadisticas
                mensaje_nombre = "{}: {}\n".format("nombre",lista[i]["nombre"])
                for datos in lista[i]["estadisticas"]:
                    mensaje = "{}: {}\n"
                    mensaje = mensaje.format(datos,lista[i]["estadisticas"][datos])
                    mensaje_final = mensaje_final + mensaje

        mensaje_final = mensaje_nombre + mensaje_final  
        print(mensaje_final)
        # Si retorno el mensaje final en vez de la lista,rompo el punto 3
    respuesta = lista_jugadores

    return respuesta
       
  
# print(estadisticas_jugador(lista_dream_team,"dos") )     
"3)"
def crear_csv(lista:list)->None:
    """
    Parametros:
        Lista: Esta lista proviene particularmente del punto dos y tiene dos elemen-
        tos, un str y un diccionario.
    Funcionamiento:
        Guardo el str en una variable para darle nombre al archivo y guardo en
        una lista auxiliar las claves de los diccionarios y los valores.
        Luego a traves de metodo join y la lista aux armo el str que se va a guardar en el  archivo csv
    Retorno: None a menos que haya un error  
    """

    nombre_archivo = "{0}.csv".format(lista[0])
    diccionario = lista[1]
    lista_aux = []
    validacion = True
    # Verificar si la lista está vacía
    if validar_lista_vacia(lista):  
        respuesta = LEYENDA_LISTA_VACIA

    if validacion:     
        # Armo una lista auxiliar para posteriormente evitar que me quede la coma al final,usando join formo el str sin la ultima coma.
        for datos in diccionario:
            lista_aux.append(datos)
            lista_aux.append(str(diccionario[datos]))            
        with open(nombre_archivo,"w") as archivo:          
            archivo.write(",".join(lista_aux))
            respuesta = "El archivo fue creado corectamente"
    return respuesta
# crear_csv(estadisticas_jugador(lista_dream_team,0))
"4)"
def logros_jugador(lista:list,texto:str)->str:
    """
    Parametros:
        Lista: Lista con los datos de los jugadores.
        Texto: El jugador a buscar.
    Funcionamiento: 
        Comparo el nombre que me ingresa con los de la lista, busco sus logros y los guardo en una variable
        mensaje junto con el nombre y luego lo muestro por pantalla con un formato en particular.
    Retorna: 
        Mensaje final o el tipo de error
    """

    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})",texto)#opcionalmente toma el espacio o el apellido del jugador para que no rompa
    mensaje_nombre = ""
    mensaje_final = ""
    validacion = True

    # Verificar si alguna lista esta vacia/findall devuelve una lista,si no encuentra nada la devuelve vacia
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re) :
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    #  Verificar que el nombre ingresado se el de uno de los jugadores
    if validar_que_este_en_la_lista(validacion_re,lista_nombres):
        respuesta = LEYENDA_NOMBRE_FUERA_DE_LA_LISTA
        validacion = False        

    if validacion:
        for jugadores in lista:
            if jugadores["nombre"] == texto: 
                # Armo el formato
                mensaje_1 = "{}: {}\n".format("nombre",jugadores["nombre"])
                mensaje_2 = "{}:\n".format("logros")
                mensaje_nombre = mensaje_1 + mensaje_2
                for texto in jugadores["logros"]:
                    mensaje = "      ° {}\n".format(texto)
                    mensaje_final = mensaje_final + mensaje
        mensaje_final = mensaje_nombre + mensaje_final
        respuesta = mensaje_final            

    return respuesta    
# print(logros_jugador(lista_dream_team,"Michael Jordan"))
"7,8,9,13,14,16,17,19)"
def jugador_mas_menos_haya_logrado(lista:list,categoria:str,mayor_o_menor:str)->list:
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
        Mayor o Menor: Es un str que indica si se quiere buscar el mayor o el menor.
    Funcionamiento: 
        A partir de la estadistica deseada o la cantidad de logros alcanzados se busca el jugador que mas/menos haya conseguido para esa estadistica/logro.
        Guardo el indice del jugador, el mismo lo uso para guardar el diccionario en una lista y armar una lista de diccionarios.
    Retorna: 
        Una lista con el diccionario del jugador o el tipo de error
    """
    mayor_cantidad = 0
    indice_guardado = 0
    lista_final = []
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [_a-zA-Z]+){0,3})$",categoria)#opcionalmente toma el espacio o el apellido del jugador para que no rompa
    categoria = categoria.replace(" ","_")#Necesario para poder comparar con las key de estadisticas
    validacion = True

    # Verificar si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False 
    
    # Verifica que la estadistica este en la lista
    if validar_que_este_en_la_lista(validacion_re,lista_estadisticas):
        respuesta = LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA
        validacion = False

    # Verifico que se ingrese mayor o menor   
    if re.match(r"^(mayor|menor)$",mayor_o_menor,re.IGNORECASE) == None:
        respuesta = LEYENDA_NO_INGRIESO_MAYOR_O_MENOR
        validacion = False

    if validacion:
        for i in range(len(lista)):
            #Busca el indice del que mas o menos logros tenga
            for claves in lista[i]:
                if claves  == categoria:
                    if i == 0 or mayor_o_menor == "mayor" and  mayor_cantidad < len(lista[i]["logros"]) \
                        or  mayor_o_menor == "menor" and  mayor_cantidad > len(lista[i]["logros"]):                    
                        mayor_cantidad = len(lista[i]["logros"])
                        indice_guardado = i                   
                else:
                #Busca el indice del que mas o menos estadisticas tenga
                    for clave,dato in lista[i]["estadisticas"].items():
                        if clave == categoria:
                            if i == 0 or  mayor_o_menor == "mayor" and  mayor_cantidad < dato \
                                or  mayor_o_menor == "menor" and  mayor_cantidad > dato:                       
                                mayor_cantidad = dato
                                indice_guardado = i
        #Guardo en una lista el jugador que le corresponde dicho indice
        lista_final.append(lista[indice_guardado])
        respuesta = lista_final
    return respuesta
# print(jugador_mayor_menor_cantidad(lista_dream_team,"porcentaje tiros libres","menor"))
"5,10,11,12,15,18)"
def buscar_y_guarda(lista:list,categoria:str,valor:int)->list:
    """
    Paramtros: 
        Lista:lista con los datos de los jugadores.
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
        Valor: Dato numerico ingresado por el usuario
    Funcionamiento: 
        A partir del valor ingresado por el usuario busco y guardo los diccionarios de los jugadores que esten 
        por arriba o debajo del valor ingresado.
    Retorno: 
        Una lista de diccionarios.
    """
    lista_jugadores_arriba_valor_ingresado = []
    validacion_re = re.findall(r"^([_a-zA-Z]+(?: [_a-zA-Z]+){0,3})$",categoria)
    valor_techo = jugador_mas_menos_haya_logrado(lista_dream_team,categoria,"mayor")# lo uso como techo de rango
    categoria_modificada = categoria.replace(" ","_") 
    validacion = True

    # Verifica si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia   
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    # Verifica que la estadistica este en la lista 
    if validar_que_este_en_la_lista(validacion_re,lista_estadisticas):
        respuesta = LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA
        validacion = False

    # Verifica que el valor ingresado no este por devajo de cero o que no supere el valor maximo en los registros.
    # Usanado la funcion jugador jugador_mayor_menor_cantidad busco el puntaje maximo en esa categoria y los uso de techo.
    for indice_del_rango in range(len(valor_techo)):
        if float(valor) > valor_techo[indice_del_rango]["estadisticas"][categoria_modificada] or  float(valor) < 0:
            respuesta = LEYENDA_FUERA_DE_RANGO
            validacion = False     

    # Guardo la lista
    if validacion:
        valor = str(valor)
        if re.match(r"^[.0-9]+$",valor):
            valor = float(valor) 
            for i in range(len(lista)):         
                if  lista[i]["estadisticas"][categoria_modificada] > valor: 
                    lista_jugadores_arriba_valor_ingresado.append(lista[i])
            respuesta = lista_jugadores_arriba_valor_ingresado
    
    return respuesta
# print(buscar_y_guarda(lista_dream_team,"puntos totales","0"))
"6)"
def salon_de_la_fama(lista:list,jugador:str)->str:
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Texto: El jugador a buscar.
    Funcionamiento: 
        Comparo el nombre que me ingresa con los de la lista, itero en  sus logros y si pertenece al salon de la fama
        los guardo en una variable mensaje junto con el nombre y luego lo muestro por pantalla con un formato en particular.
    Retorna: 
        Una variable que contiene un str
    """
    mensaje_final = " "
    mensaje_nombre = " {}\n".format(jugador)
    validacion_re = re.findall(r"^[a-zA-Z]+ [a-zA-Z]+$",jugador)
    validacion = True

    # Verifica si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia   
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False  
    # Verifica que el nombre este en la lista 
    if validar_que_este_en_la_lista(validacion_re,lista_nombres):
        respuesta = LEYENDA_NOMBRE_FUERA_DE_LA_LISTA
        validacion = False 
    
    # Busco en los logros del jugador y si esta en el salon lo muestro
    if validacion:
        for jugadores in lista:
            if jugadores["nombre"] == jugador:
                for logro in jugadores["logros"]:
                    salon_si = re.findall(r"Miembro del Salon de la Fama del Baloncesto",logro)
                    salon_si =  " ".join(salon_si)
                    mensaje = "{}".format(salon_si)
                    mensaje_final = mensaje_final + mensaje                
        mensaje_final = mensaje_nombre + mensaje_final   
        respuesta = mensaje_final              
    return respuesta      
# print(salon_de_la_fama(lista_dream_team,"Magic Johnson"))          
"16)"
def remover_menor(lista:list)->list:
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
    Funcionamiento: 
        Comapra la lista de jugadores contra la lista que contiene al jugador con menor puntuacion en una area.
        Crea una nueva lista de diccionarios con todos los jugadores sacando el que  menos puntos hizo
    Retorna: 
        Una lista con  diccionarios    
    """
    lista_final = []
    comparar = jugador_mas_menos_haya_logrado(lista_dream_team,"promedio puntos por partido","menor")
    validacion = True

    # Verifica si alguna lista esta vacia. 
    if validar_lista_vacia(lista) or validar_lista_vacia(comparar):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False 

    #Armo la nuva lista sin el jugador que menos puntos hizo
    if validacion:             
        for diccionarios in lista:
            if diccionarios not in comparar :
                lista_final.append(diccionarios)
        respuesta = lista_final
    return respuesta

# print(remover_menor(lista_dream_team))
def calcular_promedio(lista:list,categoria:str)->str:
    """
    Parametros:
        Lista: Es una lista de diccionarios.
        Categoria: Es de donde voy a sacar el dato a promediar.
    Funcionamiento: 
        Itera sobre la lista de diccionarios, acumula el dato requerido y cuenta la cantidad de veces que se acumulo.
        A partir de acumulacion y el contador saco un promedio.
    Retorna: 
        Retorno un mensaje con el promedio     
    """
    acumulador_datos = 0
    contador_datos = 0

    validacion = True
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)

    # Verifica si alguna lista esta vacia.Findall devuelve una lista,si no encuentra nada la devuelve vacia   
    if validar_lista_vacia(lista) or validar_lista_vacia(validacion_re):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

    # Verifica que la estadistica este en la lista        
    if validar_que_este_en_la_lista(validacion_re,lista_estadisticas):
        respuesta = LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA
        validacion = False 
    # Acumulo dato y cuento cantidad de datos 
    if validacion:
        for i in range(len(lista)):
            for llave,dato in lista[i]["estadisticas"].items(): 
                categoria = categoria.replace(" ","_") 
                if llave == categoria:               
                    if lista[i]["estadisticas"][categoria] != "":
                        acumulador_datos += dato
                        contador_datos += 1
    # Hago promedio
        if contador_datos > 0:
            promedio = acumulador_datos/contador_datos
            respuesta = "El promedio es {}".format(promedio) 

    return respuesta

"20)"
def ordenados_posicion_cancha(lista:list,manera:str)->str:
    """
    Parametros:
        Lista: Es una lista de diccionarios.
        Manera: Como lo quiero ordenar.
    Funcionamiento: 
        Itera sobre la lista de diccionarios, guardo clave y del dic posicion y lo remplazo por un numero del 1 al 5.
        Ordeno a partir del nunero asignado previamente a la posicion.
        Armo un mensaje con nombre, posicion en campo y puntos para la categoria correspondiente.
    Retorna: 
        Mensaje tipo str        
    """
    
    validacion = True
    # Verifica si alguna lista esta vacia.
    if validar_lista_vacia(lista):
        respuesta = LEYENDA_LISTA_VACIA
        validacion = False

        # Verifico que se ingrese ascendente o descendente   
    if not validar_manera_asc_o_desc(manera):
        respuesta = LEYENDA_NO_INGRIESO_ASCENDENTE_O_DESCENDENTE
        validacion = False

    if validacion:
        # modifico el nombre de la posicion por el numero
        for i in range(len(lista)):
            for clave,dato in lista[i].items():
                if clave == "posicion":
                    match dato:
                        case "Base":
                            lista[i][clave] = 1
                            
                        case "Escolta":
                            lista[i][clave] = 2
                                
                        case "Alero":
                            lista[i][clave] = 3    
                            
                        case "Ala-Pivot":
                            lista[i][clave] = 4
                            
                        case "Pivot":
                            lista[i][clave] = 5
        # Ordeno segun posicion puede ser de manera ascendente o descendente
        rango_a = len(lista)
        flag_swap = True
        while flag_swap:
            flag_swap = False
            rango_a = rango_a - 1
            for indice_a in range(rango_a):
                if manera == "desc" and lista[indice_a]["posicion"] < lista[indice_a+1]["posicion"] \
                    or manera == "asc" and lista[indice_a]["posicion"] > lista[indice_a+1]["posicion"]:
                    aux = lista[indice_a]
                    lista[indice_a] = lista[indice_a+1]
                    lista[indice_a+1] = aux
                    flag_swap = True
        # Armo mensaje
        mensaje = " jugador | Posicion | % tiros de campo  \n"
        for i in range(len(lista)):
            mensaje = mensaje + " {} | {} | {} Pts\n".format(lista[i]["nombre"],
                                                                            lista[i]["posicion"],
                                                                            lista[i]["estadisticas"]["porcentaje_tiros_de_campo"])
        respuesta = mensaje
    return respuesta
