from django.shortcuts import render
from .models import Pelicula
def home(request):
    xx=Pelicula.objects.all()
    return render(request,'home.html',{'peliculas':xx})
def detalles(request,i):
    x=Pelicula.objects.get(id=i)
    return render(request,'detalles.html',{'pelicula':x})
