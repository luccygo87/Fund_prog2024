# calcular las temperaturas de las siguientes ciudades principales del Ecuador

temperaturas = [
    [  # Ciudad Quito
        [10, 15, 20],  # Semana 1
        [25, 30, 35],  # Semana 2
        [31, 22, 19]   # Semana 3
    ],
    [  # Ciudad Guayaquil
        [15, 28, 32],  # Semana 1
        [21, 37, 41],  # Semana 2
        [10, 12, 18],  # Semana 3
        [11, 39, 23]   # Semana 4
    ],
    [  # Ciudad Cuenca
        [18, 30, 36],  # Semana 1
        [11, 27, 38]   # Semana 2
    ]
]

# CIudad de Quito
def promedio_temp_ciudad(arreglo_temperaturas, ciudad, semana):
    acumulador = 0
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador += arreglo_temperaturas[ciudad][semana][i]

    promedio = acumulador / len(arreglo_temperaturas[ciudad][semana])
    return promedio


resultado_prom = promedio_temp_ciudad(temperaturas, ciudad=0, semana=2)
print(resultado_prom)

# CIudad de Guayaquil
def promedio_temp_ciudad(arreglo_temperaturas, ciudad, semana):
    acumulador = 1
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador += arreglo_temperaturas[ciudad][semana][i]

    promedio = acumulador / len(arreglo_temperaturas[ciudad][semana])
    return promedio


resultado_prom = promedio_temp_ciudad(temperaturas, ciudad=1, semana=3)
print(resultado_prom)

# CIudad de Cuenca
def promedio_temp_ciudad(arreglo_temperaturas, ciudad, semana):
    acumulador = 2
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador += arreglo_temperaturas[ciudad][semana][i]

    promedio = acumulador / len(arreglo_temperaturas[ciudad][semana])
    return promedio


resultado_prom = promedio_temp_ciudad(temperaturas, ciudad=2, semana=1)
print(resultado_prom)
