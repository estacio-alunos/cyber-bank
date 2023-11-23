import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture
def user_default():
    user = User.objects.create_user(username='admin', password='carlos')
    return user


@pytest.mark.django_db
def test_create_cep(user_default):
    client = APIClient()

    response = client.post('/api/token/', data={
        'username': 'admin',
        'password': 'carlos',
    })

    assert response.status_code == 200
