from django.shortcuts import render
from .models import Servicos


def view_servicos(request):
    servicos = Servicos.objects.all()
    context = {'section': 'servicos', 'servicos': servicos}
    return render(request, 'servicos/templates/servicos/servicos.html', context)
