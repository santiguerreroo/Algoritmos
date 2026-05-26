"""""2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor."""


paises = []
for i in range(4):
    pais = input("Ingrese el nombre del país: ")
    temperaturas = []
    for j in range(3):
        temp = float(input(f"Ingrese la temperatura media mensual {j+1} para {pais}: "))
        temperaturas.append(temp)
    paises.append((pais, temperaturas))

print("\nPaíses y temperaturas medias mensuales:")

for pais, temperaturas in paises:
    print(f"{pais}: {temperaturas}")

print("\nPaíses y temperaturas medias trimestrales:")
temp_trimestral = []


#suma sin sum
for x in range(len(paises)):
    suma = 0
    for temp in paises[x][1]:
        suma += temp
    temp_trimestral.append((paises[x][0], suma / 3))
    print(f"{paises[x][0]}: {suma / 3}")


mayor=0
for x in range(len(temp_trimestral)):
    if temp_trimestral[x][1]>mayor:
        mayor=temp_trimestral[x][1]
        pais_mayor=temp_trimestral[x][0]
print(f"\nEl país con la temperatura media trimestral mayor es: {pais_mayor} con {mayor}°C")

