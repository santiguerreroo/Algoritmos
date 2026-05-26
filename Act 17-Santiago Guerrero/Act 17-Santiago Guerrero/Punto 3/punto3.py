""""3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días."""


empleados = []
for i in range(3):
    empleado = input("Ingrese el nombre del empleado: ")
    faltas = []
    for j in range(3):
        falta = int(input(f"Ingrese el número de días que {empleado} faltó en el mes {j+1}: "))
        faltas.append(falta)
    empleados.append((empleado, faltas))



print("\nEmpleados y días que faltaron:")

for empleado, faltas in empleados:
    print(f"{empleado}: {faltas}")

print("\nEmpleados con la cantidad de inasistencias:")

inasistencias = []

for x in range(len(empleados)):
    total_faltas = 0

    for falta in empleados[x][1]:
        total_faltas += falta

    inasistencias.append((empleados[x][0], total_faltas))

    print(f"{empleados[x][0]}: {total_faltas} días")

menor = inasistencias[0][1]

for x in range(len(inasistencias)):
    
    if inasistencias[x][1] < menor:
        menor = inasistencias[x][1]

print("\nEmpleados que faltan menos días:")

for x in range(len(inasistencias)):
    if inasistencias[x][1] == menor:
        print(f"{inasistencias[x][0]} con {menor} días de inasistencia")
