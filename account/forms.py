from django import forms

class AddPlant(forms.ModelForm):

	class Meta:
		model = Plant
		fields = (
				'name',
				'photo',
				'sensor',
				'type_plant',
			)

class AddSensor(forms.ModelForm):

	class Meta:
		model = Sensor
		fields = (
				'name',
			)

