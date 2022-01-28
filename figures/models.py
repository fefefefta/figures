from django.db import models

# Create your models here.

class Client(models.Model):
	ip = models.CharField(max_length=15, blank=True)
	name = models.CharField(max_length=30)

	def __str__(self):
		return f'Client {self.name}, ip:{self.ip}'


class Circle(models.Model):
	CIRCLE_TYPES = (
		('O', 'Ordinary'),
		('R', 'Rare'),
		('U', 'Unique'),
	)
	name = models.CharField(max_length=30, unique=True)
	circle_type = models.CharField(max_length=1, choices=CIRCLE_TYPES)
	owner = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True)
	sending_date = models.DateTimeField(null=True)

	def __str__(self):
		return f'circle {self.name}'
