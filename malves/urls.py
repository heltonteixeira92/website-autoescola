from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('malves.base.urls')),
    path('servicos/', include('servicos.urls')),
    path('contatos/', include('contatos.urls')),
    path('noticias/', include('blog.urls', namespace='blog')),
    path('dashboard/', include('dashboard.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )

handler404 = 'malves.base.views.handler404'
