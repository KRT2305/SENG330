from django.db import models


class DepotQuerySet(models.QuerySet):
	def depots(self):
		return self


class VehicleQuerySet(models.QuerySet):
	def vehicles(self, depot=None, v_type=None):
		if not depot:
			return self
		elif not v_type:
			return self.filter(depot=depot)
		else:
			return self.filter(depot=depot, v_type=v_type)


class BookingQuerySet(models.QuerySet):
	def bookings(self, customer=None, vehicle=None, depot=None):
		if customer:
			return self.filter(customer=customer)
		if vehicle:
			return self.filter(vehicle=vehicle)
		if depot:
			return self.filter(depot=depot)
		return self


