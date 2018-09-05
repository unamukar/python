from django.db import models

# Create your models here.

class Pelicula(models.Model):
	GENEROS=[('C','Comedia'),('D','Drama'),('T','Terror')]
	titulo=models.CharField(max_length=90)
	director=models.CharField(max_length=90)
	actor_principal=models.CharField(max_length=90)
	genero=models.CharField(choices=GENEROS,max_length=1)
	pais=models.CharField(max_length=90)
	fecha_estreno=models.DateTimeField()
	comentarios=models.TextField()
	premios=models.ManyToManyField('Premio',blank=True)

class Premio(models.Model):
	premio=models.CharField(max_length=90)
	def __str__(self):return self.premio
