from django.contrib import admin
from .models import Servicos


@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo_servico', 'subtitulo')
