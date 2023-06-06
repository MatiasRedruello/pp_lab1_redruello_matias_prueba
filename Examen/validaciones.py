import re
from funciones_base import *

def validar_lista_vacia(lista)->bool:
    """
    Valida si una lista está vacía.
    Retorna True si la lista está vacía, False en caso contrario.
    """
    return len(lista) == 0

def validar_indice(indice, lista)->bool:
    """
    Valida si un indice es un número entero válido dentro del rango de la lista.
    Retorna True si el indice es válido, False en caso contrario.
    """

    return re.match(r"^[0-9]+$",indice) and int(indice) < len(lista)

def validar_que_este_en_la_lista(lista:list,comparar:list)->bool:
    """
    Valida si un valor es un número entero válido dentro del rango de la lista.
    Retorna True si el valor es válido, False en caso contrario.
    """   
     
    if validar_lista_vacia(lista):# si no verifico si la lista esta vacia  rompe y no puedo comparar
        resultado = False
    else:
        resultado =  lista[0] not in comparar
    return resultado

def validar_manera_asc_o_desc(texto):
    """
    Valida si un si el texto machea con mi re.
    Retorna True si el valor es válido, False en caso contrario.
    """
    return re.match(r"^(asc|desc)$",texto,re.IGNORECASE)

def validar_tipo_lista(lista):
    """
    Valida si un la lista ingresda es un str
    Retorna True si el valor es válido, False en caso contrario.
    """
    return type(lista) == str

LEYENDA_LISTA_VACIA = "La lista esta vacia"
LEYENDA_INDICE = "El valor ingresado es erroneo"
LEYENDA_NOMBRE_FUERA_DE_LA_LISTA = "El nombre no esta en la lista"
LEYENDA_NO_INGRIESO_MAYOR_O_MENOR ="Debe ingresar mayor o menor para saber si quiere ver al que mas hizo de X cosa o al que menos hizo"
LEYENDA_CATEGORIA_FUERA_DE_LA_LISTA = "La categoria no esta en la lista"
LEYENDA_FUERA_DE_RANGO = "El numero ingresado esta fuera del rango"
LEYENDA_NO_INGRIESO_ASCENDENTE_O_DESCENDENTE = "Debe ingresar asc o desc para saber como quiere ordenar"
LEYENDA_HERENCIA_FUERA_DE_RANGO = "La lista tiene un valor tipo str.Verifique si ingreso la lista correctamente o si el rango que ingreso es valido."
