from django.db import models

# Create your models here.


class Vendor(models.Model):
    country_choices = (
        ('IN', 'India'),
        ('NE', 'Nepal')
    )
    state_choices = (
        ('BR', 'BIHAR'),
        ('ND', 'NEW DELHI')
    )
    name = models.CharField(max_length=30, primary_key=True, blank=False)
    contactPerson = models.CharField(max_length=30)
    contactNo = models.CharField(
        max_length=10, blank=True, null=True, default="")
    address = models.CharField(blank=True, max_length=100)
    landMark = models.CharField(blank=True, max_length=100)
    country = models.CharField(max_length=2, choices=country_choices)
    state = models.CharField(max_length=2, choices=state_choices)
    pincode = models.CharField(blank=True, max_length=6, default="")
    fax_no = models.CharField(blank=True, max_length=15, default="")
    website = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    gst_pan = models.CharField(blank=True, max_length=15, default="")

    def __str__(self):
        return self.name
