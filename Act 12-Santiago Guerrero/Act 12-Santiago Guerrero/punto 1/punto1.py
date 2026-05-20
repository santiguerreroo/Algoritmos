#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
#informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayor7=0
menor7=0

for x in range(10):
    notas=int(input("Ingrese la nota del alumno"))
    if notas>=7:
        mayor7+=1
    else:
        menor7+=1

print("la cantidad de alumnos con notas de 7 o mas son: ", mayor7 ," y los que tienen menos de 7 son: " , menor7)
