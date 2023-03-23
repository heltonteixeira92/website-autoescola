from django.urls import path
from malves.servicos.views import view_servicos


app_name = 'servicos'

urlpatterns = [
    path('', view_servicos, name='view_servicos'),
]
