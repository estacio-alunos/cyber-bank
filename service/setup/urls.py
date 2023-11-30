from django.urls import path
from . import views

app_name = 'setup'

urlpatterns = [
    path('', views.get, name='index'),
    path('/create', views.post, name='create'),
    path('/setups', views.post_get, name='patch')
]
