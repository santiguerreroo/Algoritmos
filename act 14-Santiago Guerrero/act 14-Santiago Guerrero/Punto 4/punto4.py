#5. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#altas que el promedio y cuántas más bajas.

alturas=[]

for x in range(5):
    valor=float(input("Ingrese las 5 alturas"))
    alturas.append(valor)

promedio=0

for i in range(5):
    promedio+=alturas[x]

promedio=promedio/5


menorAltura=0
for i in alturas:
    if i<promedio:
        menorAltura+=1


mayorAltura=0
for i in alturas:
    if i>promedio:
        mayorAltura+=1

print("El promedio de las alturas es: ", promedio)
print("La cantidad de personas con altura menor al promedio es: ", menorAltura)
print("La cantidad de personas con altura mayor al promedio es: ", mayorAltura)