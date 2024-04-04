import requests

# URL del servidor FastAPI
url = 'http://localhost:8000/candidato'

# Datos para enviar en la solicitud POST
data = {
    "dni": "12345678A",
    "nombre": "Juan",
    "apellido": "Pérez"
}

# Realizar la solicitud POST al servidor FastAPI
response = requests.post(url, json=data)

# Verificar el resultado de la solicitud
if response.status_code == 200:
    print("Candidato creado exitosamente:")
    print(response.json())
else:
    print("Error al crear candidato:")
    print(response.text)