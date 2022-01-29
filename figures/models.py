from django.db import models

# Create your models here.

class Client(models.Model):
	ip = models.CharField(max_length=15, blank=True)
	name = models.CharField(max_length=30)

	def __str__(self):
		return f'Client {self.name}, ip:{self.ip}'


class Circle(models.Model):
	FTYPES = (
		('O', 'Ordinary'),
		('R', 'Rare'),
		('U', 'Unique'),
	)
	name = models.CharField(max_length=30, unique=True)
	ftype = models.CharField(max_length=1, choices=FTYPES)
	owner = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True)
	sending_date = models.DateTimeField(null=True)

	def __str__(self):
		return f'circle {self.name}'

	@classmethod # TODO: move that classmethod to the parent class Figure when it created	
	def not_sended_figures_by_types(cls):
		ordinary_figures = cls.objects.filter(ftype='O', owner=None).count()
		rare_figures = cls.objects.filter(ftype='R', owner=None).count()
		unique_figures = cls.objects.filter(ftype='U', owner=None).count()

		return ordinary_figures, rare_figures, unique_figures
