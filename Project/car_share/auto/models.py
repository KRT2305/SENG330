from django.db import models
from django.contrib.auth.models import User

from .managers import *

import datetime

#  docs.djangoproject.com/en/1.11/ref/models/instances/#creating-objects


class Customer(User):
	objects = CustomerManager()

	class Meta:
		proxy = True
		ordering = ('first_name')	


class Depot(models.Model):
	address = models.CharField(max_length=200)

	objects = DepotManager()

	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])


class Vehicle(models.Model):
	depot = models.ForeignKey(Depot, on_delete=models.PROTECT, related_name='vehicle')
	available = models.BooleanField(True)
	v_type = models.CharField(max_length=200)
	license = models.CharField(max_length=200)

	objects = VehicleManager()

	def set_status(self, status):
		self.is_available = status

	def get_status(self):
		return self.is_available
	
	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])


class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
	depot = models.ForeignKey(Depot, on_delete=models.CASCADE, related_name='depot')
	booking_time = models.DateTimeField('date booked')
	
	objects = BookingManager()

	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])



