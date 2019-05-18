from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^(?P<plant_id>[0-9]+)/$', views.plant, name="plant"),
	url(r'^(?P<plant_id>[0-9]+)/graphs/$', views.plant_graphs, name="plant_graphs"),
]