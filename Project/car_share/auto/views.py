from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Customer, Depot, Vehicle, Booking
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404

@login_required
def index(request):
    customer_list = Customer.objects.order_by('last_name')
    booking_list = Booking.objects.bookings();
    # output = ', '.join([str(customer) for customer in customer_list])
    return render(
        request,
        'index.html',
        context={'customer_list': customer_list, 'booking_list': booking_list},
    )

@login_required
def detail(request, customer_id):
    return HttpResponse("You're viewing customer %s" % customer_id)

'''def logged_in():
    return (Customer.objects.get(id=customer_id)) =='''

@login_required
#@user_passes_test(logged_in)
def bookings(request, customer_id):
    booking_list = Booking.objects.bookings(Customer.objects.get(id=customer_id))
    return render(
        request,
        'bookings.html',
        context={'booking_list': booking_list},
    )

@login_required
def profile(request, customer_id):
    current_customer = Booking.objects.bookings(Customer.objects.get(id=customer_id))
    return render(
        request,
        'profile.html',
        context={'current_customer': current_customer},
    )

@login_required
def create_booking(request, customer_id):
    current_customer = Customer.objects.get(id=customer_id)
    return render(
        request,
        'create_booking.html',
        context={'current_customer': current_customer},
    )

@login_required
def my_bookings(request, customer_id):
    booking_list = Booking.objects.bookings(Customer.objects.get(id=customer_id))
    depot_list = Depot.objects.all()
    return render(
        request,
        'my_bookings.html',
        context={'booking_list': booking_list, 'depot_list': depot_list},
    )



