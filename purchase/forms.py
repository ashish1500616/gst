from django import forms

from .models import Vendor, Product, Tax


class VendorForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Vendor
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     superVendorForm, self).__init__(*args, **kwargs)
    #
    # def clean(self):
    #     cleaned_data=superVendorForm, self).clean()
    #     return cleaned_data


class ProductForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Product
        fields = '__all__'


class TaxForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Tax
        fields = '__all__'
