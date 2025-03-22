import json

# Cargar JSON
with open("personaje.json", "r", encoding="utf-8") as file:
    personaje = json.load(file)

# Mostrar datos del personaje
print(json.dumps(personaje, indent=4, ensure_ascii=False))
