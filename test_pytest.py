import requests 

class TestCource:
    headers = {'Authorization': 'Token dc2635b8fb223a39536aa03421bdb49aaffb4da2'}
    url_base_cource = 'http://localhost:8000/api/v2/cursos/'

    def test_get_allCource(self):
        cource = requests.get(url=self.url_base_cource, headers=self.headers)

        assert cource.status_code == 200 
    
    def test_get_cource(self):
        cource = requests.get(url=f'{self.url_base_cource}2/', headers=self.headers)

        assert cource.status_code == 200 
    
    def test_post_cource(self):
        new = {
            "title": "Curso de porgramação Ruby 4",
            "url": "http://www.geekuniversity.com.br/cpr"
        }

        results = requests.post(url=self.url_base_cource, headers=self.headers, data=new)

        assert results.status_code == 201
        assert results.json()['title'] == new['title']
    
    def test_put_cource(self):
        atualized = {
            "title": "Novo Curso de Ruby",
            "url": "http://www.geekuniversity.com.br/ncr"
        }

        results = requests.put(url=f'{self.url_base_cource}31/', headers=self.headers, data=atualized)

        assert results.status_code == 200 
        assert results.json()['title'] == atualized['title']
    
    def test_put_title_cource(self):
        atualized = {
            "title": "Novo Curso de Ruby 2",
            "url": "http://www.geekuniversity.com.br/ncr2"
        }

        results = requests.put(url=f'{self.url_base_cource}2/', headers=self.headers, data=atualized)

        assert results.json()['title'] == atualized['title']

    def test_delete_cource(self):
        results = requests.delete(url=f'{self.url_base_cource}2/', headers=self.headers)

        assert results.status_code == 204 and len(results.text) == 0 
