#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas.
#3. Imprimir las dos listas de sueldos.


turno_mañana=[]

turno_tarde=[]

for x in range(4):
    valor=int(input("Ingrese su sueldo del turno mañana"))
    turno_mañana.append(valor)

for i in range(4):
    valor=int(input("Ingrese su sueldo del turno tarde"))
    turno_tarde.append(valor)

print("sueldos del turno mañana", turno_mañana)
print("sueldos del turno tarde", turno_tarde)

