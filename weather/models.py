from django.db import models
import json
# Create your models here.

class Weather(models.Model):
	name = models.CharField(max_length=20)
	country = models.CharField(max_length=20)
	coord = models.CharField(max_length=20)
	temperature = models.IntegerField()


def __str__(self):
	return self.name