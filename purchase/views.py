from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Vendor, Country, State, Town, PurchaseInvoice, SalesStatement, VSalesStatement
from .forms import VendorForm, ProductForm, TaxForm, PurchaseInvoiceForm, SalesStatementForm, VSalesStatementForm
from django.views.generic import ListView, CreateView, UpdateView
import datetime

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
    success_url = reverse_lazy('purchase:home')

    # return render(request, 'purchase/addvendors.html', {'form': form})


class AddSalesStatement(CreateView):
    model = SalesStatement
    form_class = SalesStatementForm
    success_url = reverse_lazy('purchase:home')


class ViewSaleStatement(CreateView):
    model = VSalesStatement
    form_class = VSalesStatementForm
    # fromYear = 0, fromMonth = 0, fromDate = 0, toYear = 0, toMonth = 0, toDate = 0

    def post(self, request):
        global fromYear, fromMonth, fromDate, toYear, toMonth, toDate
        print(request.POST)
        from_date = request.POST.get("from_date")
        end_date = request.POST.get("end_date")
        from_date = from_date.split("/")
        print(from_date)
        end_date = end_date.split("/")
        print(end_date)
        fromYear = from_date[2]
        fromMonth = from_date[0]
        fromDate = from_date[1]
        toYear = end_date[2]
        toMonth = end_date[0]
        toDate = end_date[1]
        return HttpResponseRedirect(self.get_success_url(fromYear, fromMonth, fromDate, toYear, toMonth, toDate))

    def get_success_url(self, fromYear, fromMonth, fromDate, toYear, toMonth, toDate):
        return reverse_lazy(
            'purchase:view_statement', kwargs={'fyear': fromYear, 'fmonth': fromMonth, 'fdate': fromDate, 'tyear': toYear, 'tmonth': toMonth, 'tdate': toDate})


def ViewStatementBetweenRange(request, fyear, fmonth, fdate, tyear, tmonth, tdate):
    # sd = fyear + '-' + fmonth + '-' + fdate
    # ed = tyear + '-' + tmonth + '-' + tdate
    # print(type(fyear))
    start_date = datetime.date(int(fyear), int(fmonth), int(fdate))
    end_date = datetime.date(int(tyear), int(tmonth), int(tdate))
    purchase_statement_views = SalesStatement.objects.filter(
        date__range=(start_date, end_date)).order_by('date')
    p_s_5_igst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=5.00, tax_type="IGST").order_by('date')
    # Array Contains IGST 5 values
    t_p_s_5_igst = [0, 0, 0]
    # Calculate Sum Values for IGST 5 %
    for row in p_s_5_igst:
        t_p_s_5_igst[0] = t_p_s_5_igst[0] + row.tax_amount
        t_p_s_5_igst[1] = t_p_s_5_igst[1] + row.igst
        t_p_s_5_igst[2] = t_p_s_5_igst[2] + row.total_ammount

    p_s_12_igst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=12.00, tax_type="IGST").order_by('date')
    # Array Contains IGST 12 values
    t_p_s_12_igst = [0, 0, 0]
    # Calculate Sum Values for IGST 12 %
    for row in p_s_12_igst:
        t_p_s_12_igst[0] = t_p_s_12_igst[0] + row.tax_amount
        t_p_s_12_igst[1] = t_p_s_12_igst[1] + row.igst
        t_p_s_12_igst[2] = t_p_s_12_igst[2] + row.total_ammount
    p_s_18_igst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=18.00, tax_type="IGST").order_by('date')

    # Array Contains IGST 18 values
    t_p_s_18_igst = [0, 0, 0]
    # Calculate Sum Values for IGST 18 %
    for row in p_s_18_igst:
        t_p_s_18_igst[0] = t_p_s_18_igst[0] + row.tax_amount
        t_p_s_18_igst[1] = t_p_s_18_igst[1] + row.igst
        t_p_s_18_igst[2] = t_p_s_18_igst[2] + row.total_ammount

    #CGST /SGST
    p_s_25_cgst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=2.50, tax_type="CGST").order_by('date')
    # Array Contains CGST 2.5 values
    t_p_s_25_cgst = [0, 0, 0, 0]
    # Calculate Sum Values for CGST 25 %
    for row in p_s_25_cgst:
        t_p_s_25_cgst[0] = t_p_s_25_cgst[0] + row.tax_amount
        t_p_s_25_cgst[1] = t_p_s_25_cgst[1] + row.cgst
        t_p_s_25_cgst[2] = t_p_s_25_cgst[2] + row.sgst
        t_p_s_25_cgst[3] = t_p_s_25_cgst[3] + row.total_ammount

    p_s_6_cgst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=6.00, tax_type="CGST").order_by('date')

    # Array Contains CGST 6 values
    t_p_s_6_cgst = [0, 0, 0, 0]
    # Calculate Sum Values for CGST 6 %
    for row in p_s_6_cgst:
        t_p_s_6_cgst[0] = t_p_s_6_cgst[0] + row.tax_amount
        t_p_s_6_cgst[1] = t_p_s_6_cgst[1] + row.cgst
        t_p_s_6_cgst[2] = t_p_s_6_cgst[2] + row.sgst
        t_p_s_6_cgst[3] = t_p_s_6_cgst[3] + row.total_ammount
    p_s_9_cgst = SalesStatement.objects.filter(
        date__range=(start_date, end_date), tax_value=9.00, tax_type="CGST").order_by('date')

    # Array Contains CGST 9 values
    t_p_s_9_cgst = [0, 0, 0, 0]
    # Calculate Sum Values for CGST 6 %
    for row in p_s_9_cgst:
        t_p_s_9_cgst[0] = t_p_s_9_cgst[0] + row.tax_amount
        t_p_s_9_cgst[1] = t_p_s_9_cgst[1] + row.cgst
        t_p_s_9_cgst[2] = t_p_s_9_cgst[2] + row.sgst
        t_p_s_9_cgst[3] = t_p_s_9_cgst[3] + row.total_ammount

    total_tax_ammount = t_p_s_5_igst[0] + t_p_s_12_igst[0] + \
        t_p_s_18_igst[0] + t_p_s_25_cgst[0] + t_p_s_6_cgst[0] + t_p_s_9_cgst[0]
    total_igst = t_p_s_5_igst[1] + t_p_s_12_igst[1] + t_p_s_18_igst[1]
    total_cgst = t_p_s_25_cgst[1] + t_p_s_6_cgst[1] + t_p_s_9_cgst[1]
    total_sgst = t_p_s_25_cgst[2] + t_p_s_6_cgst[2] + t_p_s_9_cgst[2]
    total_ammount = t_p_s_5_igst[2] + t_p_s_12_igst[2] + \
        t_p_s_18_igst[2] + t_p_s_25_cgst[3] + \
        t_p_s_6_cgst[3] + t_p_s_9_cgst[3]
    total_sum_5_igst = t_p_s_5_igst[2]
    total_sum_12_igst = t_p_s_12_igst[2]
    total_sum_18_igst = t_p_s_18_igst[2]
    total_sum_25_cgst = t_p_s_25_cgst[3]
    total_sum_6_cgst = t_p_s_6_cgst[3]
    total_sum_9_cgst = t_p_s_9_cgst[3]
    # for row in purchase_statement_views:
    #     tax_V = float(str(row.tax_value).replace("%", ""))
    #     if row.tax_type == "IGST":
    #         if tax_V == 5:
    #             total_sum_5_igst = total_sum_5_igst + row.igst
    #         elif tax_V == 12:
    #             total_sum_12_igst = total_sum_12_igst + row.igst
    #         elif tax_V == 18:
    #             total_sum_18_igst = total_sum_18_igst + row.igst
    #     else:
    #         if tax_V == 2.5:
    #             total_sum_25_cgst = total_sum_25_cgst + row.cgst + row.sgst
    #             total_sum_25_cgst = total_sum_25_cgst / 2
    #         elif tax_V == 6:
    #             total_sum_6_cgst = total_sum_6_cgst + row.cgst + row.sgst
    #             total_sum_6_cgst = total_sum_6_cgst / 2
    #         elif tax_V == 9:
    #             total_sum_9_cgst = total_sum_9_cgst + row.cgst + row.sgst
    #             total_sum_9_cgst = total_sum_9_cgst / 2
    #     total_tax_ammount = total_tax_ammount + row.tax_amount
    #     total_igst = total_igst + row.igst
    #     total_cgst = total_cgst + row.cgst
    #     total_sgst = total_sgst + row.sgst
    #     total_ammount = total_ammount + row.total_ammount
    return render(request, 'purchase/statement.html', {'t_p_s_5_igst_tax_amount': t_p_s_5_igst[0], 't_p_s_5_igst': t_p_s_5_igst[1], 't_p_s_5_igst_total_amount': t_p_s_5_igst[2],
                                                       't_p_s_12_igst_tax_amount': t_p_s_12_igst[0], 't_p_s_12_igst': t_p_s_12_igst[1], 't_p_s_12_igst_total_amount': t_p_s_12_igst[2],
                                                       't_p_s_18_igst_tax_amount': t_p_s_18_igst[0], 't_p_s_18_igst': t_p_s_18_igst[1], 't_p_s_18_igst_total_amount': t_p_s_18_igst[2],
                                                       't_p_s_25_cgst_tax_amount': t_p_s_25_cgst[0], 't_p_s_25_cgst': t_p_s_25_cgst[1], 't_p_s_25_sgst': t_p_s_25_cgst[2], 't_p_s_25_cgst_total_amount': t_p_s_25_cgst[3],
                                                       't_p_s_6_cgst_tax_amount': t_p_s_6_cgst[0], 't_p_s_6_cgst': t_p_s_6_cgst[1], 't_p_s_6_sgst': t_p_s_6_cgst[2], 't_p_s_6_cgst_total_amount': t_p_s_6_cgst[3],
                                                       't_p_s_9_cgst_tax_amount': t_p_s_9_cgst[0], 't_p_s_9_cgst': t_p_s_9_cgst[1], 't_p_s_9_sgst': t_p_s_9_cgst[2], 't_p_s_9_cgst_total_amount': t_p_s_9_cgst[3],
                                                       'ps5igst': p_s_5_igst, 'ps12igst': p_s_12_igst, 'ps18igst': p_s_18_igst,
                                                       'ps25cgst': p_s_25_cgst, 'ps6cgst': p_s_6_cgst, 'ps9cgst': p_s_9_cgst,
                                                       'purchase_statement_views': purchase_statement_views, 'sd': start_date, 'ed': end_date, 'tta': total_tax_ammount, 'tigst': total_igst, 'tcgst': total_cgst, 'tsgst': total_sgst, 'ta': total_ammount, 'igst5': total_sum_5_igst, 'igst12': total_sum_12_igst, 'igst18': total_sum_18_igst, 'cgst25': total_sum_25_cgst, 'cgst6': total_sum_6_cgst, 'cgst9': total_sum_9_cgst})


class AddPurchaseInvoice(CreateView):
    model = PurchaseInvoice
    form_class = PurchaseInvoiceForm
    success_url = reverse_lazy('home')


def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect('post_detail', pk=post.pk)
            return redirect('purchase:home')
    else:
        form = ProductForm()
    return render(request, 'purchase/addProduct.html', {'form': form})


def addTax(request):
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect('post_detail', pk=post.pk)
            return redirect('purchase:home')
    else:
        form = TaxForm()
    return render(request, 'purchase/addTax.html', {'form': form})
