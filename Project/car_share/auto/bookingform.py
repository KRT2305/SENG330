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

class DeleteBooking(forms.ModelForm):

	#gets request.user as the user id to query the bookings
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(DeleteBooking, self).__init__(*args, **kwargs)
		self.fields['booking'] = forms.ChoiceField(choices=[(created_booking.vehicle,created_booking.vehicle) for created_booking in booking_list])

	

	
