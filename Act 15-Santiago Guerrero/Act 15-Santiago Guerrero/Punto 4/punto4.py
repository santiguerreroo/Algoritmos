"""4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente."""




numeros = []
for i in range(5):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)
for k in range(4):
    for x in range(4-k):
        if numeros[x] > numeros[x+1]:
            aux = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1] = aux
print("Lista ordenada de menor a mayor:")
print(numeros)
for k in range(4):
    for x in range(4-k):
        if numeros[x] < numeros[x+1]:
            aux = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1] = aux
print("Lista ordenada de mayor a menor:")
print(numeros)
