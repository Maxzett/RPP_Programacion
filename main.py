from paquete.modulo import *

depositos = ['Tierra del Fuego', 'Tucuman', 'Mendoza', 'BsAs', 'Misiones', 'Santa Fe']
equipos = ['Barcelona', 'Inter Miami', 'PSG', 'Manchester City', 'Real Madrid']

#matriz prueba
matriz_prueba = [[3,4,4,25,60],
                 [17,50,10,8,9],
                 [25,46,81,4,6],
                 [56,7,43,49,12],
                 [13,58,32,26,28],
                 [47,9,14,41,8]]


print('Seleccione una opcion:')
print('1- carga secuencial / obtener existencias')
print('2- Mostrar depositos que tienen en stock mas de 10.000 camisetas.')
print('3- Mostrar equipos que hay en stock más de 5.000 camisetas.')
print('4- Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se encuentra')
print('5- Cargar ventas')
print()
opcion = input('Ingrese una opcion: ')


match opcion:
    
    case '1':
        matriz = inicializar_matriz(len(depositos), len(equipos))
        
        for i in range(len(depositos)):
            for j in range(len(equipos)):
                
                stock = int(input(f'Ingrese el stock de {equipos[j]} en {depositos[i]}'))
                matriz[i][j] = stock

    case '2':
        totales_por_deposito = calcular_totales(matriz_prueba, 2)
        #devuelve la suma del stock por deposito = filas
        
        resultado = estimar_stock(totales_por_deposito, depositos, 400, 2)
        print(resultado)            
    
    case '3':
        totales_por_equipo = calcular_totales(matriz_prueba, 3)
        #devuelve la suma del stock por equipos = col
        
        resultado = estimar_stock(totales_por_equipo, equipos, 500, 3)
        print(resultado)
        
    case '4':
        result = calcular_maximos(matriz_prueba, depositos, equipos)
        print(result)
        
    case '5':
        matriz_ventas = [[2,5,7,12,6],
                         [8,4,11,3,15],
                         [4,6,9,10,6],
                         [2,22,5,7,9],
                         [13,5,7,18,3],
                         [0,7,19,3,6]]
        
        lista_precios = [150,200,100,125,250]
        pass
        