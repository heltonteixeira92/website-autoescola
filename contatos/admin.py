from django.contrib import admin # noqa
from .models import Horario


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dia', 'abre', 'fecha')
