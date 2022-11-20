from django.db import models
from .baker import Baker

# Create your models here.
class Donut(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	baker = models.ForeignKey(
		Baker,
		on_delete=models.CASCADE,
		related_name='baked_donut'
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name}: {self.description}"

