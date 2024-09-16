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


