#crear una matriz bidimensional 3x3
def bubble_sort(fila):
    """Ordena una fila usando el algoritmo Bubble Sort."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambiar
    return fila

def main():
    # Definimos una matriz 3x3
    matriz = [
        [9, 7, 5],
        [3, 1, 4],
        [6, 8, 2]
    ]