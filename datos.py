import requests

# Define tu clave de API
api_key = 'tu_clave_de_api'

# Define los encabezados de la solicitud
headers = {
    'Authorization': f'key {api_key}'
}

# Realiza la solicitud a la API
response = requests.get("https://rebrickable.com/api/v3/lego/parts/", headers=headers)

# Verifica que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Filtra las piezas que sean de color "Rojo"
    red_pieces = [piece for piece in data['results'] if piece['color']['name'] == 'Red']
    print(red_pieces)
else:
    print("Error al obtener los datos")
