"""1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor."""


def cargar():
    lista=[]
    for x in range(5):
        ent=int(input("ingrese 5 enteros"))
        lista.append(ent)
        lista1=tuple(lista)
    return lista1

def mayor(lista):
    mayor=lista[0]
    for entero in lista:
        if entero>mayor:
            mayor=entero
    print("El mayor elemento es: ",mayor)

def menor(lista):
    menor=lista[0]
    for entero in lista:
        if entero<menor:
            menor=entero
    print("El menor elemento es: ",menor)

lista=cargar()
mayor(lista)
menor(lista)