#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.

valoresNeg=0
valoresPos=0
valores15=0
valoresPares=0

for x in range(10):
    numeros=int(input("Ingrese los numeros"))

    if numeros>0:
        valoresPos+=1
        
    else:
        if numeros<0:
            valoresNeg+=1
    if numeros%15==0:
        valores15+=1
    if numeros%2==0:
        valoresPares+=numeros

    

print("la cantidad de valores negativos es: ", valoresNeg)
print("la cantidad de valores positivos es: ", valoresPos)
print("la cantidad de valores multiplos de 15 es: ", valores15)
print("el valor acumulado de los pares es: ", valoresPares)




