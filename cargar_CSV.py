from csv import DictReader
from django.core.management import BaseCommand
from peliculas.models import Pelicula,Premio

PREMIOS=['Mejor pelicula','Mejor director','Mejor guion','Mejor actor','Mejor actriz']

class Command(BaseCommand):
    def handle(self, *args, **options):
        for nombre in PREMIOS:
            premio=Premio(premio=nombre)
            premio.save()
        for registro in DictReader(open('../peliculas.csv')):
            pelicula=Pelicula()
            pelicula.titulo=registro['Titulo']
            pelicula.director=registro['Director']
            pelicula.actor_principal=registro['Actor principal']
            pelicula.actriz_principal=registro['Actriz principal']
            pelicula.genero=registro['Genero']
            pelicula.pais=registro['Pais']
            pelicula.fecha_estreno=registro['Fecha de estreno']
            pelicula.save()
            nombres=registro['Premios']
            premios=[nombre for nombre in nombres.split('|') if nombre]
            for premio in premios:
                p=Premio.objects.get(premio=premio)
                pelicula.premios.add(p)
            pelicula.save()
