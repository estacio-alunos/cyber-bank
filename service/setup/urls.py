from django.urls import path
from . import views

app_name = 'setup'

urlpatterns = [
    path('', views.hello, name='index')
]
