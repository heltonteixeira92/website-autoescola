from django.contrib import admin # noqa
from .models import Horario, Contato


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dia', 'abre', 'fecha')


admin.site.register(Contato)
