from django.contrib import admin

# Register your models here.

from .models import Pelicula

@admin.register(Pelicula)

class GestionPeliculas(admin.ModelAdmin):
	lista=['titulo','director','actor_principal','genero']
