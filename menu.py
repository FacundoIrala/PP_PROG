# MODULO DEL MENU


from funciones import * #importamos el modulo de funciones, con el * importamos todas las funciones

def mostrar_menu():
    bandera_verificacion = False #definimos la bandera como False
    while True: #declaramos el while para que el bucle sea infinito hasta que el usuario decida parar
        mostrar_lista() # mostramos la lista con la funcion
        opcion = int(input("Eliga una opcion del 1-5: ")) # el usuario debe ingresar la opcion deaeada y lo parseamos 
           
        match opcion: #una vez parseamos el dato ingresado, utilizamos un match, dependiendo el numero, realiza una funcionalidad distinta
            case 1:
                print("\nOpcion 1\n") #mostramos que es la opcion 1
                matriz_final  = cargar_matriz_notas() #guardamos en una variable el return de la funcion
                print(f"El la matriz es: {matriz_final}\n") #mostramos al usuario 
                bandera_verificacion = True  # inicializamos la bandera como true, ya que indica que el usuario ingreso a la opcion 1
            case 2:
                if bandera_verificacion: # deja entrar unicamente si el usuario ingreso a la opcion 1, si no, le deniega. Por eso la inicalizamos como false al principio y despues true una vez ingresado a la opcion 1
                    print("\nOpcion 2\n")#mostramos que es la opcion 2
                    porcentaje_aprobados(matriz_final) # mostramos la funcion 
                    print("\n") # salto de linea
                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n") # indica que debe ingresar primero a la primer opcion, decir la bandera esta en false
            case 3:
                if bandera_verificacion:
                    print("\nOpcion 3\n")#mostramos que es la opcion 3
                    matriz_mejor_promedio = funcion_mejor_promedio(matriz_final) #guardamos el return en una variable 
                    print(f"\nEl mejor promedio es: {matriz_mejor_promedio}\n") # mostramos la variable 
                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n")
            case 4:
                if bandera_verificacion:
                    print("\nOpcion 4\n")
                    nota_buscada = input("\nIngrese la nota que desea buscar: \n") # esta opcion le pide al usuario ingresar la nota que desea buscar
                    while not nota_buscada.isdigit() or int(nota_buscada) < 0 or int(nota_buscada) > 10: #validamos que sea entero y que este entre 0 y 10
                        nota_buscada = input("\nERROR, ingrese la nota entre 1-10 que desea buscar: \n") # le volvemos a pedir que ingrese el numero con las correspondientes reglas indicadas, es un bucle infinito hasta que el usuario ingrese bien el dato
                    nota_buscada = int(nota_buscada) #parseamos el dato, por que si no, no va a poder buscar coincidencias en la matriz, ya que el dato sera string
                    resultado = buscar_nota(matriz_final, nota_buscada) #guardamos el return en una variable
                    print(resultado) # mostramos la variable
                    print("\n")
                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n")
            case 5:
                print("\nFinalizando programa...\n") # esta opcion cierra el programa(termina el bucle) con el break
                break
            case _:
                print("\nError, ingrese opcion entre 1-5\n") #si el usuario no ingresa una opcion entre 1-5, arrojara error hasta elegir la opcion valida


