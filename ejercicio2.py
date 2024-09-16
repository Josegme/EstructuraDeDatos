"""Cargar la nota y obtener el promedio."""
print("****Nota-Promedio-Desempeño-Estado****")
print("**************************************")
print("")
#Ingresa el nombre del alumno
alumno = input("Ingrese su nombre: ")
#Solicitud de Notas de los Parciales.
nota_1er_parcial = float(input("Ingrese la nota del primer Parcial: "))
nota_2do_parcial = float(input("Ingrese la nota del segundo Parcial: "))

print("Estado del Segundo Parcial: ")
print("")
if nota_2do_parcial >= 7:
    print(f'{alumno} usted Aprobó el 2do Parcial.')
else:
    print(f'{alumno} usted Desaprobó el 2do Parcial.')

print("")
print("Desempeño del Alumno: ")
if nota_2do_parcial > nota_1er_parcial:
    print("El alumno mejoró su desempeño.")
elif nota_2do_parcial == nota_1er_parcial:
    print("Mantuvo la Nota")
else:
    print("Empeoró su Desempeño: ")

print("")
print("Informe del Estado del Alumno.")
promedio = (nota_1er_parcial + nota_2do_parcial)/2
if promedio >= 7:
    print(f'{alumno} Promocionó la Materia.')
elif 4 <= promedio < 7:
    print(f'{alumno} Debe rendir el Final.')
else:
    print(f'{alumno} Debe Recursar la Materia.')

print("Muchas Gracias.")
