from django.shortcuts import render
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Worker, Attendence
from .forms import WorkerForm
from django.views.generic import ListView, CreateView, UpdateView
import datetime


class AddWorker(CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy('purchase:home')


def logAttendence(request):
    nameOfWorker = Worker.objects.all()
    td = datetime.date.today()
    if(request.method == POST):
        pass
    return render(request, 'tokenapp/log_attendence.html', {'now': nameOfWorker, 'today_date': td})


def submit_attendence(request):

    pass
    return render(request, 'tokenapp/log_attendence.html', {'now': nameOfWorker, 'today_date': td})
