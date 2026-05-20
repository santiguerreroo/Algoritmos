#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
#empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
#programa deberá informar el importe que gasta la empresa en sueldos al personal.

cant=int(input("Ingrese cantidad de empleados"))


entre100y300=0
mas300=0
suma=0

for x in range(cant):
    sueldos=int(input("Ingrese el sueldo entre 100 y 500"))
    
    suma+=sueldos

    if sueldos>=100 and sueldos<=300:
        entre100y300+=1

    if sueldos>300:
        mas300+=1

    if sueldos<100 or sueldos>500:
        print("su sueldo no es valido")



print ("la cantidad de empleados q cobran entre 100 y 300 son: ",entre100y300, "los que ganan mas de 300 son: ", mas300, "en total se gastan: " ,suma)
