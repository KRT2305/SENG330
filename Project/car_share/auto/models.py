from django.db import models
import datetime

class Customer(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	licence = models.CharField(max_length=200)

	#customer constructor
	def __init__(self, name, address, phone_number, email,licence):
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.licence = licence

	# just playing around with this..

	'''
	def __iter__(self):
		for attr, value in self.__dict__.iteritems():
			yield attr, value
	'''
	# to string
	def __str__(self):
		output = ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
		return output


class Depot(models.Model):
	address = models.CharField(max_length=200)
	
	'''
	Might want to reconsider making depot aware of schedule, since we could
	add a way for schedule to be viewed from admin page. Then we add a way
	to search for schedule by depot. ie Schedule knows about depot, but depot
	doesn't know about schedule.
	
	Add a queury so grabbing all vehicles associated with it.
	'''
	

class Vehicle(models.Model):
	depot = models.ForeignKey(Depot, on_delete=models.PROTECT)
	available = models.BooleanField(True)
	v_type = models.CharField(max_length=200)
	license = models.CharField(max_length=200)
	# schedule

	def __init__(self, depot, available, v_type, license):
		self.depot = depot
		self.available = available
		self.v_type = v_type
		self.license = license

	def set_status(self, status):
		self.is_available = status

	def get_status(self):
		return self.is_available

class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	depot = models.ForeignKey(Depot, on_delete=models.CASCADE)
	booking_time = models.DateTimeField('date booked')
	
	def __init__(self, customer, vehicle, depot, date):
		self.customer = customer
		self.vehicle = vehicle
		self.depot = depot
		self.booking_time = date
