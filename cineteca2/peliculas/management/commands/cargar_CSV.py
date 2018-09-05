from csv import DictReader
from django.core.management import BaseCommand
from peliculas.models import Pelicula,Premio

PREMIOS=['Mejor pelicula','Mejor director','Mejor guion','Mejor actor','Mejor actriz']

class Command(BaseCommand):
    def handle(self,*args,**options):
        for x in PREMIOS:
            y=Premio(nombre=x)
            y.save()
        for x in DictReader(open('../peliculas.csv')):
            p=Pelicula()
            p.titulo=x['Titulo']
            p.director=x['Director']
            p.actor_principal=x['Actor principal']
            p.actriz_principal=x['Actriz principal']
            p.genero=x['Genero']
            p.pais=x['Pais']
            p.fecha_estreno=x['Fecha de estreno']
            p.save()
            premios=x['Premios']
            lista=[y for y in premios.split('|') if y]
            for y in lista:
                z=Premio.objects.get(nombre=y)
                p.premios.add(z)
            p.save()
