from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Depot)
admin.site.register(Vehicle)
admin.site.register(Booking)


