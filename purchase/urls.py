from django.conf.urls import url
from django.urls import re_path
# from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    url(r'^addvendor/$', views.AddVendors.as_view(), name='vendor_add'),
    url(r'^add-sales-statement/$', views.AddSalesStatement.as_view(),
        name='salesstatement_add'),
    re_path(r'^statement/(?P<fyear>[0-9]{4})/(?P<fmonth>[0-9]{2})/(?P<fdate>[0-9]{2})/(?P<tyear>[0-9]{4})/(?P<tmonth>[0-9]{2})/(?P<tdate>[0-9]{2})/$',
            views.ViewStatementBetweenRange, name='view_statement'),
    url(r'^view-sales-statement/$', views.ViewSaleStatement.as_view(),
        name='view_sales_statement_add'),
    url(r'^addproduct/$', views.addProduct, name='add_Products'),
    url(r'^addtax/$', views.addTax, name='add_Tax'),
    url(r'^purchaseinvoice/$', views.AddPurchaseInvoice.as_view(),
        name='purchase_invoice'),
    url(r'^$', views.home, name='home'),
    url('ajax/load-states/', views.load_states, name='ajax_load_states'),
    url('ajax/load-towns/', views.load_towns, name='ajax_load_towns'),
    url('ajax/load-selling-price/', views.load_sellingPrice,
        name='ajax_load_selling_price')
]
