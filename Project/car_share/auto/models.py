from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import UserManager

import datetime

#from django.utils.encoding import python_2_unicode_compatible

from .managers import *
from .globals import TAXI_TYPES


#  docs.djangoproject.com/en/1.11/ref/models/instances/#creating-objects


class Customer(User):
	objects = CustomerManager()

	class Meta:
		proxy = True  


class Depot(models.Model):
	address = models.CharField(max_length=200)
	name = models.CharField(max_length=200,default=' ')
	city = models.CharField(max_length=200,default=' ')
	state = models.CharField(max_length= 200,default=' ')
	
	objects = DepotManager()

	def __str__(self):
		return "{}-{}".format(self.name, self.city)
		# return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])


class Vehicle(models.Model):
	depot = models.ForeignKey(Depot, on_delete=models.PROTECT, related_name='vehicle')
	available = models.BooleanField(True)
	v_type = models.CharField(max_length=20, choices = TAXI_TYPES)
	license = models.CharField(max_length=200)

	objects = VehicleManager()

	def set_status(self, status):
		self.is_available = status

	def get_status(self):
		return self.is_available
	
	def __str__(self):
		return "{}\n{}\n{}".format(self.depot, self.license, self.v_type)
		# return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])


class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
	vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE, related_name='vehicle')
	depot = models.ForeignKey(Depot, on_delete=models.CASCADE, related_name='depot')
	start_time = models.DateTimeField(null = True)
	end_time = models.DateTimeField(null = True)
    
	objects = BookingManager()

	def __str__(self):
		return "{}\n{}\n{}".format(self.customer.username, self.vehicle.license, self.depot.name)


