from django.db import models
from django.db import connection
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import UserManager
#  docs.djangoproject.com/en/1.11/ref/models/instances/#creating-objects

class CustomerManager(models.Manager):
	def create_customer(self, name, address, phone_number, email, license):
		customer = self.create(name=name, address=address, phone_number=phone_number, email=email, license=license)
		return customer

class Customer(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	license = models.CharField(max_length=200)

	objects = CustomerManager()

	'''
	#customer constructor
	def __init__(self, name, address, phone_number, email,licence):
		self.name = name
		self.address = address
		self.phone_number = phone_number
		self.email = email
		self.licence = licence
	'''
	
	# to string
	def __str__(self):
		output = ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
		return output


class DepotManager(models.Manager):
	def create_depot(self, address):
		depot = self.create(address=address)
		return depot

class Depot(models.Model):
	address = models.CharField(max_length=200)

	objects = DepotManager()

	#def __init__(self, address):
	#	self.address = address
	
	'''
	Might want to reconsider making depot aware of schedule, since we could
	add a way for schedule to be viewed from admin page. Then we add a way
	to search for schedule by depot. ie Schedule knows about depot, but depot
	doesn't know about schedule.
	
	Add a queury so grabbing all vehicles associated with it.
	'''
	# to string
	def __str__(self):
		return ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
		
class vehicleManager(models.Manager):
	def create_vehicle(self, depot, available, v_type, license):
		vehicle = self.create(depot=depot, available=available, v_type=v_type, license=license)

		return vehicle

class Vehicle(models.Model):
	depot = models.ForeignKey(Depot, on_delete=models.PROTECT)
	available = models.BooleanField(True)
	v_type = models.CharField(max_length=200)
	license = models.CharField(max_length=200)

	objects = vehicleManager()

	'''
	def __init__(self, depot, available, v_type, license):
		self.depot = depot
		self.available = available
		self.v_type = v_type
		self.license = license
	'''

	def set_status(self, status):
		self.is_available = status

	def get_status(self):
		return self.is_available
	
	# to string
	def __str__(self):
		output = ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
		return output

class BookingManager(models.Manager):
	def create_booking(self, customer, vehicle, depot, booking_time):
		booking = self.create(customer=customer, vehicle=vehicle, depot=depot, booking_time=booking_time)

		return booking

class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	depot = models.ForeignKey(Depot, on_delete=models.CASCADE)
	booking_time = models.DateTimeField('date booked')
	
	objects = BookingManager()

	# to string
	def __str__(self):
		output = ''.join(['{}:: {}\n'.format(attr, value) for attr, value in self.__dict__.items()])
		return output

class ProfileManager(models.Manager):
	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, *args, **kwargs):
	    # ignore if this is an existing User
	    if not created:
	        return
	    Profile.objects.create(user=instance)
	post_save.connect(create_profile, sender=User)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
    	 instance.profile.save()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    
    
    objects = ProfileManager()


   # post_save.connect(create_profile, sender=User)

  
  


'''
DO WE ACTUALLY NEED A SCHEDULE CLASS??? (I'm thinking not)

Might make more sense to have different queries which fetch
bookings based on Customer(for the.. customer) or Depot(for the employee)


DO WE NEED A SUBSCRIPTION CLASS?? (Possibly)

But what do we want it to do?

We can assume that payment might be done in person by the employees
as this is not really within the scope of the project.
'''


