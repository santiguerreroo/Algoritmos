"""2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""

def ingresar():
    li=[]
    for i in range(10):
        valor=int(input("ingrese sus 10 sueldos "))
        li.append(valor)
    return li

def mostrar_sueldos(li):
    for i in range(10):
        print("sueldo: ",i+1, li[i])

def mayor4000(li):
    contador=0
    for i in range(10):
        if li[i]>4000:
            contador=contador+1
    print("la cantidad de sueldos mayores a 4000 son: ", contador)

def promedio(li):
    suma=0
    for i in range(10):
        suma=suma+li[i]
    promedio=suma/10
    return promedio

def menorPro(li, promedio):
        for x in range(10):
            if li[x]<promedio:
                print("el sueldo N",x+1,"es menor al promedio")


lista=ingresar()
mostrar_sueldos(lista)
mayor4000(lista)
promedioo=promedio(lista)
print("promedio: ",promedioo)
menorPro(lista,promedioo)
