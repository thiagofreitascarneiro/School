import requests

headers = {'Authorization': 'Token 90b10b4b7ce63d323d5f4ed0c87ef65b0b046693'}

url_base_cource = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliation = 'http://localhost:8000/api/v2/avaliacoes/'


new_cource = {
    'title': 'Gerência Ágil de Projetos com Scrum',
    'url': 'http://www.geekuniversity.com.br/scrum'
}

results = requests.post(url=url_base_cource, headers=headers, data=new_cource)

# Testing the cod status HTTP 201
assert results.status_code == 201

# Testing if return cource title is the same of solicited
assert results.json()['title'] == new_cource['title']