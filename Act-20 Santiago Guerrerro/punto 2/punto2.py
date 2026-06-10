"""2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado."""
articulos=[]
precios=[]
def ingresar():

    for i in range (5):
        art=input("Ingrese su articulo ")
        pre=int(input("Ingrese su precio "))
        precios.append(pre)
        articulos.append(art)
    
def printt():
    print("Los articulos y sus precios son: ")
    for i in range (5):
        print(articulos[i],precios[i])
def mayor():
    mayor=0
    for i in range (5):
        if precios[i]>mayor:
            mayor=precios[i]
    print("El que mayor precio tiene es el: ",articulos[i])

def igual():
    igual=int(input("Ingrese un precio a buscar"))
    for i in range (5):
        if precios[i]<=igual:
            print("el producto: ", articulos[i],"tiene un precio igual o menor a tu precio objetivo")

ingresar()
print()
mayor()
igual()