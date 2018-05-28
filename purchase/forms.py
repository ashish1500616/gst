from django import forms

from .models import Vendor, Product, Tax, Country, State


class VendorForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Vendor
        fields = ('name', 'country', 'state')

    # state = forms.ModelChoiceField(
    #     queryset=State.objects.all(), empty_label=None)

    # def __init__(self, *args, **kwargs):
    #     superVendorForm, self).__init__(*args, **kwargs)
    #
    # def clean(self):
    #     cleaned_data=superVendorForm, self).clean()
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                countryName = self.data.get('country')
                self.fields['state'].queryset = State.objects.filter(
                    country_name_id=countryName).order_by('state_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'state_name')


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
