# Definimos la matriz y el valor a buscar
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
valor_buscado = 5

# Inicializamos variables
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Salir del bucle interno si se encuentra el valor
    if fila_encontrada != -1:  # Salir del bucle exterior si se encontró el valor
        break

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")