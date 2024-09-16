"""Ejercicio 4-d - Costo del Comedor"""

print("====== Costo del Comedor ======")

print("Día\tCosto Total")  
costo_por_dia = 1250

# Recorremos los días del 1 al 6 (Lunes a Sábado)
for dia in range(1 , 7 ): #para recorrer 6 días
    costo_total = dia * costo_por_dia 
    print(f'{dia}\t${costo_total}')
