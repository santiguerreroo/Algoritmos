"""Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias."""


def carga():
    candidato=[]
    for i in range(3):
        nom=input(F"Ingrese el nombre del candidato {i+1} ")
        votos=[] 
        prov=input(F"Ingrese el nombre de la provincia del candidato {nom} ") 
        vot=int(input(F"Ingrese la cantidad de votos a {nom} "))
        votos.append((prov,vot))
        voto=tuple(votos)
        candidato.append([nom,voto])
    return candidato

def imprimir(candidato):

    for nom,voto in candidato:
        print (nom,voto)


candidato=carga()
imprimir(candidato)