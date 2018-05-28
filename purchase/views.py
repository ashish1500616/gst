from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Vendor, Country, State, Town
from .forms import VendorForm, ProductForm, TaxForm
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.


def home(request):
    return render(request, 'purchase/home.html', {})


def load_states(request):
    country_name_id = request.GET.get('country')
    states = State.objects.filter(
        country_name_id=country_name_id).order_by('state_name')
    print(states)
    return render(request, 'purchase/state_dropdown_list_options.html', {'states': states})


def load_towns(request):
    print("\t \nInside Load Towns.\t\n")
    country_name_id = request.GET.get('country')
    state_name_id = request.GET.get('state')
    towns = Town.objects.filter(
        state_name_id=state_name_id, country_name_id=country_name_id)

    print(towns)
    return render(request, 'purchase/town_dropdown_list_options.html', {'towns': towns})


class AddVendors(CreateView):
    # def addVendors(request):
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

    # if request.method == "POST":
    #     form = VendorForm(request.POST)
    #     if form.is_valid():
    #         # post = form.save(commit=False)
    #         # post.author = request.user
    #         # post.published_date = timezone.now()
    #         form.save()
    #         return redirect('home')  # redirect('post_detail', pk=post.pk)
    # else:
    #     form = VendorForm()

    model = Vendor
    form_class = VendorForm
    success_url = reverse_lazy('home')

    # return render(request, 'purchase/addvendors.html', {'form': form})


def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect('post_detail', pk=post.pk)
    else:
        form = ProductForm()
    return render(request, 'purchase/addProduct.html', {'form': form})


def addTax(request):
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect('post_detail', pk=post.pk)
    else:
        form = TaxForm()
    return render(request, 'purchase/addTax.html', {'form': form})
