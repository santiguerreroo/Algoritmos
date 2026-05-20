#Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.



num=int(input("ingrese numero 1")) 
num2=int(input("ingrese numero 2"))

if num>num2:    
    print("su suma es ", num+num2)
    print("su diferencia es ", num-num2)

else:
    print("su division es ", num/num2)
