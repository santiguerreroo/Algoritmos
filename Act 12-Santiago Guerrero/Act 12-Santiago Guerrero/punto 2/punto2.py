#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.
suma=0
cant=int(input("Ingrese la cantidad de personas"))

for x in range(cant):
    
    altura=int(input("Ingrese la altura de la persona "))
    suma+=altura

print("la altura promedio es de: ",suma/cant )