"""Promedio de notas de 5 alumnos y obtener el promedio"""
#PROFE PARA MI ESTA RARO EL ENUNCIADO CON EL EJEMPLO ASI QUE HICE 2 OPCIONES

print("==========Promedio de Notas==========")

suma_notas = 0 #Inicializamos el contador

for i in range(5):
    nota = float(input('Ingrese la nota: '))
    suma_notas += nota

promedio = suma_notas/5

print(f'El promedio de las notas es: {promedio}')
#Se va a mostrar como estaba en el ejemplo de lo que se espera obtener
#===================================================================

#LA OTRA OPCIÓN ES TOMAR LA NOTA DE 5 ALUMNOS Y CALCULAR EL PROMEDIO DE CADA UNO.
print("==========Promedio de notas de los Alumnos==========")
print("")
#Recorremos los 5 alumnos y calculamos el promedio
for i in range(5):
    nombre = input(f'Ingrese el nombre del alumno {i+1}: ')
    #el alumno debe ingresar sus notas
    nota_1 = float(input(f'Ingrese la nota del 1er Parcial de {nombre}: '))
    nota_2 = float(input(f'Ingrese la nota del 2do Parcial de {nombre}: '))
    #Calculamos el promedio
    promedio = (nota_1+nota_2)/2
    print(f'El promedio de {nombre} es: {promedio:.2f}')
    if promedio >= 7:
        print(f'{nombre} promocionó el Cuatrimestre.')
    elif (promedio >= 4 and promedio < 7) :
        print(f'{nombre} debe rendir el final.')
    else:
        print(f'{nombre} debe recursar la Materia.')
    
    print("_" * 40) #separador


