from django import forms

from .models import Vendor, Product, Tax, Country, State, Town


class VendorForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Vendor
        # fields = ('name', 'country', 'state')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        self.fields['town'].queryset = Town.objects.none()

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

        if 'state' in self.data:
            try:
                countryName = self.data.get('country')
                stateName = self.data.get('state')
                self.fields['town'].queryset = Town.objects.filter(
                    state_name_id=stateName, country_name_id=countryName).order_by('town_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['town'].queryset = self.instance.country.town_set.order_by(
                'town_name')


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
