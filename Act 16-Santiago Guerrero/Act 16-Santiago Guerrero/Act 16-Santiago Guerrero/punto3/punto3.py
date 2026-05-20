"""3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio."""



nombres = []
tiempos = []

for i in range(5):
    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = float(input("Ingrese el tiempo del atleta en segundos: "))
    nombres.append(nombre)
    tiempos.append(tiempo)

promedio = sum(tiempos) / len(tiempos)
print(f"El promedio de los tiempos es: {promedio} segundos")

for k in range(5 - 1):
    for x in range(5 - 1 - k):
        if tiempos[x] < tiempos[x + 1]:
            aux = tiempos[x]
            tiempos[x] = tiempos[x + 1]
            tiempos[x + 1] = aux

            aux2 = nombres[x]
            nombres[x] = nombres[x + 1]
            nombres[x + 1] = aux2

print(f"El atleta con mejor tiempo es {nombres[-1]} con un tiempo de {tiempos[-1]} segundos")
print(f"El atleta con peor tiempo es {nombres[0]} con un tiempo de {tiempos[0]} segundos")
print("Los atletas que superaron el promedio son:")
for i in range(5):
    if tiempos[i] < promedio:
        print(f"{nombres[i]} con un tiempo de {tiempos[i]} segundos")