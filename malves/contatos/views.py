from django.shortcuts import render
from .models import Horario, Contato
from django.http import JsonResponse


def view_contatos(request):
    horarios = Horario.objects.all()
    return render(request, 'contatos/contatos.html',
                  {'section': 'contatos', 'horarios': horarios})


def create_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        Contato.objects.create(
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
    return JsonResponse({"status": 'Success'})
