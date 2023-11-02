import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_create_cep():
    client = APIClient()

    user = User.objects.create_user(username='admin', password='carlos')

    response = client.post('/api/token/', data={
        'username': 'admin',
        'password': 'carlos',
    })

    assert response.status_code == 200
