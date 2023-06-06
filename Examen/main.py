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
                    jugador_posicion = lista_jugador_posicion(lista_dream_team)
                    imprimir(jugador_posicion) 

            case "1":
                    imprimir(imprimir_menu_indices())
                    jugador_seleccionado = pregunta("¿Que jugador desea seleccionar?")
                    estadisticas_jugadores(lista_dream_team,jugador_seleccionado)
                    flag = True

            case "2":
                    if flag == True:
                        imprimir(imprimir_menu_indices())
                        jugador_a_guardar = estadisticas_jugadores(lista_dream_team,jugador_seleccionado)
                        csv_del_jugador = crear_csv(jugador_a_guardar)
                        imprimir(csv_del_jugador)
                    else:
                        imprimir("No se puede ingresar a esta seccion sin pasar por el punto 1.Gracias")

            case "3":
                    imprimir(imprimir_menu_indices())
                    respuesta_jugador = pregunta("Por favor ingrese el nombre del jugador le intereza.")
                    logros_del_jugador = logros_jugador(lista_dream_team,respuesta_jugador)
                    imprimir(logros_del_jugador)

            case "4":
                    tipo_de_estadistica = "promedio puntos por partido"
                    forma_de_ordenar = "asc"
                    resultado_busqueda = buscar_y_guarda(lista_dream_team,tipo_de_estadistica,0)
                    jugadores_ordenados = ordenar(resultado_busqueda,tipo_de_estadistica,forma_de_ordenar)
                    formato_armado = mostrar(jugadores_ordenados,"promedio puntos por partido")
                    imprimir(formato_armado)

            case "5":
                    imprimir(imprimir_menu_indices())
                    jugador_elegido = pregunta("¿Que jugado elige?")
                    imprimir(salon_de_la_fama(lista_dream_team,jugador_elegido))

                
            case "6":
                    imprimir(imprimir_menu_estadisticas())
                    respuesta_estadistica = pregunta("¿Que estadistica desea elegir?")
                    respuesta_mejor_o_peor = pregunta("¿Quiere buscar al mejor(mayor) o al peor(menor)?")
                    Jugador = jugador_mas_menos_haya_logrado(lista_dream_team,respuesta_estadistica,respuesta_mejor_o_peor)
                    formato_armado = mostrar(Jugador,respuesta_estadistica)
                    imprimir(formato_armado) 

            case "7":
                    imprimir(imprimir_menu_estadisticas_dos())
                    tipo_de_estadistica = pregunta("¿Que estadistica desea elegir?")
                    valor_elegido = pregunta("¿Cual es el valor que desea ingresar?")
                    forma_de_ordenar = pregunta("¿Como los quiere ordenados de forma ascendente(asc) o descendente(desc)?")
                    resultado_busqueda = buscar_y_guarda(lista_dream_team,tipo_de_estadistica,valor_elegido)
                    jugadores_ordenados = ordenar(resultado_busqueda,tipo_de_estadistica,forma_de_ordenar)
                    formato_armado = mostrar(jugadores_ordenados,tipo_de_estadistica)
                    imprimir(formato_armado)      
                    

            case "8":
                    tipo_de_estadistica = "promedio puntos por partido"
                    sacar_al_peor = remover_menor(lista_dream_team)
                    promedio_sin_el_peor = calcular_promedio(sacar_al_peor,tipo_de_estadistica)
                    imprimir(promedio_sin_el_peor) 

            case "9":
                    imprimir(imprimir_menu_posiciones())
                    valor_ingresado = pregunta("""Ingrese un valor,se mostraran los jugadores que hayan tenido un porcentaje de tiros de campo superior a dicho numero.
                    Puede ingresar 0 (cero) si desea que esten todos los jugadores.""")
                    forma_de_ordenar = pregunta("¿Como los quiere ordenados de forma ascendente(asc) o descendente(desc)?")
                    resultado_busqueda = buscar_y_guarda(lista_dream_team,"porcentaje tiros de campo",valor_ingresado)
                    jugadores_ordenados = ordenados_posicion_cancha(resultado_busqueda,forma_de_ordenar)
                    imprimir(jugadores_ordenados)

            case "10":
                break
examen_app()
