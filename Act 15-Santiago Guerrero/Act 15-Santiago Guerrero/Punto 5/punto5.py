"""5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente."""




paises=[]
cantidadHabitantes=[]

for i in range(5):

    pais=input("Ingrese el nombre del país: ")
    habitantes=int(input("Ingrese la cantidad de habitantes del país: "))
    paises.append(pais)
    cantidadHabitantes.append(habitantes)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=cantidadHabitantes[x]
            cantidadHabitantes[x]=cantidadHabitantes[x+1]
            cantidadHabitantes[x+1]=aux2

print("Paises ordenados alfabeticamente:")
for i in range(5):
    print(f"{paises[i]} - {cantidadHabitantes[i]} habitantes")
for k in range(4):
    for x in range(4-k):
        if cantidadHabitantes[x]<cantidadHabitantes[x+1]:
            aux1=cantidadHabitantes[x]
            cantidadHabitantes[x]=cantidadHabitantes[x+1]
            cantidadHabitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2
print("\nPaises ordenados por cantidad de habitantes (de mayor a menor):")
for i in range(5):
    print(f"{paises[i]} - {cantidadHabitantes[i]} habitantes")

    