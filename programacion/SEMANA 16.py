# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    file.write('Nota 1: Comprar comida para la despensa.\n')
    file.write('Nota 2: Pagar la tarjeta de crédito.\n')
    file.write('Nota 3: Leer capítulo 3 del libro "El Señor de los Anillos".\n')

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea
    for line in file:
        print(line.strip())  # Mostrar cada línea en consola
