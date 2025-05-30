from funciones import *

def mostrar_menu():
    bandera_verificacion = False
    while True:
        mostrar_lista()
        opcion = int(input("Eliga una opcion del 1-5: "))
           
        match opcion:
            case 1:
                print("\nOpcion 1\n")
                matriz_final  = cargar_matriz_notas()
                print(f"El la matriz es: {matriz_final}\n")
                bandera_verificacion = True     
            case 2:
                if bandera_verificacion:
                    print("\nOpcion 2\n")
                    porcentaje_aprobados(matriz_final)
                    print("\n")
                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n")
            case 3:
                if bandera_verificacion:
                    print("\nOpcion 3\n")
                    matriz_mejor_promedio = funcion_mejor_promedio(matriz_final)
                    print(f"\nEl mejor promedio es: {matriz_mejor_promedio}\n")
                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n")
            case 4:
                if bandera_verificacion:
                    print("\nOpcion 4\n")
                    nota_buscada = input("\nIngrese la nota que desea buscar: \n")
                    while not nota_buscada.isdigit() or int(nota_buscada) < 0 or int(nota_buscada) > 10:
                        nota_buscada = input("\nERROR, ingrese la nota entre 1-10 que desea buscar: \n")
                    nota_buscada = int(nota_buscada)
                    resultado = buscar_nota(matriz_final, nota_buscada)
                    print(resultado)
                    print("\n")

                else:
                    print("\nError, debe ingresar a la opcion 1 primero!!!\n")
            case 5:
                print("\nFinalizando programa...\n")
                break
            case _:
                print("\nError, ingrese opcion entre 1-5\n")


