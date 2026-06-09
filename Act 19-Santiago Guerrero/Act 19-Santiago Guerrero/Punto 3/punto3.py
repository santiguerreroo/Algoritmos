"""3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto."""


def sumas (uno,dos,tres=0,cuatro=0,cinco=0):
    suma=(uno+dos+tres+cuatro+cinco)
    return suma

sumass=print(sumas(1,2))
sumass=print(sumas(1,2,3))
sumass=print(sumas(1,2,3,4))
sumass=print(sumas(1,2,3,4,5))

