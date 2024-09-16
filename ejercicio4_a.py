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
