#1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
#deben procesar de acuerdo a lo siguiente:
#a. Ingresar nombre y nota de cada alumno (almacenar los datos en
#dos listas paralelas)
#b. Realizar un listado que muestre los nombres, notas y condición del
#alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
#igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
#si la nota es inferior a 4.
#c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.


nombres = []
notas = []
for i in range(4):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del alumno: "))
    nombres.append(nombre)
    notas.append(nota)
print("Listado de alumnos:")
contador_muy_bueno = 0
for i in range(4):
    nombre = nombres[i]
    nota = notas[i]
    if nota >= 8:
        condicion = "Muy Bueno"
        contador_muy_bueno += 1
    elif nota >= 4:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    print(f"Nombre: {nombre}, Nota: {nota}, Condición: {condicion}")
print(f"\nCantidad de alumnos con condición 'Muy Bueno': {contador_muy_bueno}")