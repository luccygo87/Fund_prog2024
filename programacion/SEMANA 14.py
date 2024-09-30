def calcular_descuento(precio_total, porcentaje_descuento=10):
    descuento = precio_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
precio1 = 1520  # precio total de la compra
porcentaje1 =  10  # Porcentaje de descuento
descuento1 = calcular_descuento(precio1)
precio_final1 = precio1 - descuento1

precio2 = 2000  # precio total de la compra
porcentaje2 = 15  # Porcentaje de descuento
descuento2 = calcular_descuento(precio2, porcentaje2)
precio_final2 = precio2 - descuento2

# Salida de resultados
print(f"precio total: {precio1}, Descuento: {descuento1}, precio final a pagar: {precio_final1}")
print(f"precio total: {precio2}, Descuento: {descuento2}, precio final a pagar: {precio_final2}")