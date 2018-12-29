from django.contrib import admin

# Register your models here.


from .models import Vendor, Product, Tax, Country, State, Town, PurchaseInvoice, SalesStatement, VSalesStatement

# class Vendor(admin.ModelAdmin):
#     pass


admin.site.register(Vendor)
admin.site.register(Product)
# admin.site.register(Product)
admin.site.register(Tax)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Town)
admin.site.register(PurchaseInvoice)
admin.site.register(SalesStatement)
admin.site.register(VSalesStatement)
