from django.contrib import admin

# Register your models here.


from .models import Vendor, Product, Tax

# class Vendor(admin.ModelAdmin):
#     pass


admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Tax)
