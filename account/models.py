from django.db import models
import os

from django.conf import settings


def get_image_path(instance, filename):
    return 'plants/{}'.format(filename)

# Create your models here.
class Sensor(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Plant(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE, null=True, blank=True)
	type_plant = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Report(models.Model):
	sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
	temp = models.IntegerField()
	hum_soil = models.IntegerField()
	hum_air = models.IntegerField()
	light = models.IntegerField()

	def __str__(self):
		return self.sensor.name