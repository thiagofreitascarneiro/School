import requests

from cursos.models import Avaliation

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP 
#print(avaliacoes.status_code)


# Acessando os dados da resposta 
print(avaliacoes.json())
print(type(avaliacoes.json()))