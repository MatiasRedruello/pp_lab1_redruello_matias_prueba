from funcion_base import *
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
    if len(lista) > 0:
        if type(lista[0]) == dict:
            for jugadores in lista:
                formato = "{0} - {1}".format(jugadores["nombre"],jugadores["posicion"])
                lista_vacia.append(formato)
            return lista_vacia
        else:
            return errores(-4)
    else:
        return errores(-1)
    
# print(lista_jugador_posicion(lista_dream_team))
"2)"
lista_vacia = []
def estadisticas_jugador(lista:list,valor:int)->list:
    """
    Parametros:
        Lista:lista donde esta toda la informacion del Dream Team
        Valor: Es un dato entregado por el usuario con el fin de elegir un jugador
    Funcionamiento:
        Creo un indice a partir del largo de mi lista de diccionarios y lo comparo
        con el ingresado por el usuario.En una lista vacia guardo el jugador que el usuario
        queria. Ademas muestro los mismos datos mediante un print con formato.
    Retorno:
        Una lista con el jugadorque se busca.
    """
    valor = str(valor)
    if re.match(r"^[0-9]+$",valor):
        valor = int(valor)
        if len(lista) > 0:
            if type(lista[0]) == dict:
                if valor < len(lista):
                    mensaje_nombre = ""
                    mensaje_final = ""
                    lista_jugadores = []
                    for i in range(len(lista)):
                        if i == valor:
                            lista_jugadores.append(lista[i]["nombre"])
                            lista_jugadores.append(lista[i]["estadisticas"])
                            mensaje_nombre = "{}: {}\n".format("nombre",lista[i]["nombre"])
                            for datos in lista[i]["estadisticas"]:
                                mensaje = "{}: {}\n"
                                mensaje = mensaje.format(datos,lista[i]["estadisticas"][datos])
                                mensaje_final = mensaje_final + mensaje
                    mensaje_final = mensaje_nombre + mensaje_final  
                    print(mensaje_final)
                    return lista_jugadores
                else:
                    return errores(-3)
            else:
                 return errores(-4)
        else:
            return errores(-1)        
    else:
        return errores(-2)   
         
# print(estadisticas_jugador(lista_dream_team,15))
"3)"
def crear_csv(lista:list):
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
    if type(lista[0]) == str and type(lista[1]) == dict:
        if len(lista) > 0:
            nombre_archivo = "{0}.csv".format(lista[0])
            diccionario = lista[1]
            with open(nombre_archivo,"w") as archivo:
                for datos in diccionario:
                    mensaje = "{}:{}\n"
                    mensaje = mensaje.format(datos,diccionario[datos])
                    archivo.write(mensaje)
        else:
            return errores(-1) 
    else:
        return errores(-4)
   
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

    validacion_re = re.findall(r"^([a-zA-Z]+[ ][a-zA-Z]+)$",texto)
    if len(validacion_re) > 0:
        if validacion_re[0] in lista_nombres:  
            if len(lista) > 0:
                if type(lista[0]) ==  dict:
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
                    
                else:
                    errores(-4)
            else:
                errores(-1)
        else:
            return errores(-5)
    else:
        return errores(-6) 
    return mensaje_final    
# print(logros_jugador(lista_dream_team,"Christian Laettner"))
"7,8,9,13,14,16,17,19)"
def jugador_mayor_menor_cantidad(lista:list,categoria:str,extremo:str)->list:
    # hacer un menu con las opciones
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
        Exremo: Es un str que indica si se quiere buscar el mayor o el menor.
    Funcionamiento: 
        A partir de la estadistica deseada o la cantidad de logros alcanzados se busca el jugador que mas/menos haya conseguido para esa estadistica/logro.
        Guardo el indice del jugador, el mismo lo uso para guardar el diccionario en una lista y armar una lista de diccionarios.
        Tener en cuenta que en el caso de que haya empate arma la lista contiendo todos los jugadores con esa marca.

    Retorna: 
        Una lista con  diccionarios
    """
    mayor_cantidad = 0
    indice_guardado = 0
    lista_final = []
    lista_aux = []
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0: 
                if validacion_re[0] in lista_categoria:
                    categoria = categoria.replace(" ","_")
                    if re.match(r"^(menor|mayor)$",extremo,re.IGNORECASE):
                        for i in range(len(lista)):
                            if categoria in lista[i] and categoria == "logros":
                                if i == 0 or  extremo == "mayor" and  mayor_cantidad < len(lista[i]["logros"]) \
                                    or  extremo == "menor" and  mayor_cantidad > len(lista[i]["logros"]) :                        
                                    mayor_cantidad = len(lista[i]["logros"])
                                    indice_guardado = i
                                if i != 0 and mayor_cantidad == len(lista[i]["logros"]):
                                    lista_aux.append(lista[i])                   
                            else:
                                for llave,dato in lista[i]["estadisticas"].items():
                                    if llave == categoria:
                                        if i == 0 or  extremo == "mayor" and  mayor_cantidad < dato \
                                            or  extremo == "menor" and  mayor_cantidad > dato :                        
                                            mayor_cantidad = dato
                                            indice_guardado = i
                                        if i != 0 and mayor_cantidad == dato:
                                            lista_aux.append(lista[i])

                        for i in range(len(lista_aux)):
                            for llave,dato in lista_aux[i]["estadisticas"].items():
                                if  llave == categoria and mayor_cantidad == dato:
                                    lista_final.append(lista_aux[i])

                        if lista[indice_guardado] not in lista_final:
                            lista_final.append(lista[indice_guardado])
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

    return lista_final
# print(jugador_mayor_menor_cantidad(lista_dream_team,"logros","menor"))            
# print(jugador_mayor_menor_cantidad(lista_dream_team,"temporadas","mayor"))
# print(jugador_mayor_menor_cantidad(lista_dream_team,"promedio puntos por partido","mayor"))

"5,10,11,12,15,18)"
def buscar_y_comparar(lista:list,categoria:str,valor:int)->list:
    """
    Paramtros: 
        Lista:lista con los datos de los jugadores.
        Categoria: Dentro del diccionario estadisticas la estadistica (key) quiero usar.
        Valor: Dato numerico ingresado por el usuario,tambien puede ser puesto por defecto si es necesario.
    Funcionamiento: 
        Dentro del diccionario categoria y en la key deseada accedo al valor,comparo con el dato ingresado por el usuario
         y guardo en una lista el diccionario del los jugadores por arriba del valor ingresado.
    Retorno: 
        Una lista de diccionarios.
    """
    lista_jugadores_arriba_valor = []
    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)
    categoria_modificada = categoria.replace(" ","_") 
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0: 
                if validacion_re[0] in lista_categoria:
                    valor = str(valor)
                    if re.match(r"^[0-9]+$",valor):
                        valor = int(valor) 
                        for i in range(len(lista)): 
                            llamado = jugador_mayor_menor_cantidad(lista_dream_team,categoria,"mayor")
                            for i_dos in range(len(llamado)):
                                if  llamado[i_dos]["estadisticas"][categoria_modificada] >= valor:        
                                    if  lista[i]["estadisticas"][categoria_modificada] > valor: 
                                        lista_jugadores_arriba_valor.append(lista[i])
                                else:
                                    return errores(-3)      
                    else:
                        return errores(-2)    
                else:
                    return errores(-5)   
            else:
                return errores(-1)  
        else:
            return errores(-4)  
    else:
        return errores(-1)
    
    return lista_jugadores_arriba_valor
# print(buscar_y_comparar(lista_dream_team,"promedio puntos por partido",24))

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
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0:
                if validacion_re[0] in lista_nombres:
                    for jugadores in lista:
                        for key in jugadores.keys():
                            if jugadores[key] == jugador:
                                for logro in jugadores["logros"]:
                                    salon_si = re.findall(r"[a-zA-Z]{7}[ ][a-z]{3}[ ][a-zA-z]{5}[ ][a-z]{2}[ ][a-z]{2}[ ][a-zA-Z]{4}[ ][a-z]{3}[ ][a-zA-Z]{10}"
                                                            ,logro)
                                    salon_si =  " ".join(salon_si)
                                    mensaje = "{}".format(salon_si)
                                    mensaje_final = mensaje_final + mensaje                
                    mensaje_final = mensaje_nombre + mensaje_final   
                else:
                    return errores(-5) 
            else:
                return errores(-6)    
        else:
            return errores(-4)    
    else:
        return errores(-1)    
                
    return mensaje_final                 
# print(salon_de_la_fama(lista_dream_team,"Christian Laettner"))
     

"16)"
def remover_menor(lista:list,comparar:list)->list:
    """
    Parametros:
        Lista: Lista con  datos de los jugadores.
        Comparar: Es la lista contra la que voy a comparar
    Funcionamiento: 
        Comapra la lista de jugadores contra la lista del jugador que es el menor en una deterinada area.
        Crea una nueva lista de diccionarios con todos los jugadores menos el menor
    Retorna: 
        Una lista con  diccionarios    
    """
    if len(lista) > 0:
        if type(lista[0]) == dict:    
            if len(comparar) > 0:
                if type(comparar[0]) == dict:
                    lista_final = []
                    for diccionarios in lista:
                        if diccionarios not in comparar :
                            lista_final.append(diccionarios)
                else:
                    return errores(-4)
            else:
                return errores(-1)
        else:
            return errores(-4)
    else:
        errores(-1)
    return lista_final
# print(remover_menor(lista_dream_team,jugador_mayor_menor_cantidad(lista_dream_team,"promedio puntos por partido","mayor")))

def calcular_promedio(lista:list,categoria:str)->str:
    """
    Parametros:
        Lista: Es una lista de diccionarios.
        Categoria: Es de donde voy a sacar el dato a promediar.
    Funcionamiento: 
        Itera sobre la lista de diccionarios, acumula el dato requerido y cuenta la cantidad de veces que se acumulo.
        A partir de acumulacion y el contador saco un promedio y armo un mensaje.
    Retorna: 
        Mensaje tipo str        
    """
    acumulador_datos = 0
    contador_datos = 0
    mensaje = ""
    nombre = " "

    validacion_re = re.findall(r"^([a-zA-Z]+(?: [a-zA-Z]+){0,3})$",categoria)
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if len(validacion_re) > 0: 
                if validacion_re[0] in lista_categoria:
                    for i in range(len(lista)):
                        for llave,dato in lista[i]["estadisticas"].items(): 
                            categoria = categoria.replace(" ","_") 
                            if llave == categoria:               
                                if lista[i]["estadisticas"][categoria] != "":
                                    acumulador_datos += dato
                                    contador_datos += 1
                    if contador_datos > 0:
                        promedio = acumulador_datos/contador_datos
                    for diccioanrio in jugador_mayor_menor_cantidad(lista_dream_team,"promedio puntos por partido","menor"):
                        nombre = diccioanrio["nombre"] 
                    mensaje = "El promedio de la categoria {} es {} y el jugador excluido es {} ".format(categoria,promedio,nombre)                        
                else:
                    return errores(-5)   
            else:
                return errores(-6)  
        else:
            return errores(-4)  
    else:
        return errores(-1)
    return mensaje
# print(calcular_promedio(remover_menor(lista_dream_team,jugador_mayor_menor_cantidad(lista_dream_team,"promedio puntos por partido","menor")),"promedio puntos por partido"))

"20)"
def ordenados_posicion_cancha(lista:list,manera):
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
    if len(lista) > 0:
        if type(lista[0]) == dict:
            if re.match(r"^(asc|desc)$",manera,re.IGNORECASE):
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

                mensaje = " jugador | Posicion | % tiros de campo  \n"
                for i in range(len(lista)):
                    mensaje = mensaje + " {} | {} | {} Pts\n".format(lista[i]["nombre"],
                                                                                    lista[i]["posicion"],
                                                                                    lista[i]["estadisticas"]["porcentaje_tiros_de_campo"])
            else:
                return errores(-7)
        else:
            return errores(-4)
    else:
        return errores(-1)

    return mensaje

# print(ordenados_posicion_cancha(buscar_y_comparar(lista_dream_team,"porcentaje tiros de campo",51),"asc"))