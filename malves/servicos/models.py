from django.db import models # noqa
from django.utils.safestring import mark_safe # noqa


class Descricao(models.Model):
    item = models.CharField(max_length=15)


class Servicos(models.Model):
    titulo_servico = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo_servico

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'
