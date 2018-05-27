from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^addvendor/$', views.addVendors, name='add_Vendors'),
    url(r'^addproduct/$', views.addProduct, name='add_Products'),
    url(r'^addtax/$', views.addTax, name='add_Tax'),
    url(r'^$', views.post_home, name='home'),
]
