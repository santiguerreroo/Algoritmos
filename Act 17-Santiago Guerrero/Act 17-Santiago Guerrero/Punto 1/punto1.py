""""1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
primer elemento de &quot;lista&quot;. El resto de enteros menores a 50 deben encontrarse
en una nueva posición dentro de la lista.
Volver a imprimir la lista."""

lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]


acumulador = [] 

#los menores a 50 del primer elemnto se guardan en el ultimo elemento de la lista
for x in range(1):
        for j in range(len(lista[0])):
            if lista[0][j] > 50:
                acumulador.append(lista[0][j])
            else:
                lista[-1].append(lista[0][j])
        lista[0] = []

for x in range(len(lista)):
    sublista_limpia = []

    
    for j in range(len(lista[x])):
        if lista[x][j] > 50:
            acumulador.append(lista[x][j])
        else:
            sublista_limpia.append(lista[x][j])
            
    lista[x] = sublista_limpia

for numero in acumulador:
    lista[0].append(numero)



print("Resultado:", lista)