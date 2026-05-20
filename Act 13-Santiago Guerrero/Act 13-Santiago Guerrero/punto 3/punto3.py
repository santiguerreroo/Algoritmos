#3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
#(mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que
#puede haber dos o más estructuras repetitivas en un algoritmo.


suma1=0
suma2=0

for x in range(15):
    valores1=int(input("Ingrese 15 valores lista 1"))
    suma1+=valores1

    valores2=int(input("Ingrese 15 valores lista 2"))
    suma2+=valores2

if suma1>suma2:
    print("La lista 1 es mayor")

if suma2>suma1:
    print("La lista 2 es mayor")

if suma1==suma2:
    print("Listas iguales")