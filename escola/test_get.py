import requests

headers = {'Authorization': 'Token dc2635b8fb223a39536aa03421bdb49aaffb4da2'}

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