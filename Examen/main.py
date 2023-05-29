from funciones_interaccion import *
def examen_app():
    """
    Parametros:
        No ingresa nada
    Funcionalidad:
        Es el menu principal, desde aca se maneja todo el codigo
    Retorno: 
        No retorna nada
    """
    flag = False
    while True:
        match menu_principal_examen():
            case "0":
                imprimir(lista_jugador_posicion(lista_dream_team)) 
            case "1":
                    imprimir(imprimir_menu_indices())
                    respuesta_uno_dos = pregunta("¿Que jugador desea seleccionar?")
                    estadisticas_jugador(lista_dream_team,respuesta_uno_dos)
                    flag = True
            case "2":
                    if flag == True:
                        imprimir(imprimir_menu_indices())
                        imprimir(crear_csv(estadisticas_jugador(lista_dream_team,respuesta_uno_dos)))
                    else:
                        imprimir("No se puede ingresar a esta seccion sin pasar por el punto 2.Gracias")
            case "3":
                    imprimir(imprimir_menu_indices())
                    imprimir(logros_jugador(lista_dream_team,
                                            pregunta("Por favor ingrese el nombre del jugador le intereza.")))
            case "4":
                    imprimir(mostrar(ordenar(buscar_y_comparar(lista_dream_team,"promedio puntos por partido",0)
                                                                                ,"promedio puntos por partido",
                                                                                "asc"),"promedio puntos por partido"))
            case "5":
                    imprimir(imprimir_menu_indices())
                    imprimir(salon_de_la_fama(lista_dream_team,pregunta("¿Que jugado elige?")))

                
            case "6":
                    imprimir(imprimir_menu_estadisticas())
                    respuesta_uno_seis = pregunta("¿Que estadistica desea elegir?")
                    respuesta_dos_seis = pregunta("¿Quiere buscar al mejor(mayor) o al peor(menor)?")
                    imprimir(mostrar(jugador_mayor_menor_cantidad(lista_dream_team,respuesta_uno_seis,respuesta_dos_seis),
                                     respuesta_uno_seis)) 
            case "7":
                    imprimir(imprimir_menu_estadisticas())
                    respuesta_uno_siete = pregunta("¿Que estadistica desea elegir?")
                    respuesta_dos_siete = pregunta("¿Cual es el valor que desea ingresar?")
                    respuesta_tres_siete = pregunta("¿Como los quiere ordenados de forma ascendente(asc) o descendente(desc)?")
                    imprimir(mostrar(ordenar(buscar_y_comparar(lista_dream_team,respuesta_uno_siete,respuesta_dos_siete),
                                                               respuesta_uno_siete,
                                                               respuesta_tres_siete),respuesta_uno_siete))                                        
            case "8":
                    imprimir(calcular_promedio(remover_menor(lista_dream_team,jugador_mayor_menor_cantidad(lista_dream_team,
                                                                                                       "promedio puntos por partido",
                                                                                                       "menor")),
                                                                                                       "promedio puntos por partido"))  
            case "9":
                    imprimir(imprimir_menu_posiciones())
                    respuesta_uno_nueve = pregunta("¿Cual es el valor que desea ingresar?.Puede ingresar 0 (cero) si desea que esten todos los jugadores")
                    respuesta_dos_nueve = pregunta("¿Como los quiere ordenados de forma ascendente(asc) o descendente(desc)?")
                    imprimir(ordenados_posicion_cancha(buscar_y_comparar(lista_dream_team,"porcentaje tiros de campo",respuesta_uno_nueve),
                                                                        respuesta_dos_nueve))
            case "10":
                break
examen_app()
