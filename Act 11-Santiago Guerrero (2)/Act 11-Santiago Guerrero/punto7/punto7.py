#7. Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor
#y el menor de ellos)


num=int(input("ingrese numero 1")) 
num2=int(input("ingrese numero 2"))
num3=int(input("ingrese numero 3"))

if num>num2 and num>num3:
    print("el numero mayor es ", num)
else:
    if num2>num and num2>num3:
        print("el numero mayor es ", num2)   
    else:      
        print("el numero mayor es ", num3)

if num<num2 and num<num3:
    print("el numero menor es ", num)
else:
    if num2<num and num2<num3:
        print("el numero menor es ", num2)   
    else:      
        print("el numero menor es ", num3)