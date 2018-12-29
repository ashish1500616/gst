from django.db import models
import datetime
from django import forms

# Create your models here.


class Tax(models.Model):
    taxName = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=10, decimal_places=2,
                                primary_key=True, blank=False, default=0)

    def __str__(self):
        return (str(self.value) + "%   ")


class Country(models.Model):
    country_cd = models.CharField(blank=True, max_length=2)
    country_name = models.CharField(
        blank=False, primary_key=True, max_length=20, default="")

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_cd = models.CharField(blank=True, max_length=2)
    state_name = models.CharField(blank=True, primary_key=True, max_length=20)
    country_name = models.ForeignKey(
        Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class Town(models.Model):
    town_cd = models.CharField(blank=True, max_length=2)
    town_name = models.CharField(blank=True, primary_key=True, max_length=20)
    state_name = models.ForeignKey(
        State, on_delete=models.CASCADE)
    country_name = models.ForeignKey(
        Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.town_name


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
    # country = models.CharField(max_length=2, choices=country_choices)

    # country = models.ForeignKey(
    #     Country, on_delete=models.CASCADE, related_name='vendor_country', default="")
    # state = models.ForeignKey(
    #     State, on_delete=models.CASCADE, related_name='vendor_state', default="")

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    town = models.ForeignKey(Town, on_delete=models.SET_NULL, null=True)

    # country = models.CharField(max_length=2, choices=country_choices)
    # state = models.CharField(max_length=2, choices=country_choices)
    pincode = models.CharField(blank=True, max_length=6, default="")
    fax_no = models.CharField(blank=True, max_length=15, default="")
    website = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    gst_pan = models.CharField(blank=True, max_length=15, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    measurement_choices = (
        ('BAG', 'BAG'),
        ('BAGS', 'BAGS'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=50)
    sellPrice = models.BigIntegerField(blank=True, default=0)
    purchasePrice = models.BigIntegerField(blank=True)
    productCode = models.CharField(blank=True, max_length=15)
    unitMeasurement = models.CharField(
        max_length=5, choices=measurement_choices)
    stockAvailable = models.CharField(blank=True, max_length=50)
    # models.ManyToManyField(Tax, related_name='product_cgst')
    cgst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_cgst', default=0)
    # models.ManyToManyField(Tax, related_name='product_sgst')
    sgst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_sgst', default=0)
    # models.ManyToManyField(Tax, related_name='product_igst')
    igst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_igst', default=0)

    def __str__(self):
        return (self.name)


class PurchaseInvoice(models.Model):
    vendor_name = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='purchase_vendor_name', default="")
    address = models.CharField(blank=True, max_length=100)
    phone_number = models.CharField(
        max_length=10, blank=True, null=True, default="")
    gst_pan = models.CharField(blank=True, max_length=15, default="")
    purchaseInvoiceNo = models.BigIntegerField(blank=False)
    challan_no = models.BigIntegerField(blank=False)
    today_date = models.DateField(default=datetime.datetime.today)
    purchase_date = models.DateField(default=datetime.datetime.today)
    po_no = models.BigIntegerField(blank=False)
    po_date = models.DateField(default=datetime.datetime.today)


class SalesStatement(models.Model):
    choices = (
        ('IGST', 'IGST'),
        ('CGST', 'CGST'),
    )
    state_choices = (
        ('BR', 'BIHAR'),
        ('ND', 'NEW DELHI')
    )
    vendor_name = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, default="")
    date = models.DateField(default=datetime.datetime.today)
    bill_no = models.AutoField(primary_key=True)
    state = models.CharField(
        max_length=15, choices=state_choices, default="INDIA")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default="")
    tax_amount = models.BigIntegerField(blank=False, default=0)
    tax_type = models.CharField(max_length=10, choices=choices)
    tax_value = models.ForeignKey(
        Tax, on_delete=models.CASCADE, default="")
    igst = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    cgst = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    sgst = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    total_ammount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return str(self.bill_no) + "----" + str(self.date) + "----" + str(self.tax_amount) + "-----" + str(self.tax_type) + "---"


class VSalesStatement(models.Model):
    from_date = models.DateField()
    end_date = models.DateField()
