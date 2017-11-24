from django.db import models
import datetime

class Customer(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	licence = models.CharField(max_length=200)

	#customer constructor
	def __init__(self,name,address,phone_number,email,licence):
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.licence = licence

	def __str__(self):
		return self.name


class Booking(models.Model):
	customer = Customer()
	vehicle = Vehicle()
	depot = Depot()
	booking_time = datetime.datetime

	#def create_booking(self, customer, vehicle, depot, booking_time):

class Depot(models.Model):
	address = models.CharField(max_length=200)
	#inventory
	#schedule

class Vehicle(models.Model):
	depot = Depot()
	is_available = model.BooleanField(initial=True)
	type = models.CharField(max_length=200)
	license_plate = models.CharField(max_length=20)
	# schedule