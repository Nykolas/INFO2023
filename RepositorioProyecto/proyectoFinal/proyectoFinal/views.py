from django.shortcuts import render


def Home(request):

	return render(request,'inicio.html')


def Segunda_vista(request):

	return render(request,'segunda_pagina.html')