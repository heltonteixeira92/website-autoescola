from django.contrib import admin
from .models import Postagem


@admin.register(Postagem)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicar', 'status', 'fonte')
    list_filter = ('status', 'criado', 'publicar', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicar'
    ordering = ('status', 'publicar')
