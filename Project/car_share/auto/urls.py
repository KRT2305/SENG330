from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<customer_id>[0-9]+)/bookings/$', views.bookings, name='bookings'),
    url(r'^(?P<customer_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<customer_id>[0-9]+)/create_booking/$', views.create_booking, name='create_booking'),
    url(r'^(?P<customer_id>[0-9]+)/my_bookings/$', views.my_bookings, name='my_bookings'),
]
	
