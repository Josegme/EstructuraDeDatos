"""=====Probando For con 1, 2, y 3 Parametros"""

#utilizando un parametro -> 1 parámetro (range(n)): Se usa para recorrer de 0 a n-1.

print("==========Promedio de Notas (con un parametro)==========")

suma_notas = 0 #Inicializamos el contador

for i in range(5): #este caso el for va a iterar de 0 a 4 (total 5 veces)
    nota = float(input('Ingrese la nota: '))
    suma_notas += nota

promedio = suma_notas/5

print(f'El promedio de las notas es: {promedio}')
print("="*40)

print("====Promedio de Notas (con 2 parametro)====")
#utilizando dos parametros -> 2 parámetros (range(start, stop)): Se usa para recorrer de start a stop-1.
#es decir establecemos donde comienza y donde termina de iterar

suma_notas2 = 0
cantidad_notas2 = 0

for i in range( 1 , 6): #este caso el for itera hasta 5
    notas2 = float(input('Ingrese la nota: '))
    suma_notas2 += notas2
    cantidad_notas2 += 1

promedio2 = suma_notas2/cantidad_notas2

print(f'El promedio de las notas es: {promedio2}')
print("=" * 40)

print("===Promedio de Notas (con 3 parametro)===")

#3 parámetros (range(start, stop, step)): Añade un paso step para avanzar de forma diferente en cada iteración.
suma_notas3 = 0
cantidad_notas3 = 0

for i in range(1 , 8, 2): #es decir que "saltea" o intercala 2 veces cuanto esta iterando 
    notas3 = float(input('Ingrese la nota: '))
    suma_notas3 += notas3 
    cantidad_notas3 += 1 #para que cuente las iteraciones dentro del rango

promedio3 = suma_notas3/cantidad_notas3

print(f'El promedio de las notas es {promedio3} ')
