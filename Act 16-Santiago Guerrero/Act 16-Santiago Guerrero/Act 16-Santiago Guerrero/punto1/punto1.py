"""1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima."""


nombres = []
calificaciones = []
for i in range(6):
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    nombres.append(nombre)
    calificaciones.append(calificacion)

mayor=0
menor=0
for i in range(6):
    if calificaciones[i] > calificaciones[mayor]:
        mayor = i
    if calificaciones[i] < calificaciones[menor]:
        menor = i


Nmayor=[]
Nmenor=[]

for i in range(6):
    if calificaciones[i] == calificaciones[mayor]:
        Nmayor.append(nombres[i])

    if calificaciones[i] == calificaciones[menor]:
        Nmenor.append(nombres[i])
     

if len(Nmayor) == 1:
    print(f"El Estudiante con mayor nota es {Nmayor} con una nota de {calificaciones[mayor]}")

else:
    print(f"Los estudiantes con la mayor nota de {calificaciones[mayor]} son")
    for i in range(len(Nmayor)):
        print(f"{Nmayor[i]}")

if len(Nmenor) == 1:
    print(f"El Estudiante con menor nota es {Nmenor} con una nota de {calificaciones[menor]}")

else:
    print(f"Los estudiantes con la menor nota de {calificaciones[menor]} son")
    for i in range(len(Nmenor)):
        print(f"{Nmenor[i]}")




