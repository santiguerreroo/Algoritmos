#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
#en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
#cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
#puntos a procesar.

cant=int(input("Ingrese la cantidad de puntos a procesar"))
primerCuadrante=0
segundoCuadrante=0  
tercerCuadrante=0
cuartoCuadrante=0

for x in range(cant):
    x=int(input("Ingrese coordenada x"))
    y=int(input("Ingrese coordenada y"))

    if x>0 and y>0:
        primerCuadrante+=1

    if x<0 and y>0:
        segundoCuadrante+=1

    if x<0 and y<0:
        tercerCuadrante+=1

    if x>0 and y<0:
        cuartoCuadrante+=1

print("Puntos en el primer cuadrante:", primerCuadrante)
print("Puntos en el segundo cuadrante:", segundoCuadrante)
print("Puntos en el tercer cuadrante:", tercerCuadrante)
print("Puntos en el cuarto cuadrante:", cuartoCuadrante)