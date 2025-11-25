import json

cadena_json = '''
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

# Convertir la cadena a objeto Python
paises = json.loads(cadena_json)
print(f"Tipo de dato: {type(paises)}")  # list

# Imprimir cada país con su moneda
for pais in paises:
    print(f"{pais['nombre']} usa la moneda {pais['moneda']}")
