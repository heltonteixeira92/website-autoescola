from django.urls import path
from malves.contatos.views import view_contatos, create_contact

app_name = 'contatos'

urlpatterns = [
    path('', view_contatos, name='url_contatos'),
    path('create_contact/', create_contact, name='create_contact'),
]
