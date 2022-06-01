import requests

headers = {'Authorization': 'Token 90b10b4b7ce63d323d5f4ed0c87ef65b0b046693'}

url_base_cource = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliation = 'http://localhost:8000/api/v2/avaliacoes/'

results = requests.get(url=url_base_cource, headers=headers)

# print(results.json())

# Tests if endpoint is correct

assert results.status_code == 200

# Test the registers callback
assert results.json()['count'] == 3

# tests if title of first cource is correct
assert results.json()['results'][0]['title'] == "Criação de APIs com Django REST Framework"