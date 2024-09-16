"""Ejercicio 3"""
#Asignación del Aula
print("==========AULA=========")
dia_cursada = int(input("Ingrese el Día de la Cursada - 1 (Lunes) a 6 (Sábados): "))
if dia_cursada % 2 == 0:
    aula = "A-300"
elif dia_cursada % 2 != 0:
    aula = "A-315"
else:
    print("Ingrese un día válido.")

print(f'Aula: {aula}')

#Descuento
print("====Descuento====")
turno = input("Ingrese el Turno (Mañana-Tarde-Noche):").strip().lower()
cantidad_materias = int(input("Ingrese la cantidad de Materias: "))
cuota = float(input("Ingrese el valor de la Cuota: $"))
#se calcula el Descuento
if turno == "tarde" and cantidad_materias > 3:
    descuento = cuota * 0.25
else:
    descuento = cuota * 0.05
#cuota final
cuota_final = cuota - descuento

print(f'El valor de la cuota fina con descuento es: ${cuota_final:.2f}')

#Valor del Estacionamiento según el Vehículo.
vehiculo = input("Ingrese el Vehículo en el que Ingresa (Auto-Moto-Bicicleta): ").strip().lower()

if vehiculo == "auto" or vehiculo == "moto":
    costo_estacionamiento = 300
elif vehiculo == "bicicleta":
    costo_estacionamiento = 50
else:
    costo_estacionamiento = 0
    print("Ingresa sin vehículo.")

print(f'El costo de Estacionamiento para {vehiculo.capitalize()} es: ${costo_estacionamiento}')
print("Muchas Gracias por Asistir a Nuestra Universidad. ")