"""4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)"""


docentes = []
puntajes = []
for i in range(6):
    docente = input("Ingrese el nombre del docente: ")
    puntaje = float(input("Ingrese el puntaje promedio del docente (de 1 a 10): "))
    docentes.append(docente)
    puntajes.append(puntaje)    

for k in range(6 - 1):
    for x in range(6 - 1 - k):
        if puntajes[x] < puntajes[x + 1]:
            aux = puntajes[x]
            puntajes[x] = puntajes[x + 1]
            puntajes[x + 1] = aux

            aux2 = docentes[x]
            docentes[x] = docentes[x + 1]
            docentes[x + 1] = aux2

print(f"El docente con la calificación más alta es {docentes[-1]} con un puntaje de {puntajes[-1]}")
print(f"El docente con la calificación más baja es {docentes[0]} con un puntaje de {puntajes[0]}")

print("Lista de docentes ordenada de mayor a menor según la calificación:")
for i in range(6):
    print(f"{docentes[i]}: {puntajes[i]}")
    
aprobados = 0
desaprobados = 0
for i in range(6):
    if puntajes[i] >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Cantidad de docentes aprobados: {aprobados}")
print(f"Cantidad de docentes desaprobados: {desaprobados}")

