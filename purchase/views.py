from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Vendor
from .forms import VendorForm, ProductForm, TaxForm

# Create your views here.


def post_home(request):
    return render(request, 'purchase/home.html', {})


def addVendors(request):
    # VendorFormSet = modelformset_factory(Vendor, fields=('__all__'))
    # if request.method == 'POST':
    #     formset = VendorFormSet(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #         # do something.
    #         return
    # else:
    #     formset = VendorFormSet()
    # return render(request, 'purchase/addvendors.html', {'formset': formset})

    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            form.save()
            return redirect('post_home')  # redirect('post_detail', pk=post.pk)
    else:
        form = VendorForm()
    return render(request, 'purchase/addvendors.html', {'form': form})


def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_home')  # redirect('post_detail', pk=post.pk)
    else:
        form = ProductForm()
    return render(request, 'purchase/addProduct.html', {'form': form})


def addTax(request):
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_home')  # redirect('post_detail', pk=post.pk)
    else:
        form = TaxForm()
    return render(request, 'purchase/addTax.html', {'form': form})
