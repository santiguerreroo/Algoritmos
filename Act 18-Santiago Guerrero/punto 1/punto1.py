"""1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)"""


def cargar():

    v1=int(input("Ingrese el primer valor"))
    v2=int(input("Ingrese el segundo valor"))
    v3=int(input("Ingrese el tercer valor"))
    print ("El menor es: ")
    if v1<v2 and v1<v3 :
        print(v1)
    else:
        if v2<v3:
            print(v2)
        else:
            print(v3)

cargar()
cargar()

