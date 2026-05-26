"""4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)"""

n = int(input("Cuantos empleados tiene la empresa? "))
empleados = []

sueldos = []

for i in range(n):
    empleado = input("Ingrese el nombre del empleado: ")
    suel = int(input(f"Ingrese el sueldo de {empleado}: "))
    sueldos.append(suel)
    empleados.append(empleado)

print("\nLista original:")
for i in range(n):
    print(f"Empleado: {empleados[i]}, Sueldo: {sueldos[i]}")

empleados_filtrados = []
sueldos_filtrados = []

for i in range(n):
    if sueldos[i] < 10000: 
        empleados_filtrados.append(empleados[i])
        sueldos_filtrados.append(sueldos[i])

empleados = empleados_filtrados
sueldos = sueldos_filtrados

print("\nLista filtrada:")
for i in range(len(empleados)):
    print(f"Empleado: {empleados[i]}, Sueldo: {sueldos[i]}")