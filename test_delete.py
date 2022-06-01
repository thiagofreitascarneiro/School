import requests

headers = {'Authorization': 'Token 90b10b4b7ce63d323d5f4ed0c87ef65b0b046693'}

url_base_cource = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliation = 'http://localhost:8000/api/v2/avaliacoes/'


results = requests.delete(url=f'{url_base_cource}6/', headers=headers)

# Testing the HTTP code
assert results.status_code == 204

# test if the return content length is the same 0
assert len(results.text) == 0 

