from django.contrib import admin

# Register your models here.


from .models import Worker, Attendence

admin.site.register(Worker)
admin.site.register(Attendence)
