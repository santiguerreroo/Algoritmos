#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.


lista=["Santi", "Soto", "Lolo", "Diego", "Pablo"]

contador=0
for i in lista:
    if len(i)>=5:
        contador+=1
        print("Nombre ",i, "tiene mas de 5 caracteres")
print("La cantidad de nombres con 5 o más caracteres es: ", contador)
