from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Noticia
from .forms import Form_Alta

#CONTROLA SI EL USUARIO ESTA LOGEADO
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Noticia
	form_class = Form_Alta
	template_name = 'noticias/crear.html'
	success_url = reverse_lazy('noticias:listar_noticias')
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)


class ListarNoticias(ListView):
	model = Noticia
	template_name = 'noticias/listar.html'
	#POR DEFECTO ESTA VISTA MANDA AL TEMPLATE UNA VARIABLE
	#LLAMADA OBJECT_LIST, CON LA LISTA DE TODAS LAS NOTICIAS