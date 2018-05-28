from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^addvendor/$', views.AddVendors.as_view(), name='vendor_add'),
    url(r'^addproduct/$', views.addProduct, name='add_Products'),
    url(r'^addtax/$', views.addTax, name='add_Tax'),
    url(r'^$', views.home, name='home'),
    url('ajax/load-states/', views.load_states, name='ajax_load_states'),
]
