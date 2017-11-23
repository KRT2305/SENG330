from django.http import HttpResponse

def index(request):
    return HttpResponse("Polls index.")

def detail(request, customer_id):
    return HttpResponse("You're viewing customer {}".format(customer_id)

def bookings(request, customer_id):
    response = "You're looking at the bookings of customer %s."
    return HttpResponse(response % customer_id)





