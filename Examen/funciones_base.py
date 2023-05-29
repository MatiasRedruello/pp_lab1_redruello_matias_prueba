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

def errores(numero_error:int)->str:
    """
    Parametros:
         Recibe un entero
    funcionalidad:
         Se encarga de retornar una leyenda respondiendo a las protecciones del codigo.
    Retorno: 
         Sus retornos son sus propias protecciones
    """
    if numero_error > 0 and numero_error < 8:
        if type(numero_error) == int:
            match(numero_error):
                case -1:
                        mensaje =  "-1 Lista/diccionario vacia/o"
                        return mensaje
                case -2:
                        mensaje =  "-2 No es un caracter valido"
                        return mensaje               
                    
                case -3:
                        mensaje =  "-3 El valor ingresado esta fuera de rango"
                        return mensaje                  
                    
                case -4:
                        mensaje =  "-4 El formato de la lista ingresada no es el correcto para esta funcion"
                        return mensaje                  
                case -5:
                        mensaje = "-5 No esta en la lista"  
                        return mensaje  
                                                                                
                case -6:
                        mensaje =  "-6 Ingrese el nombre completo"
                        return mensaje  
                                        
                case -7:
                        mensaje =  "-7 Opcion incorrecta"
                        return mensaje 

        else:
                return errores(-2)
    else:
        return errores(-3)
                               
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
    if len(lista) > 0:   
        if type(lista[0]) == dict:
            
            for jugadores in lista:
                for clave,dato in jugadores.items():
                    if clave == "nombre": 
                        lista_vacia.append(dato)
        else:
            return errores(-4)
    else:
          return errores(-1)
    return lista_vacia
lista_nombres = guardar_nombres(lista_dream_team)
def guardar_categorias(lista:list)->list:
    """
    Parametros:
        lista: lista donde esta toda la informacion del Dream Team
    Funcionamiento:
        Busca el diccionario nombre y lo separo en una nueva lista 
    Retorno:
        Lista de nombres
    """
    lista_vacia = []
    if len(lista) > 0:    
        if type(lista[0]):
            for clave in lista[0]["estadisticas"].keys():
                    lista_vacia.append(clave)

            palabras =",".join(lista_vacia)
            palabras = palabras.replace("_"," ")
            lista_vacia = palabras.split(",")
            lista_vacia.append("logros")
        else:
              return errores(-4)
    else:
          return errores(-1)
    return lista_vacia
lista_categoria = guardar_categorias(lista_dream_team)




