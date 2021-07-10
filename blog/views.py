from django.shortcuts import render, get_object_or_404
from .models import Postagem


def post_list(request):
    postagens = Postagem.published.all()
    return render(request,
                  'blog/postagem/lista.html',
                  {'postagens': postagens})


def post_detail(request, year, month, day, postagem):
    postagem = get_object_or_404(Postagem, slug=postagem,
                                 status='publicado',
                                 publicar__year=year,
                                 publicar__month=month,
                                 publicar__day=day)
    return render(request,
                  'blog/postagem/detalhe.html',
                  {'postagem': postagem})
