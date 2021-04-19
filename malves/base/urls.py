from django.urls import path
from malves.base.views import home


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
