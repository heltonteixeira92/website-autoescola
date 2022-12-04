from django.shortcuts import render
from django.http import HttpResponse # noqa
from malves.blog.views import Postagem
# Create your views here.


def home(request):
    latest_postagens = Postagem.published.order_by('-publicar')[:2]
    context = {'latest_postagens': latest_postagens, 'section': 'home'}
    return render(request, 'base/home.html', context)


def handler404(request, exception):
    context = {}
    response = render(request, 'base/error-404.html', context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, 'base/error-500.html', context=context)
    response.status_code = 500
    return response
