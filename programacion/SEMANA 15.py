informacion_personal = {
    "nombre": "Lucia Gomez",
    "edad": 37,
    "ciudad": "Quito",
    "profesion": "bachiller contador",
    "universida": "Estatal Amazonica",
    "estudio actual": "primer cemestre carrera de tecnologias de la informacion"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Bachiller Contador"

# Verificar si la clave "estudio actual" existe en el diccionario
if "estudio actual" in informacion_personal:
    print("La clave 'estudio actual' existe en el diccionario.")
else:
    informacion_personal["estudio actual"] = "primer cemestre carrera de tecnologias de la informacion"
    print("La clave 'estudio actual' fue agregada al diccionario.")

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" in informacion_personal:
    print("La clave 'telefono' existe en el diccionario.")
else:
    informacion_personal["telefono"] = "0994332688"
    print("La clave 'telefono' fue agregada al diccionario.")

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)