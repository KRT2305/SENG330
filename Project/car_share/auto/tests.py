from django.test import TestCase
from .models import Customer, Vehicle, Depot, Booking

import datetime

def test():
	c = Customer.objects.get(id=1)
	d = Depot.objects.get(id=1)
	v = Vehicle.objects.get(id=1)

	now = datetime.datetime.now()

	tom = now + datetime.timedelta(days=2)

	b = Booking.objects.create_booking(c, v, d, now, tom)

	print(b)




