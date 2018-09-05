from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,Http404

from .models import Pelicula

def home(request):
	peliculas=Pelicula.objects.all()
	return render(request,'home.html',{'peliculas':peliculas})

def detalles(request,id):
	try:pelicula=Pelicula.objects.get(id=id)
	except Pelicula.DoesNotExist:raise Http404('No se ha encontrado la pelicula solicitada')
	return render(request,'detalles.html',{'pelicula':pelicula})
