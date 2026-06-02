"""3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor."""

def calcular(base,altura):
    sup=base*altura
    return sup

base1=int(input("Ingrese la primer base"))
altura1=int(input("Ingrese la primer altura"))
base2=int(input("Ingrese la segunda base"))
altura2=int(input("Ingrese la segunda altura"))

if calcular(base1,altura1)>calcular(base2,altura2):
    print("el primer rectangulo tiene una superficie mayor con", calcular(base1,altura1))
else:
    print("el segundp rectangulo tiene una superficie mayor con", calcular(base2,altura2))