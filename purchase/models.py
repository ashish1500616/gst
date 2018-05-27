from django.db import models

# Create your models here.


class Tax(models.Model):
    taxName = models.CharField(blank=True, max_length=20)
    value = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return (str(self.value) + "%   " + self.taxName)


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


class Product(models.Model):
    measurement_choices = (
        ('BAG', 'BAG'),
        ('BAGS', 'BAGS'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=50)
    sellPrice = models.BigIntegerField(blank=True)
    purchasePrice = models.BigIntegerField(blank=True, )
    productCode = models.CharField(blank=True, max_length=15)
    unitMeasurement = models.CharField(
        max_length=5, choices=measurement_choices)
    stockAvailable = models.CharField(blank=True, max_length=50)
    # models.ManyToManyField(Tax, related_name='product_cgst')
    cgst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_cgst', default="")
    # models.ManyToManyField(Tax, related_name='product_sgst')
    sgst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_sgst', default="")
    # models.ManyToManyField(Tax, related_name='product_igst')
    igst = models.ForeignKey(
        Tax, on_delete=models.CASCADE, related_name='product_igst', default="")

    def __str__(self):
        return self.name
