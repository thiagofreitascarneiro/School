import requests

headers = {'Authorization': 'Token dc2635b8fb223a39536aa03421bdb49aaffb4da2'}

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