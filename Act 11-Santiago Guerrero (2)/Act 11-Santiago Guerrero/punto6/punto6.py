#De un operario se conoce su sueldo y los años de antigüedad. Se pide
#confeccionar un programa que lea los datos de entrada e informe:
#a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
#años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
#años, otorgarle un aumento de 5 %.
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
#cambios.


num=int(input("ingrese sueldo")) 
num2=int(input("ingrese antigüedad")) 


if num<501 and num2>=10:    
    print("uds se merece un aumento, su nuevo sueldo es ", num*1.2)


else:
    if num<501 and num2<10:
        print("te mereces un aumento, su nuevo sueldo es " , num*1.05)

    else:
        print("su sueldo es ", num)