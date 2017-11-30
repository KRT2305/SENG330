from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets

from django.db import models
from django.forms import ModelForm

from .models import Booking, Depot, Vehicle
from .managers import *
from .globals import TAXI_TYPES

import datetime

class CreateBookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ('depot', 'vehicle_type', 'start_time', 'end_time')

	depot_list = Depot.objects.depots()
	vehicle_list = TAXI_TYPES

	depot = forms.ChoiceField(choices=[(depot.address, depot.address) for depot in depot_list])
	vehicle_type = forms.ChoiceField(choices=[x for x in vehicle_list])
	start_time = forms.DateTimeField(widget=forms.DateTimeInput)
	end_time = forms.DateTimeField(widget=forms.DateTimeInput)

	# vehicle = Vehicle.objects.vehicles(depot, vehicle_type)
	# bookings = Booking.objects.bookings(depot)

	# for item in vehicle:
	# 	b_start = item.start_time - datetime.timedelta(days=2)
	# 	b_end = item.end_time + datetime.timedelta(days=2)




		# if item.Vehicle.v_type != v_type:
		# 	continue
		# b_start = item.start_time - datetime.timedelta(days=2)
		# b_end = item.end_time + datetime.timedelta(days=2)

		# if start_time > b_end or end_time < b_start:
		# 	return item.vehicle