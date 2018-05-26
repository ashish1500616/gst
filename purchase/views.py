from django.shortcuts import render
from django.shortcuts import render
from .models import Vendor
# Create your views here.

ef manage_vendors(request):
    VendorFormSet = modelformset_factory(Vendor, fields=('__all__'))
    if request.method == 'POST':
        formset = VendorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = VendorFormSet()
    return render(request, 'manage_Vendors.html', {'formset': formset})
