"""2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados."""




nombres = []
ventas = []
for i in range(5):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = float(input("Ingrese venta en un mes: "))
    nombres.append(nombre)
    ventas.append(venta)

for k in range(5 - 1):
    for x in range(5 - 1 - k):
        if ventas[x] < ventas[x + 1]:
            aux = ventas[x]
            ventas[x] = ventas[x + 1]
            ventas[x + 1] = aux

            aux2 = nombres[x]
            nombres[x] = nombres[x + 1]
            nombres[x + 1] = aux2

print("Lista ordenada de mayor a menor según las ventas:")
for i in range(5):
    print(f"{nombres[i]}: {ventas[i]}")



mayor=0
menor=0

for i in range(5):
    if ventas[i] > ventas[mayor]:
        mayor = i
    if ventas[i] < ventas[menor]:
        menor = i
Nmenor=[]

for i in range(5):
    if ventas[i] == ventas[menor]:
        Nmenor.append(nombres[i])







print(f"El trabajador con menor venta es {Nmenor} con una venta de {ventas[menor]}")

