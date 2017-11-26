from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Customer, Depot, Vehicle, Booking
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    customer_list = Customer.objects.order_by('name')
   # output = ', '.join([str(customer) for customer in customer_list])
    return render(
        request,
        'index.html',
        context={'customer_list':customer_list},
    )

def detail(request, customer_id):
    return HttpResponse("You're viewing customer %s" % customer_id)

def bookings(request, customer_id):
    response = "You're looking at the bookings of customer %s."
    return HttpResponse(response % customer_id)





