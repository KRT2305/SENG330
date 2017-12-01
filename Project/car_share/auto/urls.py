from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<customer_id>[0-9]+)/bookings/$', views.bookings, name='bookings'),
    url(r'^(?P<customer_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<customer_id>[0-9]+)/create_booking/$', views.create_booking, name='create_booking'),
    url(r'^(?P<customer_id>[0-9]+)/my_bookings/$', views.my_bookings, name='my_bookings'),
    url(r'^(?P<customer_id>[0-9]+)/delete_booking/$', views.my_bookings, name='delete_booking'),
    url(r'^(?P<customer_id>[0-9]+)/booking_created/$', views.booking_created, name='booking_created'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]
	
