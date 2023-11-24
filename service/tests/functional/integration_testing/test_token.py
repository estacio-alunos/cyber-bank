import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def client() :    
    return APIClient()

@pytest.fixture
def auth():
    return User.objects.create_user(username='admin', password='carlos')

@pytest.mark.django_db
def test_retorna_acesso_negado_para_usuario_inexistent(client):
    response = client.post('/api/token/', data={
        'username': 'usuario_inexistent',
        'password': 'senha',
    })

    assert response.status_code == 401

@pytest.mark.django_db
def test_verifica_a_existencia_de_access_e_refresh_token(client, auth):
    response = client.post('/api/token/', data={
        'username': 'admin',
        'password': 'carlos',
    })

    assert 'access' in response.data
    assert 'refresh' in response.data
