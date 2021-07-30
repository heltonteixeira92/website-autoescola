from django.db import models # noqa


class Servicos(models.Model):
    nome_servico = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=30)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
