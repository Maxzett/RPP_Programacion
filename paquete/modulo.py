
def inicializar_matriz(filas: int, col: int, elemento: any = 0):
    
    matriz = []

    for i in range(len(filas)):
        fila = [0] * col

        matriz += [fila]
        
    return matriz
             

def calcular_totales(matriz: list, opcion: int) -> list:
    
    if opcion == 2:
        lista_totales = []
        acumulador = 0
    
        for fila in range(len(matriz)):
            for col in range(len(matriz[fila])):
                acumulador += matriz[fila][col] 
            lista_totales += [acumulador]   
        
        return lista_totales
    
    elif opcion == 3: 
        lista_totales_por_col = []
        acumulador_2 = 0
        
        for col in range(len(matriz[0])):
            for fila in range(len(matriz)):
                acumulador_2 += matriz[fila][col]
            lista_totales_por_col += [acumulador_2]
        
        return lista_totales_por_col

    else:
        print('Incorrecto.')

def estimar_stock(lista_totales: list, lista_nombres: list, limite: int, opcion: int)-> None:
    
    if opcion == 2:
        lista_depositos_mas_lim = []
        
        for i in range(len(lista_nombres)):
            if lista_totales[i] > limite:
                lista_depositos_mas_lim += [lista_nombres[i]]

        print(f'Los depositos con mas de {limite} unidades son: {lista_depositos_mas_lim}')
        
    
    elif opcion == 3:
        lista_equipos_mas_lim = []
        
        for i in range(len(lista_nombres)):
            if lista_totales[i] > limite:
                lista_equipos_mas_lim += [lista_nombres[i]]

        print(f'Los equipos con mas de {limite} camisetas son: {lista_equipos_mas_lim}')


#punto 4: Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
#encuentra.

def calcular_maximos(matriz: list, lista_nom: list, lista_nom_2: list)-> None:
    
    for i in range(len(lista_nom_2)):
        flag = False
        
        for j in range(len(matriz[i])):    
            if flag == False:
                maximo = matriz[j][i]
                correspondiente = lista_nom[j]
                flag = True
                
            elif matriz[j][i] > maximo:
                maximo = matriz[j][i]
                correspondiente = lista_nom[j]        
        print(f'El {lista_nom_2[i]} tiena la maxima cantidad de camisetas en {correspondiente}, son {maximo}')


# Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
# determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
# se deben restar los productos vendidos del stock y generar una matriz con la
# recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
# listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.
 
def cargar_ventas(lista_precios: list = 100) -> list:
    pass