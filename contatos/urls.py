from django.urls import path
from contatos.views import view_contatos

app_name = 'contatos'

urlpatterns = [
    path('', view_contatos, name='url_contatos'),
]
