#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
#iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.


cant=int(input("Ingrese la cantidad de triangulos"))


triangulosEquilateros=0
triangulosIsosceles=0
triangulosEscalenos=0

for x in range(cant):
    lado1=int(input("Ingrese el lado 1 del triangulo"))
    lado2=int(input("Ingrese el lado 2 del triangulo"))
    lado3=int(input("Ingrese el lado 3 del triangulo"))

    if lado1==lado2 and lado2==lado3:
        print("El triangulo es equilatero")
        triangulosEquilateros+=1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("El triangulo es isosceles")
            triangulosIsosceles+=1
        else:
            print("El triangulo es escaleno")
            triangulosEscalenos+=1

print("La cantidad de triangulos equilateros es: ", triangulosEquilateros)
print("La cantidad de triangulos isosceles es: ", triangulosIsosceles)
print("La cantidad de triangulos escalenos es: ", triangulosEscalenos)