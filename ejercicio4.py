"""Ejercicio 4 -> listado de Aulas """
print("====Listado de AULAS====")

# Asignación del Aula para cada día
print("Día\tAula")  # Encabezado de la tabla con \t para tabulación

# Recorremos los días del 1 al 6 (Lunes a Sábado)
for dia_cursada in range(1, 7):
    # Determinamos el aula según si el día es par o impar
    if dia_cursada % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    
    # Imprimimos cada día junto con su aula correspondiente
    print(f"{dia_cursada}\t{aula}")

print("_"*40)

"""Ejercicio 4_b: Carga de Edades"""
print("==========Carga de Edades==========")
print("")

# Inicializamos el contador (Intentos no válidos)
contador = 0
# Bucle para Solicitar la edad y contar los intentos no válidos
while True:
    try: 
        edad = int(input("Ingrese una edad mayor o igual a 18: "))
        #If else para verificar la edad y contar
        if edad < 18:
            print("Error! Debe ingresar una edad mayor o igual a 18.")
            contador += 1  #Incrementamos el contador de intentos no válidos
        else:
            print(f"La edad ingresada es: {edad}")
            break #para cortar el bucle si ingresa edad válida
    except ValueError: #con ValueError -> Capturamos errores si el usuario ingresa algo que no sea un número y contamos
        print("Error! Debe ingresar un número válido.")
        contador += 1

# Imprimimos la cantidad de ingresos inválidos
print(f"Se han ingresado {contador} intentos erroneos.")

print("_"*40)

"""Promedio de notas de 5 alumnos y obtener el promedio"""
#PROFE PARA MI ESTA RARO EL ENUNCIADO CON EL EJEMPLO ASI QUE HICE 2 OPCIONES

print("==========Promedio de Notas==========")

suma_notas = 0 #Inicializamos el contador

for i in range(5):
    nota = float(input('Ingrese la nota: '))
    suma_notas += nota

promedio = suma_notas/5

print(f'El promedio de las notas es: {promedio}')
print("_"*40)

"""Ejercicio 4-d - Costo del Comedor"""

print("====== Costo del Comedor ======")

print("Día\tCosto Total")  
costo_por_dia = 1250

# Recorremos los días del 1 al 6 (Lunes a Sábado)
for dia in range(1 , 7 ): #para recorrer 6 días
    costo_total = dia * costo_por_dia 
    print(f'{dia}\t${costo_total}')
    