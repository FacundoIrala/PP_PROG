# PUNTO 1
def cargar_matriz_notas():
    matriz = [] #inicializamos la variable como lista
    n = (input("Ingrese cantidad de alumnos: ")) #le pedimos al usuario que ingrese cant de alumnos
    
    while not n.isdigit(): #validacion, si la variable no es un digito positivo, arroja error y le vuelve a pedir al usuario el dato 
        print("ERROR, ingrese un numero")
        n = (input("Ingrese cantidad de alumnos: "))   
    
    m = input("Ingrese la cantidad de examenes que tuvo cada alumno, debe ser igual a la cantidad de alumnos: ")
    
    while not m.isdigit() or m != n:
        print("ERROR, ingrese un numero, tener en cuenta que debe ser el mismo a la cantidad de alumnos")
        m = (input("Ingrese la cantidad de examenes que tuvo cada alumno: "))
    
    n = int(n)#parseamos el dato
    m = int(m)#parseamos el dato
    #parseo aca los datos ya que si lo hago en la linea 8, al moment ode comparar n y m, tira error ya que uno ya es del tipo int y el otro str
    
    
    for i in range(n):#recorremos segun el dato ingresado por el usuario
        fila = [] #Creamos una lista para guardar las notas
        for j in range(m):#recorremos segun el dato ingresado por el usuario
                nota = (input(f"Ingrese el dato para la celda [{i}][{j}]: ")) #le pedimos al usuario cargar las notas
                while not nota.isdigit() or int(nota) < 0 or int(nota) > 10: #validamos que sea un numero positivo y que este entre 1-10
                    print("ERROR, ingrese una nota válida (0-10)") #le mostramos que ingreso mal
                    nota = input(f"  Nota del examen {j+1}: ")#le pedimos que reingrese la nota con los parametros solicitados
                fila.append(int(nota))#agregamos la nota a la fila
                    
        matriz.append(fila) # agrego la fila a la columna
    
    
    return matriz # retorno la matriz

# PUNTO 2 

def porcentaje_aprobados(matriz):
    for i in range(len(matriz)): #recorremos la primera columna
        total_examenes = 0 #inicializamos la variable del total de examenes
        total_aprobados = 0 #inicializamos la variable del total de aprobados
        for j in range(len(matriz[i])): #recorremos la fila
            total_examenes += 1 #agregamos un contador por cada examen que se encuentre en la fila, osea que rindio el alumno
            if matriz[i][j] >= 6: # validamos que la nota sea mayor a 6
                total_aprobados += 1 # si da true, agregamos +1 al contador de aprobados
        
        porcentaje_total =(total_aprobados / total_examenes)* 100 # hacemos la operacion para calcular el porcentaje de examenes que aprobo el alumno
        
        print(f"Alumno {i + 1}: {porcentaje_total: } % de examenes que aprobo") # mostramos en pantalla por cada lista dentro de la matriz, simbolizando al alumno con sus notas
            
# PUNTO 3

def funcion_mejor_promedio(matriz):
    columna = []
    
    bandera = True          
    
    for i in range(len(matriz)):
        acumulador_examenes = 0
        fila = []
        for j in range(len(matriz[i])):
            acumulador_examenes += matriz[i][j]      
                         
        promedio = acumulador_examenes / len(matriz[i])
            
        if bandera == True or  promedio >= mayor_promedio:
            mayor_promedio = promedio
            indice_alumno = i
            bandera = False
        
    fila.append(promedio)
    fila.append(indice_alumno)
        
    columna.append(fila)
    
    return columna

# PUNTO 4

def buscar_nota(matriz, nota_buscada):
    
    nueva_matriz = []

    for i in range(len(matriz)):        
        for j in range(len(matriz[i])):
            if nota_buscada == matriz[i][j]:
                lista_indice_nota = [i,j]
                nueva_matriz.append(lista_indice_nota)
        
    if not nueva_matriz:
        return "No se encontró ninguna coincidencia"    
        
    return nueva_matriz



def mostrar_lista():
    lista_opciones = ["1) Función cargar_matriz_notas\n",
                  "2) Función porcentaje_aprobados\n",
                  "3) Función mejor_promedio\n",
                  "4) Función buscar_nota\n",
                  "5) Salir del programa\n"]
    
    for opcion in lista_opciones:
        print(opcion)


