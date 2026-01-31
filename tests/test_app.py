import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'GARAGE 24' in rv.data

def test_catalogo_page(client):
    rv = client.get('/catalogo')
    assert rv.status_code == 200

def test_cadastro_carro_invalido(client):
    rv = client.post('/catalogo', data={
        'modelo': '',
        'ano': 1800,
        'preco': -1000,
        'imagem': 'url-invalida'
    })
    assert rv.status_code == 302

def test_404_error(client):
    rv = client.get('/pagina-inexistente')
    assert rv.status_code == 404
