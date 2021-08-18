from django.shortcuts import render
from .models import Horario


def view_contatos(request):
    horarios = Horario.objects.all()
    return render(request, 'contatos/contatos.html',
                  {'section': 'contatos', 'horarios': horarios})
