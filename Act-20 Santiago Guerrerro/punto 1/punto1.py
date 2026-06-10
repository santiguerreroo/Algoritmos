"""1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=[&quot;enero&quot;, &quot;febrero&quot;, &quot;marzo&quot;, &quot;abril&quot;, &quot;mayo&quot;, &quot;junio&quot;]
print(&quot;Palabra con mas caracteres:&quot;,mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)"""


def largo (a1,a2,a3,a4,a5,a6):
    li=[a1,a2,a3,a4,a5,a6]
    mascorto=""
    for i in range(6):
        if len(li[i])>len(mascorto):
            mascorto=li[i]
    print("el mas largo es: ", mascorto)


largo("a","aa","aaa","aaaa","aaaaa","aaaaaa")
        
