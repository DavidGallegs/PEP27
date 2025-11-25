import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

# Convertir a cadena JSON
pais_json = json.dumpsl(pais, indent=2, sort_keys=True, ensure_ascii=False)
print(pais_json)
