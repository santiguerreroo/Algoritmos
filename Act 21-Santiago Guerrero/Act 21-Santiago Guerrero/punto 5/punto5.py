"""Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15."""


def carga():
    producto=[]
    for i in range(5):
        nom=input(F"Ingrese el nombre del producto {i+1} ")
        pre=int(input(F"Ingrese el precio del producto {nom} ") )
        producto.append((nom,pre))
    return producto

def listar(producto):
        for nom,pre in producto:
            print(nom,pre)

def comp(producto):
     for i in range(5):
          if producto[i][1]>=10 and producto[i][1]<=15:
               print(F"El producto {producto[i][0]} tiene un precio entre 10 y 15")

producto=carga()
listar(producto)
comp(producto)