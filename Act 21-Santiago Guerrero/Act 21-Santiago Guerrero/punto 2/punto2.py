"""Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor."""

def cargar():
    lista=[]
    nom=(input("ingrese nombre del empleado"))
    sue=int(input("ingrese sueldo del empleado"))
    lista.append((nom,sue))
    return lista

def mayor(emp1,emp2):
    empleado1=emp1[0]
    empleado2=emp2[0]
    if empleado1[1]>empleado2[1]:
        print("El que mayor sueldo tiene es el empleado ", empleado1[0])

    else:
        print("El que mayor sueldo tiene es el empleado ", empleado2[0])

emp1=cargar()
emp2=cargar()
mayor(emp1,emp2)