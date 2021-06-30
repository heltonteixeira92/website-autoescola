from django.shortcuts import render


def view_contatos(request):
    return render(request, 'contatos/contatos.html',
                  {'section': 'contatos'})
