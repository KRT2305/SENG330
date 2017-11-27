from django.db import models
from django.contrib.auth.models import User
from django.db import connection
import datetime

#  docs.djangoproject.com/en/1.11/ref/models/instances/#creating-objects


'''
class CustomerManager(models.Manager):
	def create_customer(self, name, address, phone_number, email, license):
		return self.create(name=name, address=address, phone_number=phone_number, email=email, license=license)
#'''

class CustomerManager(models.Manager):
	def create_customer(self, username, first_name, last_name, email, password):
		return self.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

class Customer(User):
	objects = CustomerManager()

	class Meta:
		proxy = True
		ordering = ('first_name', )
'''
class Customer(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	license = models.CharField(max_length=200)

	objects = CustomerManager()
	
	# to string (mostly for debugging)
	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
#'''

#class DepotQuerySet(models.QuerySet):
	

class DepotManager(models.Manager):
	def create_depot(self, address):
		return self.create(address=address)

class Depot(models.Model):
	address = models.CharField(max_length=200)

	objects = DepotManager()

	'''
	Might want to reconsider making depot aware of schedule, since we could
	add a way for schedule to be viewed from admin page. Then we add a way
	to search for schedule by depot. ie Schedule knows about depot, but depot
	doesn't know about schedule.
	
	Add a query so grabbing all vehicles associated with it.
	'''

	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
'''NOPENOPENOPE
class VehicleQuerySet(models.QuerySet):
	def get_by_depot(self, location):
		return self.filter(depot
'''		
class VehicleManager(models.Manager):
	def create_vehicle(self, depot, available, v_type, license):
		return self.create(depot=depot, available=available, v_type=v_type, license=license)

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

class BookingManager(models.Manager):
	def create_booking(self, customer, vehicle, depot, booking_time):
		return self.create(customer=customer, vehicle=vehicle, depot=depot, booking_time=booking_time)

class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
	depot = models.ForeignKey(Depot, on_delete=models.CASCADE, related_name='depot')
	booking_time = models.DateTimeField('date booked')
	
	objects = BookingManager()

	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])

'''
DO WE ACTUALLY NEED A SCHEDULE CLASS??? (I'm thinking not)

Might make more sense to have different queries which fetch
bookings based on Customer(for the.. customer) or Depot(for the employee)


DO WE NEED A SUBSCRIPTION CLASS?? (Possibly)

But what do we want it to do?

We can assume that payment might be done in person by the employees
as this is not really within the scope of the project.
'''


