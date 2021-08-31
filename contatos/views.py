from django.shortcuts import render
from .models import Horario
from .forms import ContatoForm


def view_contatos(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contatos/sucesso.html')
    form = ContatoForm()
    horarios = Horario.objects.all()
    return render(request, 'contatos/contatos.html',
                  {'section': 'contatos', 'horarios': horarios, 'form': form})
