from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant
import json

# Create your views here.
def home(request):
	template_name = "account/home.html"
	plants = Plant.objects.all()
	return render(request, template_name, context={'plants':plants})

def plant(request, plant_id):
	template_name = 'account/plant.html'
	plant = Plant.objects.get(id=plant_id)
	sensor = plant.sensor
	if len(sensor.report_set.all()):
		report = sensor.report_set.latest('id')	
		context = {
			"plant":plant,
			"report_temp":report.temp,
			"report_hum_soil":report.hum_soil,
			"report_hum_air":report.hum_air,
			"report_light":report.light,	
		}
	else:
		context = {
			"plant":plant,
		}
	return render(request, template_name, context)

def plant_graphs(request, plant_id):
	template_name = 'account/plant_graphs.html'
	plant = Plant.objects.get(id=plant_id)
	sensor = plant.sensor
	reports = sensor.report_set.all()
	last7_days_temp = []
	for report in list(reversed(reports))[:7]:
		last7_days_temp.append(report.temp)
	context = {
		"last7_days_temp":json.dumps(last7_days_temp),
		"day":last7_days_temp[0]
	}
	return render(request, template_name, context)