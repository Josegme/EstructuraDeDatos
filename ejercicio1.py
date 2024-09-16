"""Ejercicio N1 - Python - Estructura de Datos"""
#Título del TP
print("===============================================================")
print("===========Universidad de Python - Inscripciones===============")
print("===============================================================")
print("")

#Primero solicita los datos Personales
nombre = input("Ingrese su Nombre: ")
edad = int(input("Ingrese su Edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")
matricula = float(input("Ingrese el monto de la matrícula: $"))
print("")

#Variable que muestra si posee Título Secundario - Booleano
posee_titulo_secundario = True

#Cuota (es igual a la matricula + 1000)
cuota = matricula + 1000

#Ahora informa sobre la materia "Python I"
materia = "Python I"
arancel_python_1 = 12000
costo_mensual = arancel_python_1 / 4 #Como es cuatrimestral le divido por 4

#Si paga en Efectivo se puede hacer un descuento del 15%
pago_en_efectivo = input("¿Desea pagar en efectivo? (Si/No): ").strip().lower()
if pago_en_efectivo == "si":
    descuento = costo_mensual*0.15
    cuota_final = costo_mensual - descuento
else:
    cuota_final = costo_mensual

    #IMprime los datos Solicitados
print("")
print("=======================================================")
print("============Datos De Ingreso===========================")
print("=======================================================")
print(f'Nombre Completo: {nombre}')
print(f'Fecha de Nacimiento: {fecha_nacimiento} y {edad} años')
print(f'Posee Título: {posee_titulo_secundario}')
print(f'Matricula: ${cuota:.2f}')
print(f'Arancel mensual materia {materia}: ${costo_mensual:.2f}.')
print(f'Arancel Mensual materia {materia} con descuento: ${cuota_final:.2f}')

