from django.test import TestCase
from .models import Customer, Vehicle, Depot, Booking

import datetime

def make_user():
	c = Customer.objects.create_customer('testemail@email.com', 'test', 'account', '100', 'password')
	c.save()
	print(c.id)
	
def make_depot():
	d = Depot.objects.create_depot('1520Pear', 'Pear', 'vic', 'BC')
	d.save()

def make_vehicle():
	d = Depot.objects.get(id=3)
	v = Vehicle.objects.create_vehicle(d, True, 'truck', 'K0SA21H')
	v.save()

def make_booking():
	c = Customer.objects.get(id=5)
	c.email = "1000"
	d = Depot.objects.get(id=3)
	v = Vehicle.objects.get(id=1)
	now = datetime.datetime.now()
	tom = now + datetime.timedelta(days=2)
	
	print("customer's hours before booking: {}".format(c.email))
	
	b = Booking.objects.create_booking(c, v, d, now, tom)

	print(b)
	print("customer's hours after booking: {}".format(c.email))
	
	
def delete_booking():
	c = Customer.objects.get(id=5)
	
	booking_list = Booking.objects.bookings(c)
	
	print("customer's hours before deletion: {}".format(c.email))
	
	Booking.objects.delete_booking(c, booking_list[0])
	
	print("customer's hours after deletion: {}".format(c.email))
