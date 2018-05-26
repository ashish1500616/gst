from django.contrib import admin

# Register your models here.


from .models import Vendor

# class Vendor(admin.ModelAdmin):
#     pass


admin.site.register(Vendor)
