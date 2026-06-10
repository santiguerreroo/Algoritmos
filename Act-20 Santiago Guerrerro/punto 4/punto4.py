"""4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)"""

def mayor():
    eddad=[]
    for i in range(2):
        edades=int(input("ingrese las edades"))
        eddad.append(edades)
    
    for i in range(2):
        if eddad[i]>=18:
            print("La edad: ", i+1," es mayor o igual a 18")
    
mayor()