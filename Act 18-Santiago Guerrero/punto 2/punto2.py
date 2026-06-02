"""""2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida."""



def ordenar(v1,v2,v3):
    if v1<v2 and v1<v3 and v2<v3:
        print("ordenado de menor a mayor: ", v1,v2,v3)
    else:
        if v1<v1 and v1<v3 and v3<v2:
            print("ordenado de menor a mayor: ", v1,v3,v2)
        else:
            if v2<v1 and v2<v3 and v1<v3:
                print("ordenado de menor a mayor: ", v2,v1,v3)
            else:
                if v2<v1 and v2<v3 and v1>v3:
                    print("ordenado de menor a mayor: ", v2,v3,v2)
                else:
                    if v3<v1 and v3<v2 and v1<v2:
                        print("ordenado de menor a mayor: ", v3,v1,v2)
                    else:
                        print("ordenado de menor a mayor: ", v3,v2,v1)

def ingresar():
    v1=int(input("Ingrese el primer valor"))
    v2=int(input("Ingrese el segundo valor"))
    v3=int(input("Ingrese el tercer valor"))
    ordenar(v1,v2,v3)
    
ingresar()
                        
            
