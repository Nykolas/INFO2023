
from django.urls import path, include
from . import views

app_name='noticias'

urlpatterns = [
    path('Crear', views.CrearNoticia.as_view(), name="crear_noticia"),
]
