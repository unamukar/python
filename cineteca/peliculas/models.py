from django.db import models

# Create your models here.

class Pelicula(models.Model):
	titulo=models.CharField(max_length=90)
	director=models.CharField(max_length=90)
	actor_principal=models.CharField(max_length=90)
	actriz_principal=models.CharField(max_length=90)
	genero=models.CharField(max_length=90)
	pais=models.CharField(max_length=90)
	fecha_estreno=models.IntegerField()
	premios=models.ManyToManyField('Premio',blank=True)

class Premio(models.Model):
	premio=models.CharField(max_length=90)
	def __str__(self):return self.premio
