from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets

from django.db import models
from django.forms import ModelForm

from .models import Booking, Depot, Vehicle
from .managers import *
from .globals import TAXI_TYPES, DEPOTS

import datetime

class CreateBookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ('vehicle_type', 'start_time', 'end_time')
		exclude = ('user',)
		#widgets = { 'start_date': forms.DateTimeInput(attrs={'class':'datetime-input'})}

	depot_list = Depot.objects.depots()
	vehicle_list = Vehicle.objects.vehicles()

	depot = forms.ChoiceField(choices=[(depot.address,depot.address) for depot in depot_list])
	vehicle_type = forms.ChoiceField(choices=[(vehicle_type.v_type,vehicle_type.v_type) for vehicle_type in vehicle_list])
	start_time = forms.DateTimeField()
	end_time = forms.DateTimeField()


	
	
	

	
