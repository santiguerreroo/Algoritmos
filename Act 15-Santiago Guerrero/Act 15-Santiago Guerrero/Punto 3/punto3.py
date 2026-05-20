"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.

"""



cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
sueldos = []
for i in range(cantidad_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}: "))
    sueldos.append(sueldo)

for k in range(cantidad_empleados - 1):
    for x in range(cantidad_empleados - 1 - k):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x + 1] = aux
print("Lista de sueldos ordenada de menor a mayor:")
print(sueldos)
