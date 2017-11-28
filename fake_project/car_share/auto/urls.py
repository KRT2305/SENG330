from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<customer_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<customer_id>[0-9]+)/bookings/$', views.bookings, name='bookings'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    ##url(r'^account_activated/$', views.account_activated, name='account_activated'),
   

]
	
