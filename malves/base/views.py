from django.shortcuts import render
from django.http import HttpResponse # noqa
from blog.models import Postagem
# Create your views here.


def home(request):
    latest_postagens = Postagem.published.order_by('-publicar')[:2]
    context = {'latest_postagens': latest_postagens, 'section': 'home'}
    return render(request, 'base/home.html', context)
