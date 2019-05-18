from django.contrib import admin
from .models import Plant, Sensor, Report

# Register your models here.
admin.site.register(Plant)
admin.site.register(Sensor)
admin.site.register(Report)