from django.db import models

# Create your models here.

class Producto(models.Model):
	precio = models.DecimalField(max_digits=10, decimal_places = 2)
	nombre = models.CharField(max_length = 120)
	descrpcion = models.TextField()
	stock = models.IntegerField()

	def __str__(self):
		return self.nombre