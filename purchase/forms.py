from django import forms

from .models import Vendor


class VendorForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Vendor
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     superVendorForm, self).__init__(*args, **kwargs)
    #
    # def clean(self):
    #     cleaned_data = superVendorForm, self).clean()
    #     return cleaned_data
    #
