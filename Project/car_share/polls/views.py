from django.http import HttpResponse

from .models import Customer

def index(request):
    customer_list = Customer.objects.order_by('name')
    output = ', '.join([str(customer) for customer in customer_list])
    return HttpResponse(output)

def detail(request, customer_id):
    return HttpResponse("You're viewing customer %s" % customer_id)

def bookings(request, customer_id):
    response = "You're looking at the bookings of customer %s."
    return HttpResponse(response % customer_id)





