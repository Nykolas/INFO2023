
from django.urls import path, include
from . import views

app_name='usuarios'

urlpatterns = [
    path('Registro', views.Registro.as_view(), name="registrar"),
]
