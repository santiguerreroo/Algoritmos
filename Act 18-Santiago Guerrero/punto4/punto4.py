"""4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras a o A."""

def contar(cadena):
    contador = 0
    for letra in cadena:
        if letra == "a" or letra == "A":
            contador += 1
    return contador
texto = input("Ingrese un texto: ")
  
print("La cantidad de letras 'a' o 'A' en el texto es: ", contar(texto))