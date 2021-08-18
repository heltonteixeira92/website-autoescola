from django.db import models # noqa


class Horario(models.Model):
    dia = models.CharField(max_length=15)
    abre = models.CharField(max_length=2)
    fecha = models.CharField(max_length=2)

    def __str__(self):
        return self.dia
