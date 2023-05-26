from funcion_json import *
import re
"1)"
def lista_jugador_posicion(lista:list)->list:
    """
    Parametros:
        lista: lista donde esta toda la informacion del Dream Team
    Funcionamiento:
        Busca el nombre y la posicion de juego del jugador y la muestra
    Retorno:
        Lista con nombre y posicion
    """
    lista_vacia =  []
    for jugadores in lista:
        formato = " {0} - {1}".format(jugadores["nombre"],jugadores["posicion"])
        lista_vacia.append(formato)
    return lista_vacia
# print(lista_jugador_posicion(lista_dream_team))
"2)"
def estadisticas_jugador(lista:list,indice:str)->list:
    """
    Parametros:
        Lista:lista donde esta toda la informacion del Dream Team
        Indice: Es un dato entregado por el usuario con el fin de elegir un jugador
    Funcionamiento:
        Creo un indice a partir del largo de mi lista de diccionarios y lo comparo
        con el ingresado por el usuario.En una lista vacia guardo el jugador que el usuario
        queria. Ademas muestro los mismos datos mediante un print con formato.
    Retorno:
        Una lista con el jugadorque se busca.
    """
    mensaje_nombre = ""
    mensaje_final = ""
    lista_vacia = []
    for i in range(len(lista)):
        if i == int(indice):
            lista_vacia.append(lista[i]["nombre"])
            lista_vacia.append(lista[i]["estadisticas"])
            mensaje_nombre = "{}: {}\n".format("nombre",lista[i]["nombre"])
            for datos in lista[i]["estadisticas"]:
                mensaje = "{}: {}\n"
                mensaje = mensaje.format(datos,lista[i]["estadisticas"][datos])
                mensaje_final = mensaje_final + mensaje
    mensaje_final = mensaje_nombre + mensaje_final        
    print(mensaje_final)            
    return lista_vacia
# estadisticas_jugador(lista_dream_team,"8")
"3)"
def crear_csv(lista:list)->None:
    """
    Parametros:
        Lista: Esta lista proviene particularmente del punto dos y tiene dos elemen-
        tos
        un str y un diccionario.
    Funcionamiento:
        Guardo el str en una variable para darle nombre al archivo y guardo el diccio-
        nario en otra y con el mismo creo el csv con los datos y las key correspon-
        dientes
    Retorno: None       
    """
    nombre_archivo = "{0}.csv".format(lista[0])
    diccionario = lista[1]
    print(type(lista))
    
    
    with open(nombre_archivo,"w") as archivo:
        for datos in diccionario:
            mensaje = "{}:{}\n"
            mensaje = mensaje.format(datos,diccionario[datos])
            archivo.write(mensaje)
   
# print(crear_csv((estadisticas_jugador(lista_dream_team,"0"))))
"4)"
def logros_jugador(lista:list,texto:str)->str:
    """
    Parametros:
        Lista: Lista con lso datos de los jugadores.
        Texto: El jugador a buscar.
    Funcionamiento: 
        Comparo el nombre que me ingresa con los de la lista, busco sus logros y los guardo en una variable
        mensaje junto cpn el nombre y luego lo muestro por pantalla con un formato en particular.
    Retorna: 
        Mensaje final
    """
    mensaje_nombre = ""
    mensaje_final = ""
    for jugadores in lista:
        for key in jugadores.keys():
            if jugadores[key] == texto:
               mensaje_1 = "{}: {}\n".format("nombre",jugadores["nombre"])
               mensaje_2 = "{}:\n".format("logros")
               mensaje_nombre = mensaje_1 + mensaje_2
               for texto in jugadores["logros"]:
                 mensaje = "      ° {}\n".format(texto)
                 mensaje_final = mensaje_final + mensaje
    mensaje_final = mensaje_nombre + mensaje_final
    return mensaje_final
        
# logros_jugador(lista_dream_team,"Larry Bird")
"5)"
# terminar no lo entiendo bien
def calcular_promedio_puntos(lista:list):
    acumulador_puntos = 0
    contador = 0
    promedio = 0
    for jugadores in lista:
        for dato in jugadores["estadisticas"]:
           if dato == "promedio_puntos_por_partido":
               acumulador_puntos = acumulador_puntos + jugadores["estadisticas"][dato]
               contador += 1
    promedio = acumulador_puntos/contador
    print(promedio)

# calcular_promedio_puntos(lista_dream_team)
"6)"
def salon_de_la_fama(lista:list,texto:str)->str:
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Texto: El jugador a buscar.
    Funcionamiento: 
        Comparo el nombre que me ingresa con los de la lista, itero en  sus logros y si pertenece al salon de la fama
        los guardo en una variable mensaje junto con el nombre y luego lo muestro por pantalla con un formato en particular.
    Retorna: 
        Mensaje final
    """
    mensaje_final = " "
    mensaje_nombre = " {}\n".format(texto)
    for jugadores in lista:
        for key in jugadores.keys():
            if jugadores[key] == texto:
               for logro in jugadores["logros"]:
                   salon_si = re.findall(r"[a-zA-Z]{7}[ ][a-z]{3}[ ][a-zA-z]{5}[ ][a-z]{2}[ ][a-z]{2}[ ][a-zA-Z]{4}[ ][a-z]{3}[ ][a-zA-Z]{10}",logro)
                   salon_si =  " ".join(salon_si)
                   mensaje = "{}".format(salon_si)
                   mensaje_final = mensaje_final + mensaje                
    mensaje_final = mensaje_nombre + mensaje_final            
              
    return mensaje_final                 
# salon_de_la_fama(lista_dream_team,"Magic Johnson")
"7,8,9,13,14,19)"
def jugador_mayor_cantidad(lista:list,texto:str)->str:
    # hacer un menu con las opciones
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Texto: la estadistica que se requiere
    Funcionamiento: 
        A partir de la estadistica deseada se busca el jugador que mas haya logrado para dicho pedido.
        Se muestra dicho jugador de mayor estadistica con el valor de la misma
    Retorna: 
        Mensaje final
    """
    mayor_cantidad = 0
    nombre_mayor_cantidad = ""
    for i in range(len(lista)):
        for llave,dato in lista[i]["estadisticas"].items():
            if llave == texto and  mayor_cantidad < dato:                        
                mayor_cantidad = dato
                nombre_mayor_cantidad = lista[i]["nombre"]
    mensaje = "El jugador {} es el mas destacado en la categoria {} y dicho valor es de {}".format(nombre_mayor_cantidad,
                                                                                   texto,
                                                                                   mayor_cantidad)
    return mensaje
                    
# jugador_mayor_cantidad(lista_dream_team,"temporadas")