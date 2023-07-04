from django.shortcuts import render

# Create your views here.

def Catalogo(request):

	return render(request, 'productos/catalogo.html')