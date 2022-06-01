import requests

from cursos.models import Avaliation

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP 
#print(avaliacoes.status_code)


# Acessando os dados da resposta 
print(avaliacoes.json())
print(type(avaliacoes.json()))


# GET Cursos 

headers = {'Authorization': 'Token dc2635b8fb223a39536aa03421bdb49aaffb4da2'}

cursos = requests.get('http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())