from django.shortcuts import render


def view_servicos(request):
    return render(request, 'servicos/servicos.html')
