"""3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas."""

lipos=[]
lineg=[]
def cargar():
    for i in range(10):
        ingresar=int(input("ingrese 10 numeros positivos o negativos"))
        if ingresar<0:
            lineg.append(ingresar)
        else:
            lipos.append(ingresar)
def printt():
    print("Lista positiva")
    for x in range(len(lipos)):
        print(lipos[x])
    print("Lista negativa")
    for t in range(len(lineg)):
        print(lineg[t])

cargar()
printt()