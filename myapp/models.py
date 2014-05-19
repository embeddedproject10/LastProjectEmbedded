from django.db import models

# Create your models here.
class Places(models.Model):
	name = models.CharField(max_length=50)
	direction = models.CharField(max_length=50)
	crowded = models.CharField(max_length=5,default="no")

	def __str__(self):
		return self.name





