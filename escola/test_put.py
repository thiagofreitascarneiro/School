import requests

headers = {'Authorization': 'Token 90b10b4b7ce63d323d5f4ed0c87ef65b0b046693'}

url_base_cource = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliation = 'http://localhost:8000/api/v2/avaliacoes/'


cource_atualized = {
    "title": "React Ignite Bootcamp",
    "url": "http://app.rocketseat.com.br/ncs3"
}

# seeking out the cource with ID 3
# cource = requests.get(url=f'{url_base_cource}3/', headers=headers)
# print(cource.json())


results = requests.put(url=f'{url_base_cource}3/', headers=headers, data=cource_atualized)

# Testing status code HTTP 
assert results.status_code == 200

# Testing the title 
assert results.json()['title'] == cource_atualized['title']